import re
import pandas as pd
import numpy as np
import time
from DC_settings import arrange_cols, fill_nans
from PROCESSOR.plates_parser import main as plates_parser

# Функция по очистке датафрейма
def clean_df_headers(df, col_keyword_pairs):
    for keyword, colnames in col_keyword_pairs.items():
        for colname in colnames:
            df[colname][df[colname].apply(lambda val, keyword=keyword: any(re.findall(keyword, str(val))))] = np.nan
    return df

    
def main(src2_get):
    """
    df из источника представляет собой оперативную сводку, за дневную и ночную смену, ориентированную на визуализацию. 
    Сводка используется как опорный материал при проведении селекторных совещаний. Требуется привести данные, полученные из источника в матричный вид, 
    для последующей выгрузки в БД. Из-за слияния некоторых ячеек в экселе и разбивки данных на 2 смены, при трансформации данных стоят задачи по 
    выравниваю строк по горизонтали, и слиянию таблиц 2х смен по вертикали, при вертикальном распределении общих параметров.
    """ 

    df = src2_get
    
    
    # Собираем текущую дату из заголовка колонки 0 в df, так как она распредилилась в название заголовка при открытии источника в src2_ops_get.py
    date = df.columns[0]
    L_date = [date.strftime('%d.%m.%Y')]
    
    # Задаем колонкам нужные имена
    df.rename(columns=
              {
                  df.columns[0]: 'General', 
                  df.columns[1]: 'Locations',
                  df.columns[2]: 'Units',
                  df.columns[3]: 'Tasks',
                  df.columns[4]: 'Urgency',
                  df.columns[5]: 'Mileage',
                  df.columns[6]: 'Units_2',
                  df.columns[7]: 'Tasks_2',
                  df.columns[8]: 'Urgency_2',
                  df.columns[9]: 'Mileage_2',
                  }, inplace=True)
    
    # Вставляем новую пустую колонку под марки автомобилей, которые вытянем из колонки 'General'
    df['Brands'] = np.nan
   
    # Переносим марки автомобилей типа "Chevrolet" в колонку Brands из колонки 'General', используя regex
    for idx, val in df['General'].items():
        if re.findall('[A-z]+', str(val)):
            df.loc[idx, 'Brands'] = val
    # Убираем смешанную колонку 'General' за ненадобностью
    df = df.drop(columns=['General'])
    
    # Дублируем колонки "Brands" и "Locations" для выравнивая df по вертикали
    df['Brands_2'] = df['Brands']
    df['Locations_2'] = df['Locations']
        
    # Перераспределяем колонки в нужном порядке, отправляя лист в функцию arrange_cols
    df = arrange_cols(df, ['Brands', 'Locations', 'Units', 'Tasks', 'Urgency', 'Mileage',
                            'Brands_2', 'Locations_2', 'Units_2', 'Tasks_2', 'Urgency_2', 'Mileage_2',])
    
    # Чистим df от ненужных заголовков, унаследованных из источника
    # Маппим регексы на нужные колонки df в словаре
    col_keyword_pairs = {
        'втомоб': ('Units', 'Units_2'),
        'Задание': ('Tasks', 'Tasks_2'),
        'Приоритет': ('Urgency', 'Urgency_2'),
        'Пробег': ('Mileage', 'Mileage_2'),
    }

    # Отправляем словарь в функцию clean_df_headers, получаем очищенный df
    df = clean_df_headers(df, col_keyword_pairs)
    
    
    # Заполняем пустоты в колонках
    L_colnames = ['Brands', 'Brands_2', 'Locations', 'Locations_2']
    for i in L_colnames:
        df = fill_nans(df, i)
    
    
    # Разбиваем df на группы по маркам автомобилей 'Brands'
    grouped_df = df.groupby('Brands')
    
    # Создаем лист для сборки групп после преобразований
    merged_groups = []
    # Проходим по листу с группами
    for _, group_df in grouped_df:
        # Разбиваем группы на 2 отделения: дневной и ночной смены
        df1 = group_df[['Brands', 'Locations', 'Units', 'Tasks', 'Urgency', 'Mileage']]
        df2 = group_df[['Brands_2', 'Locations_2', 'Units_2', 'Tasks_2', 'Urgency_2', 'Mileage_2']]
        # Сливаем их относительно друг друга по вертикали по всем группам
        concatenated_df = pd.concat([df1, df2], axis=0)
        # Загоняем преобразованные группы в лист для сборки
        merged_groups.append(concatenated_df)
        
    # Собираем группы в единый датафрейм
    df = pd.concat(merged_groups, axis=0)
    
    
    # Переносим значения из "ночного блока" в "дневной" при помощи паттерн маски
    mask = df['Brands'].isnull() & ~df['Brands_2'].isnull()
    df.loc[mask, 'Brands'] = df.loc[mask, 'Brands_2']
    df.loc[mask, 'Locations'] = df.loc[mask, 'Locations_2']
    df.loc[mask, 'Units'] = df.loc[mask, 'Units_2']
    df.loc[mask, 'Tasks'] = df.loc[mask, 'Tasks_2']
    df.loc[mask, 'Urgency'] = df.loc[mask, 'Urgency_2']
    df.loc[mask, 'Mileage'] = df.loc[mask, 'Mileage_2']

    # Убираем ненужные исходные колонки ночной смены
    df = df.loc[:, ['Brands', 'Locations', 'Units', 'Tasks', 'Urgency', 'Mileage']]
    
    # Равняем df, убирая лишние пустоты
    df = df.dropna(subset=['Units'], thresh=1)
    df.reset_index(drop=True, inplace=True)
    
    # Выравниваем лист с датой по длине с датафреймом
    L_date = L_date * len(df)
    df['Date'] = L_date
    
    # Забираем колонку с названиями автомобилей и их номерами для парсинга номеров
    L_plates = df.loc[:, 'Units'].tolist()
    # Отправляем лист во вспомогательный модуль
    L_plates = plates_parser(L_plates)
    # Добавляем лист в качестве колонки
    df['Plates'] = L_plates
    
    # Перераспределяем колонки в нужном порядке, отправляя лист в функцию arrange_cols 
    # во вспомогательном модуле DC_settings.py
    df = arrange_cols(df, ['Date', 'Brands', 'Locations','Units', 
                           'Plates', 'Tasks', 'Urgency', 'Mileage'])
    
    # Возвращаем датафрейм в _main.py
    return df
   
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    print(f'--- %s seconds --- % {(time.time() - start_time)}')
from __init__ import *
from DC_settings import *

from PROCESSOR.plates_parser import main as plates_parser

def main(src3_get):
    """
    df из источника представляет собой бухгалтерскую выгрузку из 1С, которую этот модуль приводит в матричный вид.
    """ 
    df = src3_get
    
    # Задаем колонкам нужные имена
    df.rename(columns=
              {
                  df.columns[1]: 'General', 
                  df.columns[2]: 'Depreciation',
                  df.columns[3]: 'Prod_date',
                  df.columns[4]: 'Code',
                  df.columns[5]: 'Drivers',
                  df.columns[6]: 'Ratings',
                  }, inplace=True)
    
    # Оставляем нужные колонки
    df = df.loc[:, ['General', 'Drivers', 'Ratings']]
    
    # Derivating new cols
    df['Brands'] = np.nan
    df['Locations'] = np.nan
    df['Units'] = np.nan
    
    # Moving data 
    def copy_col(pattern, col):
        for idx, val in df['General'].items():
            if re.findall(pattern, str(val)):
                df.loc[idx, col] = val
        
    copy_col(r'^[A-Za-z]+(?:-[A-Za-z]+)?$', 'Brands')
    copy_col('АО', 'Locations')
    copy_col(r'[А-я]\s*\d{3}\s*[А-я]{2}\s*\d+\S+', 'Units')
    
    
    # Заполняем пустоты в колонках
    L_colnames = ['Brands', 'Locations']
    for i in L_colnames:
        df = fill_nans(df, i)
    
    # Равняем df, убирая лишние пустоты
    df = df.dropna(subset=['Units'], thresh=1)
    df.reset_index(drop=True, inplace=True)
    
    # Забираем колонку с названиями автомобилей и их номерами для парсинга номеров
    L_plates = df.loc[:, 'Units'].tolist()
    # Отправляем лист во вспомогательный модуль
    L_plates = plates_parser(L_plates)
    L_plates = [[re.sub(',', ', ', i[0]) + i[1] if len(i) > 1 else re.sub(',', '', i[0])] for i in L_plates]
    L_plates = [x[0].split(',') for x in L_plates]
    
    # Добавляем лист в качестве колонки
    df['Plates'] = L_plates
    
    # Парсим названия автомобилей
    L_units = df.loc[:, 'Units'].tolist()
    regex = r'([A-z]+\s[A-z]+\-*\d*)|([A-z]+\s\d\s\Series*)|([A-z].*Class)|([A-z].*GLE)'
    L_units = [''.join(match for match in re.findall(regex, x)[0] if match) for x in L_units]
    df['Units'] = L_units
    # Перераспределяем колонки в нужном порядке, отправляя лист в функцию arrange_cols 
    # во вспомогательном модуле DC_settings.py
    df = arrange_cols(df, ['Brands', 'Locations', 'Units', 'Plates',  'Drivers', 'Ratings'])
    
    return df

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

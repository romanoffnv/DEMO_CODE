# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

from PROCESSOR.plates_parser import main as plates_parser

def main(src2_get):
    df = src2_get
    
    # Собираем дату из ячейки
    date = df.columns[0]
    L_date = [date.strftime('%d.%m.%Y')]
    
    # Забираем марки автомобилей и административные округи в листы
    def listing_cars_locs(col, df, flag):
        L = df.iloc[:, col].tolist()
        L = [str(x) for x in L]
        if flag:
            L = [''.join(re.findall('[A-z]+', x)) for x in L]
        L = [x for x in L if x != '' and x != 'nan']
        return L
    
    L_brands = listing_cars_locs(0, df, True)
    L_locations = listing_cars_locs(1, df, False)
    
    # Собираем индексы границ секций блока марок автомобилей в лист
    L_section_borders = []
    for idx, val in df.iloc[:, 0].items():
        if val in L_brands:
            L_section_borders.append(idx)
    L_section_borders.append(df.index[-1])
    
    # Собираем блоки автомобилей в виде отдельных df в лист
    L_group_dfs = []
    for i in range(len(L_section_borders) - 1):
        start_idx = L_section_borders[i]
        end_idx = L_section_borders[i + 1]
        brand_section_data = df.iloc[start_idx:end_idx + 1]
        L_group_dfs.append(brand_section_data)
        
    # Create a new DataFrame to hold the final result
    final_df = pd.DataFrame()

    # Iterate over the grouped DataFrames
    for idx, i in enumerate(L_group_dfs):
        pprint(L_brands[idx])
        pprint(idx)
        pprint(L_brands[0])
        pprint(L_brands[1])
        L_brand = L_brands[idx]
        L_location = L_locations[idx]
        
        # Разбиваем df на 2 подблока по колонкам "Дневная смена", "Ночная смена"
        day = i.iloc[:, 2:6]
        night = i.iloc[:, 6:11]
        
        # Сбрасываем пустые значения перед склеиванием
        day = day.dropna()
        night = night.dropna()
        
        #  Склеиваем df блоки вертикально
        df_concat = pd.concat([day, night], axis=0).reset_index(drop=True)

        # Перебираем df, если ячейка в нулевой колонке пустая, а ячейка в 4й колонке со значением, переносим значения из "ночного блока" в "дневной"
        for idx, row in df_concat.iterrows():
            if pd.isna(row[0]) and not pd.isna(row[4]):
                df_concat.at[idx, df_concat.columns[0]] = df_concat.at[idx, df_concat.columns[4]]
                df_concat.at[idx, df_concat.columns[1]] = df_concat.at[idx, df_concat.columns[5]]
                df_concat.at[idx, df_concat.columns[2]] = df_concat.at[idx, df_concat.columns[6]]
                df_concat.at[idx, df_concat.columns[3]] = df_concat.at[idx, df_concat.columns[7]]
        
        # Убираем лишние колонки
        df_concat = df_concat.iloc[:, 0:4]
        
        # Чистим df от ненужных заголовков
        for idx, row in df_concat.iloc[:, 0].iteritems():
            if row == 'Автомобиль':
                df_concat.iloc[idx, 0] = np.nan
            
        df_concat = df_concat.dropna(subset=df_concat.columns[0:1])
        
        # Add Brand and Location columns
        df_concat['Brand'] = L_brand
        df_concat['Locations'] = L_location

        # Append the current group's data to the final DataFrame
        final_df = final_df.append(df_concat, ignore_index=True)
    df = final_df
    # Уравниваем лист с единственным значением даты по длине с df
    L_date = L_date * len(df)
    df['Date'] = L_date
    
    # Забираем колонку с названиями автомобилей для парсинга номеров
    L_plates = df.iloc[:, 0].tolist()
    L_plates = plates_parser(L_plates)
    df['Plates'] = L_plates
    
    # Задаем колонкам имена
    df.rename(columns=
              {
                  df.columns[0]: 'Units', 
                  df.columns[1]: 'Tasks',
                  df.columns[2]: 'Urgency',
                  df.columns[3]: 'Mileage',
                  }, inplace=True)

    # Перераспределяем колонки в нужном порядке
    
    cols = df.columns.tolist()
    cols = ['Date',
            'Brand',
            'Locations',
            'Units',
            'Plates',
            'Tasks',
            'Urgency',
            'Mileage',
            ]
    df = df[cols]
    # Display the final DataFrame
    print_val = df
    pprint(print_val, set_pandas_options(print_val, width=1000, colwidth=20, colmap = False))
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))


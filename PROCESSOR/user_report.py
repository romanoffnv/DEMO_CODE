import pandas as pd
import time

def main(uniplates_generalizer):
    # Распаковываем воходящие датафреймы
    df1 = uniplates_generalizer[0]
    df2 = uniplates_generalizer[1]
    df3 = uniplates_generalizer[2]
    
    # Определяем листы для составления конечного датафрейма
    # Пустые для заполенения в ходе сопоставления
    Date, Brands, Tasks, Urgency, Mileage = [], [], [], [], []
    Locations, Units, Drivers, Ratings = [], [], [], []
    # Прямые, взятые из датафрейма сопоставителя
    Plates = df1['Plates'].tolist()
    Status = df1['Status'].tolist()
    Coordinates = df1['Coordinates'].tolist()
    
    # Сопоставляемся по гос.номерам из 1го датафрейма, приведенным в общий вид, заполняем соответствующие листы
    for _, val in df1['Plates'].items():
        for idx_2, val_2 in df2['Plates'].items():
            if val == val_2:
                Date.append(df2.loc[idx_2, 'Date'])
                Brands.append(df2.loc[idx_2, 'Brands'])
                Tasks.append(df2.loc[idx_2, 'Tasks'])
                Urgency.append(df2.loc[idx_2, 'Urgency'])
                Mileage.append(df2.loc[idx_2, 'Mileage'])
        for idx_3, val_3 in df3['Plates'].items():
            if val == val_3:
                Locations.append(df3.loc[idx_3, 'Locations'])
                Units.append(df3.loc[idx_3, 'Units'])
                Drivers.append(df3.loc[idx_3, 'Drivers'])
                Ratings.append(df3.loc[idx_3, 'Ratings'])
    
    # Складываем листы в финальный датафрейм 
    df = pd.DataFrame(zip(Date, Brands, Locations, Units, Plates, Status, Coordinates, Tasks, Urgency, Mileage, Drivers, Ratings), 
                      columns = ['Date', 'Brands', 'Locations', 'Units', 'Plates', 'Status', 'Coords', 'Tasks', 'Urgency', 'Mileage', 'Drivers', 'Ratings'])
    # Возвращаем финальный датафрейм в _main.py
    return df


if __name__ == '__main__':
    main()
    start_time = time.time()
    print(f'--- %s seconds --- % {(time.time() - start_time)}')

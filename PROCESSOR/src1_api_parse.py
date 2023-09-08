import time
import pandas as pd
from PROCESSOR.plates_parser import main as plates_parser

def main(src1_get):
    # Принимаем данные полученные через API github.com в формате JSON
    # Распределяем данные по соответствующим спискам
    L_units = [x['name'] for x in src1_get]
    L_plates = list(L_units)
    L_plates = plates_parser(L_plates)
    L_status = [x['status'] for x in src1_get]
    L_locations = [str(x['location']) for x in src1_get]
    
    # Из сформированных списков создаем датафрейм и возращаем его в _main.py
    return pd.DataFrame(zip(L_units, L_plates, L_status, L_locations), columns = ['Units', 'Plates',  'Status', 'Coordinates'])


if __name__ == '__main__':
    main()
    start_time = time.time()
    print(f'--- %s seconds ---% {(time.time() - start_time)}')

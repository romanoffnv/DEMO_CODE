import os
import sys
import pandas as pd
import sqlite3
import time
from DC_settings import db_connect as dbcon

# Определяем путь к корневой папке проекта из текущей + 1 уровень вверх
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
SRC_DIR = parent_dir + r'\SRC'

def main():
    
    # Коннект к SQLlite 
    db_name = 'data.db'
    table_name = 'User_rep'
    try:
        cursor, _ = dbcon(SRC_DIR, db_name)
        
        # Функция формирования sql запросов
        def sql_request(col_names):
            columns = []
            for i in col_names:
                cursor.execute(f"SELECT {i} FROM {table_name}")
                columns.append(cursor.fetchall())
            return pd.DataFrame(zip(*columns), columns = col_names)
        df_userrep = sql_request(['Date', 'Brands', 'Locations', 'Units', 'Plates', 'Status', 'Tasks', 'Urgency'])
        df_map = sql_request(['Units', 'Plates', 'Coords'])
        df_charts = sql_request(['Status', 'Urgency', 'Ratings'])
    except sqlite3.Error:
        print('Update the data base')
    
    return df_userrep, df_map, df_charts

        
  
if __name__ ==  '__main__':
    main()
    start_time = time.time()
    print(f'--- %s seconds --- % {(time.time() - start_time)}')
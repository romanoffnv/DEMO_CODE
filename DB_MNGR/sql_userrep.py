import os
import sys

# Определяем путь к корневой папке проекта из текущей + 1 уровень вверх
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
SRC_DIR = parent_dir + '\SRC'


# Импортируем общие модули
from __init__ import *
from DC_settings import *


# Импортируем отдельные функции из общего модуля DC_settings
from DC_settings import db_connect as dbcon

def main():
    
    # Коннектимся к SQLlite 
    db_name = 'data.db'
    table_name = 'User_rep'
    try:
        cursor, cnx = dbcon(SRC_DIR, db_name)
        columns = ['Date', 'Brands', 'Locations', 'Units', 'Plates', 'Status', 'Tasks', 'Urgency']
        cols = []
        for i in columns:
            cursor.execute(f"SELECT {i} FROM {table_name}")
            cols.append(cursor.fetchall())
        df = pd.DataFrame(zip(cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6], cols[7]), columns=columns)
        print(df)
        return df 
    except sqlite3.Error as e:
        print('Update the data base')
        return 'Update the data base'
        
  
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

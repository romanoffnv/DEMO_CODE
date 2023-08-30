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
        cursor.execute(f"SELECT Status FROM {table_name}")
        L_status = cursor.fetchall()
        # pprint(L_status)
    except sqlite3.Error as e:
        print('Update the data base')
        
    online = 'online'
    offline = 'offline'
    on_count = L_status.count(online)
    off_count = L_status.count(offline)
    
    return on_count, off_count
        
  
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

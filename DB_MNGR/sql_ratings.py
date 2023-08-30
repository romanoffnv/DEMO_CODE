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
    except sqlite3.Error as e:
        print('Update the data base')
        
    # Построение графика 'Ratings'
    hi = ((df['Ratings'].astype(float) < 5.0) & (df['Ratings'].astype(float) > 4.7)).sum()
    mid = ((df['Ratings'].astype(float) < 4.7) & (df['Ratings'].astype(float) > 4.2)).sum()
    under_mid = ((df['Ratings'].astype(float) < 4.2) & (df['Ratings'].astype(float) > 3.7)).sum()
    low = ((df['Ratings'].astype(float) < 3.7) & (df['Ratings'].astype(float) > 3.3)).sum()
    trash = ((df['Ratings'].astype(float) < 3.3) & (df['Ratings'].astype(float) > 0)).sum()

    pprint(make_chart(['Высокий', 'Средний', 'Ниже среднего', 'Низкий', 'Увольнение'], [hi, mid, under_mid, low, trash], 'bar', 'Распределение рейтингов водителей'))
    
    return on_count, off_count
        
  
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

import os.path
import sqlite3
import pandas as pd

# Data base functions *********************************************************
def db_connect(x, db_name):
    path_asus = 'C:\\Users\\roman\\OneDrive\\Рабочий стол\\SANDBOX\\PS_REPORT'
    path_work = 'D:\\Users\Sauron\Desktop\SANDBOX\PS_REPORT'
    if os.path.exists(path_asus):
        file = os.path.join(path_asus, db_name)
        folder_path = path_asus
    else:
        file = os.path.join(path_work, db_name)
        folder_path = path_work
    
    cnx = sqlite3.connect(file)
    cnx.row_factory = lambda cursor, row: row[0]
    cursor = cnx.cursor()
    if x == 'cursor':
        return cursor
    elif x == 'cnx':
        return file
    elif x == 'folder_path':
        return folder_path
def db_get(db_name, table_name):
    file = db_connect('cnx', db_name)
    cnx = sqlite3.connect(file)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", cnx)
    return df

def db_post(db_name, db, df, close):
    cursor = db_connect('cursor', db)
    file = db_connect('cnx', db)
    cnx = sqlite3.connect(file)
    cursor.execute(f"DROP TABLE IF EXISTS {db_name}")
    df.to_sql(name=f'{db_name}', con=cnx, if_exists='replace', index=False)
    cnx.commit()
    if close:
        cnx.close()

def db_drop(db_name, db, close):
    cursor = db_connect('cursor', db)
    file = db_connect('cnx', db)
    cnx = sqlite3.connect(file)
    cursor.execute(f"DROP TABLE IF EXISTS {db_name}")
    if close:
        cnx.close()
    
# db = db_connect('cnx', db_name = 'data.db')    
# db_post(table_name, db, df, close = True)
# db_drop(table_name, db, close = True)

# Pandas settings *********************************************************
def set_pandas_options(df, width, colwidth, colmap):
    # Pandas
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', width)
    pd.set_option('display.max_colwidth', colwidth)
    # cmd view control
    if colmap:
        df.columns = df.columns.map(str)
        df.rename(columns=lambda x: x[:10] if len(x) > 20 else x, inplace=True)

# print_val = df_trans
# pprint(print_val, set_pandas_options(print_val, width=1000, colwidth=100, colmap = False))
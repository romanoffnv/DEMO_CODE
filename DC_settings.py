import os.path
import sqlite3
import pandas as pd

# Data base functions *********************************************************
def db_connect(SRC_DIR, db_name):
        file = os.path.join(SRC_DIR, db_name)
        cnx = sqlite3.connect(file)
        cnx.row_factory = lambda cursor, row: row[0]
        cursor = cnx.cursor()
        return cursor, cnx 

def db_get(db_name, table_name):
    file = db_connect('cnx', db_name)
    cnx = sqlite3.connect(file)
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", cnx)
    return df

def db_post(cursor, cnx, table_name, src, close):
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    src.to_sql(name=f'{table_name}', con=cnx, if_exists='replace', index=False)
    cnx.commit()
    if close:
        cnx.close()

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

# Функция перераспределения колонок в нужном порядке
def arrange_cols(df, cols):
    return df[cols]

# Функция заполнения пустот
def fill_nans(df, colname):
    df[colname] = df[colname].fillna(method='ffill')
    return df

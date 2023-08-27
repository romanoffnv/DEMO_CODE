import os
import sys

# Определяем путь к корневой папке проекта из текущей + 1 уровень вверх
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Импортируем общие модули
from __init__ import *
from DC_settings import *

# Импортируем зависимые модули
from PROCESSOR.src1_api_get import main as src1_api_get
from PROCESSOR.src1_api_parse import main as src1_api_parse
from PROCESSOR.src_xlsx_get import main as src_xlsx_get
from PROCESSOR.src2_ops_parse import main as src2_ops_parse
from PROCESSOR.src3_drvs_parse import main as src3_drvs_parse
from PROCESSOR.src3_drvs_validator import main as src3_drvs_validator
from PROCESSOR.uniplates import main as uniplates
from PROCESSOR.user_report import main as user_report

# Импортируем отдельные функции из общего модуля DC_settings
from DC_settings import db_connect as dbcon
from DC_settings import db_post as dbpost

def main():
    # Извлекаем данные из источника github.com через API в формате JSON
    src1_get = src1_api_get()
    # Парсим данные, полученные в модуле src1_api_get
    src1_parse = src1_api_parse(src1_get)
    # Извлекаем данные из источника DEMO_CODE_dispatch.xlsx, через общий модуль открытия эксель файлов src_xlsx_get
    src2_get = src_xlsx_get(parent_dir, fname = 'dispatch')
    # Парсим данные, полученные в модуле src_xlsx_get
    src2_parse = src2_ops_parse(src2_get)
    # Извлекаем данные из источника DEMO_CODE_drivers.xlsx, через общий модуль открытия эксель файлов src_xlsx_get
    src3_get = src_xlsx_get(parent_dir, fname = 'drivers')
    # Парсим данные, полученные в модуле src_xlsx_get
    src3_parse = src3_drvs_parse(src3_get)
    # Отправляем очищенные данные в модуль валидации src3_drvs_validator, для отбраковки случайных совпадений через нейросеть
    src3_validator = src3_drvs_validator(src3_parse)
    # Отправляем датафреймы, полученные из источников в модуль uniplates_generalizer для приведения гос.номеров в сопоставимый вид
    uniplates_generalizer = uniplates(src1_parse, src2_parse, src3_validator)
    # Отправляем датафреймы с приведенными данными в модуль user_report для создания сводного отчета
    userrep = user_report(uniplates_generalizer)
    # Приводим типы данных к строке
    userrep = userrep.astype(str)
    
    # Коннектимся к SQLlite 
    db_name = 'data.db'
    table_name = 'User_rep'
    cursor, cnx = dbcon(parent_dir + '\SRC', db_name)
    
    
    # Выгружаем данные в БД
    src_post_db = dbpost(cursor, cnx, table_name, userrep, close = True)
    
    
        

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

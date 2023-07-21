Architecture in structure
root
__init__.py
DC_settings.py
main.py  
database.db    
PROCESSOR
    'PROCESSOR/_main.py'
    'PROCESSOR/_main.py/src1_api_get.py'
    'PROCESSOR/_main.py/src1_api_parse.py'
    'PROCESSOR/_main.py/src2_ops_get.py'
    'PROCESSOR/_main.py/src2_ops_parse.py'
    'PROCESSOR/_main.py/src3_drvs_get.py'
    'PROCESSOR/_main.py/src3_drvs_parse.py'
    'PROCESSOR/_main.py/src3_drvs_validator.py'
    'PROCESSOR/_main.py/uniplates.py'
    'PROCESSOR/_main.py/user_report.py'

GUI
    'GUI/_main.py'
    'GUI/_main.py/button_field.py'
    'GUI/_main.py/screen_field.py'
    'GUI/_main.py/warning_field.py'
SRC


Architecture in description
__init__.py
    'В этом файле размещены все импорты проекта'
DC_settings.py
    'В этом находится: 
    1. Функционал работы с базой данных SQL lite. Коннект к базе, создание, удаление таблиц, выгрузка данных в БД, выгрузка данных из БД'
    2. Параметры просмотра пандовских датафреймов в консоли
main.py
    'main.py это главный модуль, который запускает 2 основных компонента программы. PROCESSOR и GUI, через контроллеры этих компонентов _main.py'  
database.db
    'Файл базы данных SQLLite, формирующийся в результате работы компонента PROCESSOR, далее используемый через пользовательский интерфейс'     
PROCESSOR'
    'PROCESSOR/_main.py'
        '_main.py управляет всеми процессами компонента PROCESSOR, связанными с извлечением данных из источников, преобразованием, валидацией и размещением в БД'
    'PROCESSOR/_main.py/src1_api_get.py'
        'Модуль коннектится с веб-ресурсом по API и получает данные в форматие json'
    'PROCESSOR/_main.py/src1_api_parse.py'
        'Модуль парсит данные из файла json в дата фрейм df_src1, возвращает df_src1 в _main.py'
    'PROCESSOR/_main.py/src2_ops_get.py'
        'Модуль открывает источник оперативной сводки DEMO_CODE_dispatch.xlsx в формате дата фрейм df_src2'
    'PROCESSOR/_main.py/src2_ops_parse.py'
        'Модуль парсит df_src2, после преобразований и трансформаций возвращает df_src2 в _main.py'
    'PROCESSOR/_main.py/src3_drvs_get.py'
        'Модуль открывает источник оперативной сводки DEMO_CODE_drivers.xlsx в формате дата фрейм df_src3'
    'PROCESSOR/_main.py/src3_drvs_parse.py'
        'Модуль парсит df_src3, после преобразований и трансформаций передает df_src3 в src3_drvs_validator.py'
    'PROCESSOR/_main.py/src3_drvs_validator.py'
        'src3_drvs_validator.py это однослойная нейронная сеть, обучаемая автоматически через датасет, прогоняет колонки данных из df_src3 forwardprop и backprop, определенные как "гос.номера", отфильтровывая данные, не прошедшие по параметрам как True. Возвращает очищенный df_src3 в _main.py'
    'PROCESSOR/_main.py/uniplates.py'
        'uniplates.py принимает df_src1, df_src2, df_src3 из _main.py, где преобразовывает колонки номеров из этих датафреймов в сопоставимый вид, далее отправляет эти дата фреймы в user_report.py'
    'PROCESSOR/_main.py/user_report.py'
        'user_report.py принимает df_src1, df_src2, df_src3 с преобразованными данными, сопоставляет и консолидирует общий отчет в виде дата фрейма df_report, с последующим размещением в database.db через вспомогательный модуль DC_settings.py'
'Running the GUI Module'
    'GUI/_main.py'
        'Главный модуль управления компонентом GUI, собирает общий интерфейс'
    'GUI/_main.py/button_field.py'
        'Модуль создает поле кнопок, возвращает в _main.py'
    'GUI/_main.py/screen_field.py'
        'Модуль поле главного презентационного экрана, возвращает в _main.py'
    'GUI/_main.py/warning_field.py'
        'Модуль поле дополнительного экрана для оповещений, возвращает в _main.py'
SRC
    'Папка содержит источники "файл json, DEMO_CODE_dispatch, DEMO_CODE_drivers'
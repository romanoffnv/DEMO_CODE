<b>Architecture in structure</b><br>
root<br>
__init__.py<br>
DC_settings.py<br>
main.py<br>
database.db<br><br>
PROCESSOR<br>
    'PROCESSOR/_main.py'<br>
    'PROCESSOR/_main.py/src1_api_get.py'<br>
    'PROCESSOR/_main.py/src1_api_parse.py'<br>
    'PROCESSOR/_main.py/src_xlsx_get'<br>
    'PROCESSOR/_main.py/src2_ops_parse.py'<br>
    'PROCESSOR/_main.py/src3_drvs_parse.py'<br>
    'PROCESSOR/_main.py/src3_drvs_validator.py'<br>
    'PROCESSOR/_main.py/plates_parser.py'<br>
    'PROCESSOR/_main.py/uniplates.py'<br>
    'PROCESSOR/_main.py/user_report.py'<br><br>

GUI<br>
    'GUI/_main.py'<br>
    'GUI/_main.py/button_field.py'<br>
    'GUI/_main.py/screen_field.py'<br>
    'GUI/_main.py/warning_field.py'<br><br>
SRC<br><br>


<b>Architecture in description</b><br>
__init__.py<br>
    ```'В этом файле размещены все импорты проекта'```<br>
DC_settings.py<br>
    ```В этом модуле находится:``` <br>
    ```1. Функционал работы с базой данных SQL lite. Коннект к базе, создание, удаление таблиц, выгрузка данных в БД, выгрузка данных из БД'```<br>
    ```2. Параметры просмотра пандовских датафреймов в консоли ```<br>
main.py<br>
    ```'main.py это главный модуль, который запускает 2 основных компонента программы. PROCESSOR и GUI, через контроллеры этих компонентов _main.py'```<br>
database.db<br>
    ```'Файл базы данных SQLLite, формирующийся в результате работы компонента PROCESSOR, далее используемый через пользовательский интерфейс'```<br>
PROCESSOR'<br>
    ---> 'PROCESSOR/_main.py'<br>
        ```'_main.py управляет всеми процессами компонента PROCESSOR, связанными с извлечением данных из источников, преобразованием, валидацией и размещением в БД'```<br>
    ---> 'PROCESSOR/_main.py/src1_api_get.py'<br>
        ```'Модуль коннектится с веб-ресурсом по API и получает данные в форматие json, файл не сохраняется на локальной машине, а процессится в ходе рантайма'```<br>
    ---> 'PROCESSOR/_main.py/src1_api_parse.py'<br>
        ```'Модуль парсит данные из файла json в дата фрейм df_src1, возвращает df_src1 в _main.py'```<br>
    ---> 'PROCESSOR/_main.py/src_xlsx_get.py'<br>
        ```'Модуль открывает источники в формате xlsx и возвращает их в виде датафреймов'```<br>
    ---> 'PROCESSOR/_main.py/src2_ops_parse.py'<br>
        ```'Модуль парсит df_src2, после преобразований и трансформаций возвращает df_src2 в _main.py'```<br>
    ---> 'PROCESSOR/_main.py/src3_drvs_parse.py'<br>
        ```'Модуль парсит df_src3, после преобразований и трансформаций передает df_src3 в src3_drvs_validator.py'```<br>
    ---> 'PROCESSOR/_main.py/src3_drvs_validator.py'<br>
        ```'src3_drvs_validator.py это однослойная нейронная сеть, прогоняет колонки данных из df_src3 в циклах обучения forwardprop и backprop, определенные как "гос.номера", отфильтровывая данные, не прошедшие по параметрам как True. Возвращает очищенный df_src3 в _main.py'```<br>
    ---> 'PROCESSOR/_main.py/plates_parser.py'<br>
        ```'plates_parser.py общий модуль для компонента PROCESSOR, который парсит номера автомобилей из разных источников при помощи универсального регулярного выражения'```<br>    
    ---> 'PROCESSOR/_main.py/uniplates.py'<br>
        ```'uniplates.py принимает df_src1, df_src2, df_src3 из _main.py, где преобразовывает колонки номеров из этих датафреймов в сопоставимый вид, далее отправляет эти дата фреймы в user_report.py'```<br>
    ---> 'PROCESSOR/_main.py/user_report.py'<br>
        ```'user_report.py принимает df_src1, df_src2, df_src3 с преобразованными данными, сопоставляет и консолидирует общий отчет в виде дата фрейма df_report, с последующим размещением в database.db через вспомогательный модуль DC_settings.py'```<br>
GUI<br>
    ---> 'GUI/_main.py'<br>
        ```'Главный модуль управления компонентом GUI, собирает общий интерфейс'```<br>
    ---> 'GUI/_main.py/button_field.py'<br>
        ```'Модуль создает поле кнопок, возвращает в _main.py'```<br>
    ---> 'GUI/_main.py/screen_field.py'<br>
        ```'Модуль поле главного презентационного экрана, возвращает в _main.py'```<br>
    ---> 'GUI/_main.py/warning_field.py'<br>
        ```'Модуль поле дополнительного экрана для оповещений, возвращает в _main.py'```<br><br>
SRC<br>
    ```'Папка содержит источники "DEMO_CODE_dispatch, DEMO_CODE_drivers. Источники больших размеров отслеживаются системой LFS, их размер изменяется автономно, вне зависимости от коммитов и прогрессивно не увеличивает размер репозитория'```<br>

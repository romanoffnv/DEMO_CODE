## Описание

Эта программа разработана в целях презентации и представляет собой информационную панель с графическим интерфейсом. Управление информационной панелью осуществляется пользователем. Программа производит анализ данных, полученных из трех источников, и визуализирует определенные метрики.

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">

  <div style="flex: 0 0 calc(50% - 10px); margin-right: 10px;">
    <img src="https://github.com/romanoffnv/DC_JSON/blob/main/GUI_1.png?raw=true" alt="Скрин GUI_1" width="50%">
  </div>

  <div style="flex: 0 0 calc(50% - 10px); margin-right: 10px;">
    <img src="https://github.com/romanoffnv/DC_JSON/blob/main/GUI_2.png?raw=true" alt="Скрин GUI_2" width="50%">
  </div>

</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">

  <div style="flex: 0 0 calc(50% - 10px); margin-right: 10px;">
    <img src="https://github.com/romanoffnv/DC_JSON/blob/main/GUI_3.png?raw=true" alt="Скрин GUI_3" width="50%">
  </div>

  <div style="flex: 0 0 calc(50% - 10px); margin-right: 10px;">
    <img src="https://github.com/romanoffnv/DC_JSON/blob/main/GUI_4.png?raw=true" alt="Скрин GUI_4" width="50%">
  </div>

</div>

<div style="display: flex; flex-wrap: wrap; justify-content: space-between;">

  <div style="flex: 0 0 calc(50% - 10px); margin-right: 10px;">
    <img src="https://github.com/romanoffnv/DC_JSON/blob/main/GUI_5.png?raw=true" alt="Скрин GUI_5" width="50%">
  </div>

  <div style="flex: 0 0 calc(50% - 10px); margin-right: 10px;">
    <img src="https://github.com/romanoffnv/DC_JSON/blob/main/GUI_6.png?raw=true" alt="Скрин GUI_6" width="50%">
  </div>

</div>




## Архитектура

ROOT<br>
|-[init](#init)<br>
|- [DC_settings.py](#dc_settingspy)<br>
|- [main.py](#mainpy) <br>
|- [.gitattributes](#gitattributes) <br>

NOTEBOOKS<br>
|--- [validator.ipynb](#notebooks)<br>
|--- [charts.ipynb](#notebooks)<br>

PROCESSOR<br>
|--- [_main.py](#mainpy) <br>
|--- [plates_parser.py](#plates_parserpy) <br>
|--- [sql_requests.py](#sql_requestspy) <br>
|--- [src_xlsx_get](#src_xlsx_getpy) <br>
|--- [src1_api_get.py](#src1_api_getpy) <br>
|--- [src1_api_parse.py](#src1_api_parsepy) <br>
|--- [src2_ops_parse.py](#src2_ops_parsepy) <br>
|--- [src3_drvs_parse.py](#src3_drvs_parsepy) <br>
|--- [src3_drvs_validator.py](#src3_drvs_validatorpy) <br>
|--- [uniplates.py](#uniplatespy) <br>
|--- [user_report.py](#user_reportpy) <br>

GUI<br> 
|--- [GUI/_main.py](#_mainpy-1)<br>
|--- [button_field.py](#button_fieldpy)<br>
|--- [screen_field.py](#screen_fieldpy)<br>
|--- [display_functions.py](#display_functionspy) <br>

SRC<br> 
|--- [DEMO_CODE_dispatch.xlsx](#src)<br>
|--- [DEMO_CODE_drivers.xlsx](#src)<br>
|--- [database.db](#src)<br>

## Описание компонентов и модулей

### ROOT

#### [init](#)

Это общий модуль для всего проекта, в котором размещены все импорты используемых библиотек

#### [DC_settings.py](#)

В этом модуле находятся: <br>

1. Функционал работы с базой данных SQL lite. Коннект к базе, создание, удаление таблиц, выгрузка данных в БД, выгрузка данных из БД <br>
2. Параметры просмотра пандовских датафреймов в консоли <br>
3. Некоторые часто используемые функции при работе с датафреймами <br>

#### [main.py](#)

main.py это главный модуль, который запускает 2 основных компонента программы. PROCESSOR и GUI, через контроллеры этих компонентов _main.py

#### [.gitattributes](#)

В этом файле системы LFS прописаны файлы больших размеров, которые не выкладываются в github.com с каждым коммитом, а находятся в выделенном месте на сервере, что позволяет экономить место.

### NOTEBOOKS
В этой папке находятся файлы Jupyter Notebook, предназначенные для модулей, которые требуют графического представления данных. Файлы носят вспомогательный характер и непосредственно в [архитектуре](#) не задействованы

### PROCESSOR
Компонент процессор управляет извлечением данных из источников, с последующим их преобразованием и выгрузкой в базу данных
#### [_main.py](#)

_main.py управляет всеми процессами компонента PROCESSOR, связанными с извлечением данных из источников, преобразованием, валидацией и размещением в БД

#### [plates_parser.py](#)

Общий модуль для компонента PROCESSOR, принимает список данных, далее извлекает номерные знаки автомобилей при помощи универсального регулярного выражения.
#### [sql_requests.py](#)

В этом модуле находится функция формирования SQL запросов
#### [src_xlsx_get.py](#)

Модуль принимает название источника в формате xlsx, присвоенное переменной fname в файле _main.py. Функция принимает путь до папки SRC и название источника, далее перебирает все файлы в папке SRC, если находит требуемый файл, открывает его и возвращает в формате датафрейма.

#### [src1_api_get.py](#)

Модуль подключается к веб-ресурсу <i>github.com</i> через API и извлекает данные в формате JSON. Файл не сохраняется на локальной машине, а обрабатывается непосредственно в процессе выполнения программы, в режиме реального времени.

#### [src1_api_parse.py](#)

Модуль принимает данные, полученные в <b>src1_api_get.py</b>, распределяет их по соответствующим спискам. Из сформированных списков создает датафрейм и возвращает его в _main.py

#### [src2_ops_parse.py](#)

Модуль принимает данные, полученные в <b>src_xlsx_get.py</b>, в виде датафрейма. Так как источник является оперативной сводкой, предназначенной больше для визуального представления данных, чем для проведения аналитики, функционал модуля проводит ряд трансформаций по приведению данных в матричный вид. <br>

![Скрин диспетчерской сводки](https://github.com/romanoffnv/DC_JSON/blob/main/Dispatch%202023-08-17%20082034.png?raw=true)

#### [src3_drvs_parse.py](#)

Модуль принимает данные, полученные в <b>src_xlsx_get.py</b>, в виде датафрейма. Источник является выгрузкой из системы 1С, проходит ряд преобразований по приведению данных в матричный вид.

![Скрин выгрузки из 1С](https://github.com/romanoffnv/DC_JSON/blob/main/Drivers%202023-08-17%20082305.png?raw=true)

#### [src3_drvs_validator.py](#)

Модуль проводит валидацию гос.номеров автомобилей при помощи простейшей нейронной сети, обучаемой распределением весов и коэфициентов смещений вручную, извлеченных через общий модуль plates_parser.py. Валидация требуется так, как извлечение номерных знаков при помощи регулярного выражения в данном источнике не дает однозначных результатов, по причине присутствия в строках других данных, по структуре подходящих для отбора регулярным выражением. Более подробное описание кода и выводы в консоль можно посмотреть в [validator.ipynb](NOTEBOOKS/validator.ipynb)

#### [uniplates.py](#)

Модуль принимает 3 преобразованных датафрейма из _main.py и приводит колонки гос.номеров в унифицированный вид для последующего сопоставления 3х датафреймов и отбора нужных колонок данных, с целью формирования общего отчета.

#### [user_report.py](#)

Модуль принимает 3 преобразованных датафрейма, проводит сопоставление по гос.номерам и формирует консолидированную таблицу данных, которая возвращается обратно в _main.py, где выгружается в БД SQLite

### GUI
Компонент обеспечивает графическое отображение панели управления пользователя и данных
#### [_main.py](#)

Главный модуль управления компонентом GUI, собирает общий интерфейс

#### [button_field.py](#)

Модуль создает поле кнопок, возвращает в _main.py

#### [screen_field.py](#)

Модуль поле главного презентационного экрана, возвращает в _main.py
#### [display_functions.py](#)

В этом модуле находится группа функций, определяющих параметры отображения разных типов данных, а также фукнция, создающая разные типы диаграмм

### SRC

Папка содержит источники DEMO_CODE_dispatch, DEMO_CODE_drivers и файл базы данных data.db. Источники больших размеров отслеживаются системой LFS, их размер изменяется автономно, вне зависимости от коммитов и прогрессивно не увеличивает размер репозитория

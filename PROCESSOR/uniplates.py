from __init__ import *
from DC_settings import *

def main(src1_parse, src2_parse, src3_validator):
    # Принимаем датафреймы для преобразования данных в колонках 'Plates' к общему виду
    # Функция преобразователь
    def uniplate(df):
        # Принимаем датафрейм
        # Итерируем по рядам входящего датафрейма
        for index, row in df.iterrows():
            # Преобразуем к типу данных "строка"
            combined = ''.join(row['Plates'])
            # Убираем пробелы
            no_spaces = re.sub('\s', '', combined)
            # Приводим буквенные значения к нижнему регистру
            lowercase = no_spaces.lower()
            # Обновляем входящий датафрейм 
            df.at[index, 'Plates'] = lowercase
        return df
       
    # Отправляем датафреймы в функцию преобразователь 
    src1_parse = uniplate(src1_parse)
    src2_parse = uniplate(src2_parse)
    src3_validator = uniplate(src3_validator)
    
    # Возвращаем преобразованные датафреймы в _main.py
    return src1_parse, src2_parse, src3_validator 
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

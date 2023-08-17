from __init__ import *
from DC_settings import *

def main(src3_parse):
    # Присваиваем входящий датафрейм новой переменной
    df = src3_parse
    
    # Разбиваем колонку, состоящую из листов парных значений на 2 колонки, и загоняем их в датафрейм
    L_plates = df['Plates'].tolist()
    col_1, col_2 = [], []
    
    # Итерируемся по списку парных значений и заполняем новые колонки
    for i in L_plates:
        if len(i) > 1:
            col_1.append(i[0])
            col_2.append(i[1])
        else:
            col_1.append(i[0])
            col_2.append(np.nan)
    
    # Удаляем пробелы из значений col_2 с помощью регулярных выражений
    col_2 = [re.sub('\s*', '', str(x)) for x in col_2]
    df_plates = pd.DataFrame(zip(col_1, col_2), columns = ['col_1', 'col_2'])
    
    # Определение функции нейросети
    def neural_network(plate):
        # Определяем список допустимых буквенных значений
        legal_letters = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х', 'а', 'в', 'е', 'к', 'м', 'н', 'о', 'р', 'с', 'т', 'у', 'х']

        # Определяем архитектуру нейросети
        input_dim = 4
        hidden_dim = 4
        output_dim = 1

        # Назначаем веса и коэфициенты смещения для первого скрытого слоя вручную
        weights1 = np.array([[1, 0.6, 0.7, 0.8],
                            [0.2, 0.3, 0.4, 0.5],
                            [0.3, 0.4, 0.5, 0.6],
                            [0.4, 0.5, 0.6, 0.7]])

        bias1 = np.array([-0.4, -0.3, -0.6, -0.5])

        # Определяем функцию активации нейронов в виде сигмоидной функции
        def sigmoid(x):
            return 1 / (1 + np.exp(-x))

        # Определям параметры для цикла обучения
        learning_rate = 0.1
        epochs = 1000

        # Определям функцию валидации гос.номеров при помощи нейросети
        def is_valid_plate(plate):
            # Лист для векторизации свойств гос.номеров
            input_data = []

            # Длина гос.номера
            input_data.append(1 if len(plate) == 9 and ' ' not in plate else 0)

            # Наличие 3 букв в строке
            input_data.append(2 if len([c for c in plate if c.isalpha()]) == 3 else 0)

            # Наличие 6 цифр в строке
            input_data.append(3 if len([c for c in plate if c.isdigit()]) == 6 else 0)

            # Буквы входят в список допустимых буквенных значений
            input_data.append(4 if all(c in legal_letters for c in plate if c.isalpha()) else 0)

            # Прямое распространение
            hidden_layer1 = np.dot(input_data, weights1) + bias1
            hidden_output1 = sigmoid(hidden_layer1)
            output_layer = np.dot(hidden_output1, weights1) + bias1
            output = sigmoid(output_layer)

            # Порог валидности
            return output >= 0.8
        
        # Выполняем валидацию номерных знаков с использованием нейросети
        is_valid = is_valid_plate(plate)
        return is_valid
    
    # Определяем списки для хранения результатов валидации
    valid_1, valid_2 = [], []
    
    # Итерируемся по датафрейму и выполняем валидацию с использованием нейросети
    for index, (i, j) in enumerate(zip(df_plates['col_1'], df_plates['col_2'])):
        is_valid_1 = neural_network(i)
        valid_1.append(is_valid_1)
        is_valid_2 = neural_network(j)
        valid_2.append(is_valid_2)
    
    # Создаем датафрейм с результатами валидации       
    df_verif = pd.DataFrame(zip(col_1, valid_1, col_2, valid_2), columns = ['Plates_1', 'Verif_1', 'Plates_2', 'Verif_2'])
    
    # Обновлям датафрейм нулевыми значениями если гос.номер не прошел проверку на валидность
    for index, (p1, v1, p2, v2) in df_verif[['Plates_1', 'Verif_1', 'Plates_2', 'Verif_2']].iterrows():
        if np.any(v1 == False):
           df_verif.at[index, 'Plates_1'] = np.nan
        elif np.any(v2 == False):
            df_verif.at[index, 'Plates_2'] = np.nan
    
    # Создаем базовый датафрейм с действительными гос.номерами
    df_base = df_verif.loc[:, ['Plates_1', 'Plates_2']]
    
    # Сливаем 2 колонки по принципу "Валидный гос.номер остается, нулевое значение уходит"
    for index, (p1, p2) in df_base[['Plates_1', 'Plates_2']].iterrows():
        if not pd.isna(p2):
            df_base.at[index, 'Plates_1'] = p2
            df_base.at[index, 'Plates_2'] = np.nan

    # Обновляем исходный датафрейм
    L_plates = df_base['Plates_1'].tolist()
    df['Plates'] = L_plates
    
    # Возвращаем датафрейм в _main.py
    return df
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

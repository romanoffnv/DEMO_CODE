import re
import time

def main(L_plates):
    """Это общий модуль, принимающий колонку с гос.номерами в виде списка. Цель модуля - парсинг номеров,
    с использованием универсального регулярного выражения."""
    
    L = []
    pattern = r'([А-я])\s*(\d{3})\s*([А-я]{2})\s*(\d+\S+)'
    for i in L_plates:
        result = re.finditer(pattern, str(i))
        L.append([i[0] for i in result])
    return L

    
if __name__ == '__main__':
    main()
    start_time = time.time()
    print(f'--- %s seconds --- % {(time.time() - start_time)}')
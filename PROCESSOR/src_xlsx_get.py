from __init__ import *
from DC_settings import *

def main(parent_dir, fname):
    # Октрываем источник с названием, присвоенным переменной fname в df
    # Дополняем ссылку от корневой папки проекта к папке с источниками
    SRC_DIR = parent_dir + '\SRC'
    
    # Функция переберет все файлы в папке с источниками и вернет открытый источник в виде df 
    # если в его названии будет название, присвоенное переменной fname
    def src_xlsx_get(fname):
        for filename in os.listdir(SRC_DIR):
            f = os.path.join(SRC_DIR, filename)
            if os.path.isfile(f):
                if re.findall(re.escape(fname), f):
                    fname = f
                
        return pd.read_excel(fname) 
    return src_xlsx_get(fname)
    



if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

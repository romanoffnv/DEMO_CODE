# Global imports (for independent module run)
import os
import sys

from __init__ import *
from DC_settings import *

def main(parent_dir):
    # Октрываем источник DEMO_CODE_dispatch.xlsx в df
    # Дополняем ссылку от родительской к папке с источниками
    SRC_DIR = parent_dir + '\SRC'
    
    # Функция преберет все файлы в папке с источниками и вернет открытый источник в виде df если в его названии будет dispatch
    def open_src2():
        for filename in os.listdir(SRC_DIR):
            f = os.path.join(SRC_DIR, filename)
            if os.path.isfile(f):
                if re.findall(f'dispatch', f):
                    dispatch = f
                
        return pd.read_excel(dispatch) 
    return open_src2()
    



if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

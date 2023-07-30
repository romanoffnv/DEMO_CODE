# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

def main():
    SRC_DIR = parent_dir + '\SRC'
    pprint(SRC_DIR)
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

# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

def main(src1_get):
    pprint('PROCESSOR/_main.py/src1_api_parse.py')
    pprint(src1_get)

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

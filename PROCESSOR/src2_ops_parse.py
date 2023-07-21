# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

def main():
    pprint('PROCESSOR/_main.py/src2_ops_parse.py')

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

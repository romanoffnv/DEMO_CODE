import os
import sys

# Global imports
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *
from PROCESSOR._main import main as processor


def main():
    prssor = processor() 
    pprint(prssor)
    
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
    
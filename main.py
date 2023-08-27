import os
import sys

# Глобальные переменные
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(parent_dir)


from __init__ import *
from DC_settings import *
from PROCESSOR._main import main as processor
from GUI._main import main as gui


def main():
    gui()
    # processor()
    # pprint('main.py')
    # pprint('Running the PROCESSOR Module')
    # pprint(processor())
    # pprint('Running the GUI Module')
    # pprint(gui())
    
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
    
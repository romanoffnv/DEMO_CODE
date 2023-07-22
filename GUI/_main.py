# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *
from GUI.button_field import main as button_field
from GUI.screen_field import main as screen_field
from GUI.warning_field import main as warning_field


def main():
    pprint('GUI/_main.py')
    
    btn_field = button_field()
    scrn_field = screen_field()
    wrn_field = warning_field()
    
    
    
    

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

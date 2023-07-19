# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

def main():
    global_routing = 'Gobal. PROCESSOR _main.py +++'
    local_routing = 'Local. PROCESSOR _main.py +++'
    pprint(local_routing)
    return global_routing

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

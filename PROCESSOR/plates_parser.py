# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *

def main(L_plates):
    return [''.join(re.findall('[А-я]\s*\d{3}\s*[А-я]{2}\s*\d+\S+', x)) for x in L_plates]

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
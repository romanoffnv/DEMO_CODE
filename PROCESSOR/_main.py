# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from __init__ import *
from DC_settings import *
from PROCESSOR.src1_api_get import main as src1_api_get
from PROCESSOR.src1_api_parse import main as src1_api_parse
from PROCESSOR.src2_ops_get import main as src2_ops_get
from PROCESSOR.src2_ops_parse import main as src2_ops_parse
from PROCESSOR.src3_drvs_get import main as src3_drvs_get
from PROCESSOR.src3_drvs_parse import main as src3_drvs_parse
from PROCESSOR.src3_drvs_validator import main as src3_drvs_validator
from PROCESSOR.uniplates import main as uniplates
from PROCESSOR.user_report import main as user_report

def main():
    pprint('PROCESSOR/_main.py')
    src1_get = src1_api_get()
    src1_parse = src1_api_parse(src1_get)
    src2_get = src2_ops_get()
    src2_parse = src2_ops_parse(src2_get)
    # src3_get = src3_drvs_get()
    # src3_parse = src3_drvs_parse()
    # src3_validator = src3_drvs_validator()
    # uniplates_generalizer = uniplates()
    # userrep = user_report()
    
    
    

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

# Global imports (for independent module run)
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
fname ='dispatch'

from __init__ import *
from DC_settings import *
from PROCESSOR.src1_api_get import main as src1_api_get
from PROCESSOR.src1_api_parse import main as src1_api_parse
from PROCESSOR.src_xlsx_get import main as src_xlsx_get
from PROCESSOR.src2_ops_parse import main as src2_ops_parse
from PROCESSOR.src3_drvs_parse import main as src3_drvs_parse
from PROCESSOR.src3_drvs_validator import main as src3_drvs_validator
from PROCESSOR.uniplates import main as uniplates
from PROCESSOR.user_report import main as user_report

def main():
    # src1_get = src1_api_get()
    # src1_parse = src1_api_parse(src1_get)
    src2_get = src_xlsx_get(parent_dir, fname = 'dispatch')
    src2_parse = src2_ops_parse(src2_get)
    src3_get = src_xlsx_get(parent_dir, fname = 'drivers')
    src3_parse = src3_drvs_parse(src3_get)
    # pprint(src1_parse)
    # pprint(src2_parse)
    # pprint(src3_parse)
    src3_validator = src3_drvs_validator(src3_parse)
    # uniplates_generalizer = uniplates()
    # userrep = user_report()
    
        

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

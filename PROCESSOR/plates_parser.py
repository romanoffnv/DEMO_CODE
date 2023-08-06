# Global imports (for independent module run)
import os
import sys

from __init__ import *
from DC_settings import *

def main(L_plates):
    
    L = []
    pattern = '([А-я])\s*(\d{3})\s*([А-я]{2})\s*(\d+\S+)'
    for i in L_plates:
        result = re.finditer(pattern, str(i))
        L.append([i[0] for i in result])
    return L

    
    # extracted_data = [re.findall(pattern, x) for x in L_plates]
    # # pprint(extracted_data)
    
    # L_plates_all = [[''.join(part) for part in plate_data] for plate_data in extracted_data]
    # L_plates_clean = [[re.sub(',', ', ', i[0]) + i[1] if len(i) > 1 else re.sub(',', '', i[0])] for i in L_plates_all]
    
    
    # return L_plates_clean
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
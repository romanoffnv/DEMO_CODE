from __init__ import *
from DC_settings import *

from PROCESSOR.plates_parser import main as plates_parser

def main(src1_get):
    L_units = [x['name'] for x in src1_get]
    L_plates = [x for x in L_units]
    L_plates = plates_parser(L_plates)
    L_status = [x['status'] for x in src1_get]
    L_locations = [tuple(x['location']) for x in src1_get]
    
    return pd.DataFrame(zip(L_units, L_plates, L_status, L_locations), columns = ['Units', 'Plates',  'Status', 'Coordinates'])
    
    
        

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

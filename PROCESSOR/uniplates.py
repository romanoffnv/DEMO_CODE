from __init__ import *
from DC_settings import *

def main(src1_parse, src2_parse, src3_validator):
    def uniplate(df):
        for index, row in df.iterrows():
            combined = ''.join(row['Plates'])
            no_spaces = re.sub('\s', '', combined)
            lowercase = no_spaces.lower()
            df.at[index, 'Plates'] = lowercase
        return df
        
    src1_parse = uniplate(src1_parse)
    src2_parse = uniplate(src2_parse)
    src3_validator = uniplate(src3_validator)
   
    return src1_parse, src2_parse, src3_validator 
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

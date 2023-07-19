import os
import sys

# Global imports
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))
sys.path.append(parent_dir)

from __init__ import *
from Settings import *
from omnicomm_api._main import main as omnicomm_api
from brm._main import main as b_fr_brm
from cits._main import main as c_ct_cits
from accountance._main import main as d_accountance
from drivers._main import main as drivers
from total_match.match_1 import main as match_1
from total_match.match_2 import main as match_2
from total_match.match_3 import main as match_3
from total_match.match_4 import main as match_4


from Plate_ripper import main as plate_ripper
from Plate_indexer import main as plate_indexer


def main():
    src_dir = parent_dir + '\_SRC'
    db = db_connect('cnx', db_name = 'data.db')
    
    
    with tqdm(total=5) as pbar:
        pbar.set_description('Fetching json')
        df_1 = omnicomm_api(parent_dir) #get omnicomm df
        pprint('Main')
        pprint('Omnicomm report')
        pprint(df_1.describe())
        pbar.update(1)
        
        pbar.set_description('Getting brm')
        df_2 = b_fr_brm(parent_dir) #get brm df
        pprint('BRM report')
        pprint(df_2.describe())
        pbar.update(1)
        
        # pbar.set_description('Matching omnicomm and brm dfs')
        # df_3 = match_1(df_1, df_2) #get matched and merged om and brm dfs
        # pbar.update(1)
        
        pbar.set_description('Getting cits')
        df_4 = c_ct_cits(parent_dir) #get cits df
        pprint('Cits report')
        pprint(df_4.describe())
        pbar.update(1)
        
        # pbar.set_description('Matching merged om_brm_cits')
        # df_5 = match_2(df_3, df_4) #get matched and merged om_brm_cits df
        # pbar.update(1)
        
        pbar.set_description('Getting accountance')
        df_6 = d_accountance(parent_dir) #get acc df
        pprint('Accountance report')
        pprint(df_6.describe())
        pbar.update(1)
        
        # pbar.set_description('Matching om_brm_cits_acc')
        # df_7 = match_3(df_5, df_6) #get matched and merged om_brm_cits_acc df
        # pbar.update(1)
        
        pbar.set_description('Getting drivers')
        df_8 = drivers(parent_dir) #get drv df
        pprint('Drivers report')
        pprint(df_8.describe())
        pbar.update(1)
        
        # pbar.set_description('Matching om_brm_cits_acc_drivers')
        # df_9 = match_4(df_7, df_8) #get matched and merged om_brm_cits_acc_drivers final df df
        # pbar.update(1)
        
        # pbar.set_description('Cleaning up')
        # # Add any clean up operations here
        # time.sleep(1)
        # pbar.update(1)
        # pbar.set_description('Done')
        # time.sleep(1)
        # pbar.update(1)
    
    # df = df_9
    
    # # Specify the Excel file name
    # excel_file = src_dir + '\DB.xlsx'
    # # Dump the DataFrame into an Excel file
    # df.to_excel(excel_file, index=False)
    
    # # Dump df into db
    # # Get the current date
    # current_date = datetime.datetime.now().strftime('%d_%m_%Y')

    
    # # Use the current date as the table name with a prefix
    # table_name = 'table_' + current_date

    # # Upload the DataFrame to the new table with the current date as the name
    # db_post(table_name, db, df, close = True)
    
    # drop table in case if one was created in experimental purposes
    # table_name = 'table_28_04_2023'
    # db_drop(table_name, db, close = True)
    
if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))
    
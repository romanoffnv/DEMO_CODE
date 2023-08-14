from __init__ import *
from DC_settings import *

def main():
    url = "https://github.com/romanoffnv/DC_JSON/raw/main/vehicles.json"
    
    def get_json_github(url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Link is accessible. Response: {response.status_code}.")
                dict_json = json.loads(response.text)
                return dict_json
            else:
                pprint(f"Error: The link returned a status code of {response.status_code}.")
        except requests.exceptions.RequestException as e:
            pprint(f"Error: Unable to access the link. {e}")
    
    dict_json = get_json_github(url)
    return dict_json

if __name__ == '__main__':
    main()
    start_time = time.time()
    pprint("--- %s seconds ---" % (time.time() - start_time))

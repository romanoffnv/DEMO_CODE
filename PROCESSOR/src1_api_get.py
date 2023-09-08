import requests
import json
import time

def main():
    url = "https://github.com/romanoffnv/DC_JSON/raw/main/vehicles.json"
    
    def get_json_github(url):
        try:
            response = requests.get(url,  timeout = 10)
            if response.status_code == 200:
                print(f"Link is accessible. Response: {response.status_code}.")
                dict_json = json.loads(response.text)
                return dict_json
            print(f"Error: The link returned a status code of {response.status_code}.")
            return 0
        except requests.exceptions.RequestException as e:
            print(f"Error: Unable to access the link. {e}")
            return 0
    
    dict_json = get_json_github(url)
    print(dict_json)
    return dict_json


if __name__ == '__main__':
    main()
    start_time = time.time()
    print(f"--- %s seconds --- % {(time.time() - start_time)}")

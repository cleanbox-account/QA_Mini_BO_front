import requests
import json
import sys
import Data.pages_addresses as env
from utilsModules.Logs_input import input_logs

    
def get_BO_token(my_phone, my_pass):
    test_dir="test"
    # input_logs("INFO", "---"+" "*10+"Get token from BO_API",test_dir)
    url = env.bo_api_url_auth
    payload = json.dumps({
        "mobilePhone": my_phone,
        "password": my_pass
    })
    headers = {
        'path': '/api/Users/authenticate',
        'accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        # input_logs("INFO", "response code = "+str(response.status_code),test_dir)
        if response.status_code == 200:
            my_token = response.json()['token']
            # input_logs("INFO", "Succeed token request ", test_dir)
            # input_logs("INFO", "token :  %s" % my_token,test_dir)
            return my_token 
        else:
            input_logs("ERROR", "Failed response code >>>"+str(response.status_code), test_dir)
            input_logs("ERROR", "Failed response text >>>"+response.text, test_dir)
            return False
    except requests.exceptions.RequestException as err:
        input_logs("ERROR", "Error: %s" % err, test_dir)
        return False

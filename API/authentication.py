from time import sleep
import requests
import json
import sys
# import Data.pages_addresses as env
import API.url_elm as env1
from API.Logs_input import input_from_API_logs as logs #,input_logs

sys.path.append("..")
url = env1.k_api_url
url1 = env1.bo_api_url_auth
st_5104_id = env1.st_5104_id
k_station_url=env1.k_station_url
oneproj_api_login=env1.oneproj_api_login

def get_tokken(mphone, password,test_dir):
    payload = json.dumps({
        "mobilePhone": mphone,
        "password": password
    })
    headers = {
        'accept': '',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        # logs("INFO", "API response code = {0}".format(response.status_code),test_dir)
        if response.status_code == 200:     
            my_token = response.json()['token']
            my_id = response.json()['id']
            my_fname = response.json()['firstName']
            my_lname = response.json()['lastName']
            my_email = response.json()['email']
            my_mobilePhone = response.json()['mobilePhone']
            my_stationNumber = response.json()['stationNumber']
            my_station_id = response.json()['stationId']
            my_role = response.json()['role']
            # logs("INFO", "token :  %s" % my_token,test_dir)
            # logs("INFO", "id :  %s" % my_id,test_dir)
            # logs("INFO", "Full name :  %s %s     role :  %s" %
            #            (my_fname, my_lname, my_role),test_dir)
            # logs("INFO", "mobile phone :  %s     email :  %s" %
            #            (my_mobilePhone, my_email),test_dir)
            # logs("INFO", "related to user station id :  %s     station number :  %s" %
            #            (my_station_id, my_stationNumber),test_dir)
            # return (my_id, my_station_id, my_token)
            user_details={
                "id":my_id,
                "mobilePhone": my_mobilePhone,
                "firstName": my_fname,
                "lastName": my_lname,
                "role": my_role,
                "token": my_token,
                # "station_id": st_5104_id,
                # "stationNumber": 5104}
                "station_id": my_station_id,
                "stationNumber": int(my_stationNumber)}
            logs("INFO", "Succeed Kiosk token creation... " ,test_dir)
            return user_details  
        else:
            logs("ERROR", "Failed response code >>> "+str(response.status_code), test_dir)
            logs("ERROR", "Failed response text >>>", test_dir)
            logs("ERROR", "{0}".format(response.text), test_dir)
            sleep(3)
            return False
    except requests.exceptions.RequestException as err:
        logs("ERROR", "Error: %s" % err,test_dir)
        sleep(3)
        return False
    finally:
        logs("---", "- - - - - - - - ",test_dir)

def get_external_mail_tokken(userName, password,test_dir):
    payload = json.dumps({
        "userName": userName,
        "password": password
    })
    headers = {
        'accept': '',
        'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", oneproj_api_login, headers=headers, data=payload)
        # logs("INFO", "API response code = {0}".format(response.status_code),test_dir)
        if response.status_code == 200:     
            my_token = response.json()['token']
            my_result = response.json()['result']
            
            logs("INFO", "Succeed api token creation... " ,test_dir)
            if my_result=="Success":
                return my_token  
            else :
                logs("ERROR", "Failed to receive token > {0} ".format(my_result), test_dir)
                return False
        else:
            logs("ERROR", "Failed response code >>> "+str(response.status_code), test_dir)
            logs("ERROR", "Failed response text >>>", test_dir)
            logs("ERROR", "{0}".format(response.text), test_dir)
            sleep(3)
            return False
    except requests.exceptions.RequestException as err:
        logs("ERROR", "Error: %s" % err,test_dir)
        sleep(3)
        return False
    finally:
        logs("---", "- - - - - - - - ",test_dir)



def get_BO_tokken(my_phone, my_pass, test_dir):
    logs("INFO", "---"+" "*10+"Get token from BO_API", test_dir)
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
        response = requests.request("POST", url1, headers=headers, data=payload)
        # logs("INFO", "response code = "+str(response.status_code), test_dir)
        if response.status_code == 200:
            my_token = response.json()['token']
            my_id = response.json()['id']
            my_fname = response.json()['firstName']
            my_lname = response.json()['lastName']
            my_email = response.json()['email']
            my_mobilePhone = response.json()['mobilePhone']
            my_stationNumber = response.json()['stationNumber']
            my_station_id = response.json()['stationId']
            my_role = response.json()['role']
            # logs("INFO", "token :  %s" % my_token,test_dir)
            logs("INFO", "Succeed BO token creation ", test_dir)
            # logs("INFO", "id :  %s" % my_id, test_dir)
            # logs("INFO", "Full name :  %s %s - role :  %s" %
            #                     (my_fname, my_lname, my_role), test_dir)
            # logs("INFO", "mobile phone :  %s - email :  %s" %
            #                     (my_mobilePhone, my_email), test_dir)
            # logs("INFO", "related to user station id :  %s - station number :  %s" %
            #                     (my_station_id, my_stationNumber), test_dir)
            
            return my_token 
        else:
            logs("ERROR", "Failed response code >>> "+str(response.status_code), test_dir)
            logs("ERROR", "Failed response text >>>", test_dir)
            logs("ERROR", "{0}".format(response.text), test_dir)
            sleep(3)
            return False
    except requests.exceptions.RequestException as err:
        logs("ERROR", "Error: %s" % err, test_dir)
        sleep(3)
        return False
    
def get_station_info(test_dir):
    headers = {
        'accept': '',
        'Content-Type': 'application/json'
    }
    try:
        response = requests.request("GET", k_station_url, headers=headers)
        logs("INFO", "API response code = {0}".format(response.status_code),test_dir)
        if response.status_code == 200:     
            env = response.json()['env']
            stationNumber = response.json()['stationNumber']
            station_id = response.json()['stationId']
            version = response.json()['version']
            # logs("INFO", "token :  %s" % my_token,test_dir)
            logs("INFO", "--- Station details : ",test_dir)
            logs("INFO", "env :  %s   version : %s" % (env,version),test_dir)
            logs("INFO", "current station id :  %s     station number :  %s" %(station_id, stationNumber),test_dir)
            # return (my_id, my_station_id, my_token)
            station_details={
                "env":env,
                "version":version,
                "station_id": station_id,
                "stationNumber": int(stationNumber)}
            return station_details 
        else:
            logs("ERROR", "Failed response code >>>"+str(response.status_code), test_dir)
            logs("ERROR", "Failed response text >>>"+response.text, test_dir)
            sleep(3)
            return False
    except requests.exceptions.RequestException as err:
        logs("ERROR", "Error: %s" % err,test_dir)
        sleep(3)
        return False
    finally:
        logs("---", "- - - - - - - - ",test_dir)
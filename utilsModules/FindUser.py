import json
import Data.pages_addresses as env

    
def get_user(usr_role):
    #file=env.json_path+env.users_path    #used json file in the project path
    file=env.json_users     #used json file out off project path > absolute file path
    
    try:
        json_in = open(file)
        users=json.load(json_in)

        my_user=next(filter(lambda user:user['role']==usr_role,users),None)
    except FileNotFoundError:
        return None
    json_in.close()
    return my_user

def get_bo_user(usr_role):
    file=env.json_bousers     #used json file out off project path > absolute file path
    
    try:
        json_in = open(file)
        users=json.load(json_in)

        my_user=next(filter(lambda user:user['role']==usr_role,users),None)
    except FileNotFoundError:
        return None
    json_in.close()
    return my_user

import json
import Data.pages_addresses as env

    
def get_user(usr_role):
    file=env.json_path+env.users_path
    
    try:
        json_in = open(file)
        users=json.load(json_in)
        # for usr in users:
        #     if usr["role"]==usr_role:
        #         my_user= usr
        #         break
        my_user=next(filter(lambda user:user['role']==usr_role,users),None)
    except FileNotFoundError:
        return None
    json_in.close()
    return my_user

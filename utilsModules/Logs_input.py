# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2022.01.30
# version ='1.0'
# ---------------------------------------------------------------------------
""" Sepparated logger for loggin out of pytest files adding row with - """
# ---------------------------------------------------------------------------
from   datetime import  datetime
import Data.pages_addresses as env

def input_logs(mess_type, message,dir):
    # print(message)
    now_date=datetime.now().strftime("%Y_%m_%d")
    filename=env.logs_path+dir+"\logfile_"+now_date+".log"
    f = open(filename, "a", encoding='utf-8')
    if mess_type=="---": 
        f.write("-"*150+"\n")
    else:
        f.write("%s : %s : %s\n"%(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3],mess_type,message))
    f.close()


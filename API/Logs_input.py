from datetime import datetime
from pathlib import Path
import API.url_elm as env


def input_logs(mess_type, message, dir):
    # print(message)
    now_date = datetime.now().strftime("%Y_%m_%d")
    filename = env.logs_path + dir+"\logfile_"+now_date+".log"

    if mess_type == "---":
        f = open(filename, "a", encoding='utf-8')
        f.write("-"*150+"\n")
        f.close()
    else:
        f = open(filename, "a", encoding='utf-8')
        f.write("%s : %s : %s\n" % (datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S.%f")[:-3], mess_type, message))
        f.close()


def input_from_API_logs(mess_type, message, dir):
    # print(message)
    now_date = datetime.now().strftime("%Y_%m_%d")
    filename2 = env.logs_path + dir+"\\api_logfile_"+now_date+".log"
    f = open(filename2, "a", encoding='utf-8')
    f.write("%s : %s : API requests : %s\n" % (datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S.%f")[:-3], mess_type, message))
    f.close()

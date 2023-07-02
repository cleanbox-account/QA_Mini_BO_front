from time import sleep
import requests

import json
import sys
from API.Logs_input import input_logs
from API.Logs_input import input_from_API_logs as logs
from datetime import datetime, timedelta
import Data.pages_addresses as env
import pytz

sys.path.append("..")
curr_order = ''
# orders_list = []



def api_active_orders(user_id, station_id, token, test_dir):
    # global orders_list
    url = env.k_api_url_station_id + station_id+"&userId="+user_id
    orders_list = []
    payload = ""
    headers = {
        'Authorization': 'Bearer '+token
    }
    sleep(3)
    
    try:    
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:  
            full_orders_list = response.json()
            input_logs("INFO", "{0}_Has {1} active orders for User {2} in {3} station ".format("api_active_orders[28]",len(full_orders_list), user_id, station_id), test_dir)
            # input_logs("----response json list-----")
            # input_logs(full_orders_list)
            if len(full_orders_list) > 0:
                i=1
                input_logs("INFO","----orders list---", test_dir)
                for elem in (response.json()):
                    input_logs("INFO","{0} {1}".format(i,elem['orderNumber']),test_dir)
                    items_list = []
                    for item in elem['orderItems']:
                        items_list.append({'id': item['id'], 'itemNumber': item['itemNumber'],
                                        'quantity': item['quantity'], 'processName': item['processName']})
                    orders_list.append({
                        'customerId': elem['customerId'],
                        'orderNumber': elem['orderNumber'],
                        'orderDate': elem['orderDate'],
                        'stationId': elem['stationId'],
                        'stationNumber': elem['stationNumber'],
                        # order type 1- laundry , 13- DHL for example
                        'orderType': elem['orderType'],
                        # 'orderState':elem["order"],
                        'orderItems': items_list,  # array of items

                    })
                    i+=1
                
                # input_logs("INFO",json.dumps(orders_list, indent=1), test_dir)
                # input_logs("INFO",orders_list, test_dir)
                # input_logs("INFO",find_last_order(orders_list))
                return orders_list
            else:
                return []
        else:
            input_logs("ERROR", "Failed response code >>> "+str(response.status_code), test_dir)
            logs("ERROR", "Failed response code >>> "+str(response.status_code), test_dir)
            input_logs("ERROR", "Failed response text >>>", test_dir)
            logs("ERROR", "Failed response text >>>", test_dir)
            input_logs("ERROR", "{0}".format(response.text), test_dir)
            logs("ERROR", "{0}".format(response.text), test_dir)
            return False
    except requests.exceptions.RequestException as err:
        input_logs("ERROR", "Error: %s" % err,test_dir)
        logs("ERROR", "Error: %s" % err,test_dir)
        return False


def find_last_order(orders_list, test_dir):
    # global orders_list  timestamp ex. '2022-02-15T12:20:14.149660'
    last_order = 'NO ORDERS'
    my_datatime = datetime.now()-timedelta(seconds=60)
    my_time = my_datatime.strftime("%Y-%m-%d %H:%M:%S")
    if is_dst(my_datatime):
        tdelta=3
    else:
        tdelta=2
    input_logs("INFO", "from now -60 sec :"+my_time, test_dir)
    for order_elm in orders_list:
        o_type = order_elm['orderType']
        timestr = order_elm['orderDate']
        o_number = order_elm['orderNumber']
        order_time = datetime.strptime(
                (timestr[: 19]).strip(), '%Y-%m-%dT%H:%M:%S')+timedelta(hours=tdelta)
        if o_type == 1:  # laundry type
            #input_logs("TIME ISO >",s)
            # order_time = datetime.strptime(
            #     (timestr[: 19]).strip(), '%Y-%m-%dT%H:%M:%S')+timedelta(hours=tdelta)
            input_logs("INFO","find_last_order[80] : Laundry - order number > " + str(o_number) +"   order time > " + str(order_time), test_dir)
            if (my_datatime < order_time):  # find order done in last 60 seconds
                last_order = order_elm
                
        elif o_type in (13, 14, 15, 2):  # parcels type
            # order_time = datetime.strptime(
            #     (timestr[: 19]).strip(), '%Y-%m-%dT%H:%M:%S')+timedelta(hours=tdelta)

            input_logs("INFO", "find_last_order[88] : Parcels - order number > " + str(o_number)+ "   order time > " + str(order_time), test_dir)
            if (my_datatime < order_time):  # find order done in last 60 seconds
                last_order = order_elm
                
        elif o_type ==5:  # Shipment type
            # order_time = datetime.strptime(
            #     (timestr[: 19]).strip(), '%Y-%m-%dT%H:%M:%S')+timedelta(hours=tdelta)

            input_logs("INFO", "find_last_order[96] : Shipment - order number > " + str(o_number)+ "   order time > " + str(order_time), test_dir)
            if (my_datatime < order_time):  # find order done in last 60 seconds
                last_order = order_elm
                
        elif o_type ==4:  # Locker rental type
            # order_time = datetime.strptime(
            #     (timestr[: 19]).strip(), '%Y-%m-%dT%H:%M:%S')+timedelta(hours=tdelta)

            input_logs("INFO", "find_last_order[104] : Locker rental - order number > " + str(o_number)+ "   order time > " + str(order_time), test_dir)
            if (my_datatime < order_time):  # find order done in last 60 seconds
                last_order = order_elm
                
        elif o_type ==16:  # Decathlon type
            # order_time = datetime.strptime(
            #     (timestr[: 19]).strip(), '%Y-%m-%dT%H:%M:%S')+timedelta(hours=tdelta)

            input_logs("INFO", "find_last_order[112] : Decathlon - order number > " + str(o_number)+ "   order time > " + str(order_time), test_dir)
            if (my_datatime < order_time):  # find order done in last 60 seconds
                last_order = order_elm
                
    if not last_order == 'NO ORDERS':
        # print("INFO ----LAST ORDER----")
        # input_logs("INFO",last_order)
        return last_order
    else:
        return False
    
def is_dst(dt,timeZone=pytz.timezone("Asia/Jerusalem")):   #return True or False if has DST daylight time
    aware_dt = timeZone.localize(dt)
    return aware_dt.dst() != timedelta(0,0)
    
def push_order_in_temp(order, test_dir):
    orders=pull_order_from_temp(test_dir)
    if orders==None :
        orders=[]   
    orders.append(order)
    file=env.json_path+test_dir+"\\temp\\temp.json"
    json_out=open(file,"w")
    json.dump(orders,json_out,indent=4)
    input_logs("INFO", "push_order_in_temp[135] : Push the order of parcel in temp file....", test_dir)
    input_logs("INFO", json.dumps(orders, indent=1), test_dir)
    input_logs("INFO", orders, test_dir)
    json_out.close()
    
def pull_order_from_temp( test_dir):
    file=env.json_path+test_dir+"\\temp\\temp.json"
    try:
        json_in = open(file)
        orders=json.load(json_in)
    except FileNotFoundError:
        return None
    input_logs("INFO", "pull_order_from_temp[147] : Pull out orders of parcels from temp file....", test_dir)
    input_logs("INFO", json.dumps(orders, indent=1), test_dir)
    # input_logs("INFO", orders, test_dir)
    json_in.close()
    return orders

def pop_order_from_temp(order_key_to_pop, test_dir): # pop one order from orders array
    file=env.json_path+test_dir+"\\temp\\temp.json"   
    try:
        json_in = open(file)
        orders=json.load(json_in)
    except FileNotFoundError:
        return None
    # input_logs("INFO", "Pop '{0}' order of parcel from temp file....".format(order_key_to_pop), test_dir)
    # input_logs("INFO", json.dumps(orders, indent=1), test_dir)
    # input_logs("INFO", orders, test_dir)
    json_in.close() # close after load json
    order_pop=None
    for order in orders:
        if order_key_to_pop == order["order_number"] :
            index= orders.index(order) #return index of obj
            order_pop = orders.pop(index) # pop from array the obj with index
            # input_logs("INFO","Order of parcel to pop out is : '{}'".format(json.dumps(order_pop, indent=1)),test_dir)
            # input_logs("INFO","Order to pop out is : '{}'".format(order_pop),test_dir)
            break
    # input_logs("INFO", "After pop parcel: ", test_dir) 
    # input_logs("INFO", json.dumps(orders, indent=1), test_dir)
    # input_logs("INFO", orders, test_dir)
    json_out=open(file,"w") # open for rewrite json
    json.dump(orders,json_out,indent=4)
    json_out.close()
    return order_pop

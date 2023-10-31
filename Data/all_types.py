def switch_account_type_name(account_type):
    if account_type =="Unknown" :
        return 'NA'
    elif account_type =="Done" :
        return 'Done'
    elif account_type =="DHL" :
        return 'DHL'
    elif account_type =="Bar" :
        return 'Bar'
    elif account_type =="UPS" :
        return 'UPS'
    elif account_type =="Decathlon" :
        return 'DEC'
    elif account_type =="Marmelada" :
        return 'MRM'
    elif account_type =="YadMordechai" :
        return 'YAD'
    elif account_type =="MarmeladaMarket" :
        return 'MRKT'
    elif account_type =="Exelot" :
        return 'EXL'
    elif account_type =="GeffenMedical" :
        return 'GFN'
    elif account_type =="SdeMoshe" :
        return 'SDM'
    elif account_type =="NegroCoffee" :
        return 'NGC'
    elif account_type =="Amirim" :
        return 'AMR'
    elif account_type =="CheapSim" :
        return 'CHS'
    elif account_type =="AquaBell" :
        return 'AQB'
    elif account_type =="OneProject" :
        return 'OPR'
    elif account_type =="ZigZag" :
        return 'ZGZ'
    elif account_type =="HFD" :
        return 'HFD'
    elif account_type =="ClothApp" :
        return 'CLA'
    elif account_type =="LittleOneSleep" :
        return 'LOS'
    elif account_type =="YDM" :
        return 'YDM'
    elif account_type =="GameStorm" :
        return 'GMS'
    elif account_type =="TAU" :
        return 'TAU'
    elif account_type =="MotorShop" :
        return 'MTS'
    elif account_type =="BerorHayil" :
        return 'BRH'
    elif account_type =="CDEK" :
        return 'CDK'
    elif account_type =="Velo" :
        return 'VEL'
    elif account_type =="Benda" :
        return 'BND'
    elif account_type =="Azrieli" :
        return 'AZR'
    else:
        return 'NA'
    
def find_username_by_account_type(account_type):
    if account_type =="NegroCoffee" :
        return "negroUser"
    elif account_type =="CheapSim" :
        return "cheapSimUser"
    elif account_type =="MotorShop" :
        return "motorShop"
    else:
        return 'NA'
    
def switch_Orders_Type_to_Short(order_type):
    if order_type == 0:
        return 'NA'
    elif order_type == 1:
        return 'Laundry'
    elif order_type == 2:
        return 'Mail'
    elif order_type == 3:
        return 'Product'
    elif order_type == 4:
        return 'LockerRent'
    # parcel types:
    elif order_type == 5:
        return 'Shipment'    
    elif order_type == 6:
        return 'RDHL'#Returns 
    elif order_type == 7:
        return 'REXL' #Exelot returns
    elif order_type == 8:
        return 'MEX' #MailExternal
   
    elif order_type == 12:
        return 'EXL' #Exelot
    elif order_type == 13:
        return 'DHL'
    elif order_type == 14:
        return 'Bar'
    elif order_type == 15:
        return 'UPS'
    elif order_type == 16:
        return 'DEC' # Decathlon'
    elif order_type == 17:
        return 'YAD' #'YadMordechai' 
    elif order_type == 18:
        return 'GFN' #'GeffenMedical' 
    elif order_type == 19:
        return 'SDM' #'SdeMoshe' 
    elif order_type == 20:
        return 'AMR' #'Amirim' 
    elif order_type == 21:
        return 'OPR' #'OnePrj' 
    elif order_type == 22:
        return 'ZGZ' #'ZigZag' 
    elif order_type == 23:
        return 'HFD' #HFD
    elif order_type == 24:
        return 'RHFD' #DeliveryReturnsHFD
    elif order_type == 25:
        return 'YDM' #YDM
    elif order_type == 26:
        return 'RYDM' #DeliveryReturnsYDM
    elif order_type == 27:
        return 'TAU' #TAU
    elif order_type == 28:
        return 'VEL' #Velo
    elif order_type == 29:
        return 'CDK' #return CDEK
    elif order_type == 30:
        return 'BRH' #BerorHayil
    elif order_type == 31:
        return 'RTRN' #ReturnsExternal


    
def switch_Orders_Type_to_string(order_type):
    if order_type == 0:
        return 'NA'
    elif order_type == 1:
        return 'Laundry'
    elif order_type == 2:
        return 'Mail'
    elif order_type == 3:
        return 'Product'
    elif order_type == 4:
        return 'LockerRent'
    # parcel types:
    elif order_type == 5:
        return 'Shipment'    
    elif order_type == 6:
        return 'Returns'    
    elif order_type ==7:
        return 'Exelot returns'    
    elif order_type ==8:
        return 'MailExternal'    

    elif order_type == 12:
        return 'Exelot'
    elif order_type == 13:
        return 'DHL'
    elif order_type == 14:
        return 'Bar'
    elif order_type == 15:
        return 'UPS'
    elif order_type == 16:
        return 'Decathlon'
    elif order_type == 17:
        return 'YadMordechai' 
    elif order_type == 18:
        return 'GeffenMedical' 
    elif order_type == 19:
        return 'SdeMoshe' 
    elif order_type == 20:
        return 'Amirim' 
    elif order_type == 21:
        return 'OneProject' 
    elif order_type == 22:
        return 'ZigZag' 
    elif order_type == 23:
        return 'HFD' 
    elif order_type == 24:
        return 'DeliveryReturnsHFD' 
    elif order_type == 25:
        return 'YDM' 
    elif order_type == 26:
        return 'DeliveryReturnsYDM' 
    elif order_type == 27:
        return 'TAU' 
    elif order_type == 28:
        return 'Velo' 
    elif order_type == 29:
        return 'CDEK' 
    elif order_type == 30:
        return 'BerorHayil' 
    elif order_type == 31:
        return 'ReturnsExternal' 
    

def switch_Orders_Status_Name(order_state):
    if order_state == 0:
        return 'WaitingForPickup'
    elif order_state == 1:
        return 'DirtyPickedByDriver'
    elif order_state == 2:
        return 'Pending'
    elif order_state == 3:
        return 'CleanPickedUpByDriver'
    elif order_state == 4:
        return 'ReadyInLocker'
    elif order_state == 5:
        return 'IsPicked'
    elif order_state == 6:
        return 'Canceled'
    elif order_state == 7:
        return 'MonthlyPayment'
    elif order_state == 12:
        return 'ReturnedToSender'
    elif order_state == 13:
        return 'MarkAsReturn'
    # elif order_state == 14:
    #     return 'InStorage' 
    # elif order_state == 15:
    #     return 'ApprovedInStorage' 
    elif order_state == 16:
        return 'ReadyForService' 
    elif order_state == 17:
        return 'OutForService' 
    elif order_state == 18:
        return 'PreCreateOrderRequest' 
    else:
        return 'NA'
    
def find_account_type(account_type):
    if account_type =="Unknown" :
        return 0
    elif account_type =="Done" :
        return 1
    elif account_type =="DHL" :
        return 2
    elif account_type =="Bar" :
        return 3
    elif account_type =="UPS" :
        return 4
    elif account_type =="Decathlon" :
        return 5
    elif account_type =="Marmelada" :
        return 6
    elif account_type =="YadMordechai" :
        return 7
    elif account_type =="MarmeladaMarket" :
        return 8
    elif account_type =="Exelot" :
        return 9
    elif account_type =="GeffenMedical" :
        return 10
    elif account_type =="SdeMoshe" :
        return 11
    elif account_type =="NegroCoffee" :
        return 12
    elif account_type =="Amirim" :
        return 13
    elif account_type =="CheapSim" :
        return 14
    elif account_type =="AquaBell" :
        return 15
    elif account_type =="OneProject" :
        return 16
    elif account_type =="ZigZag" :
        return 17
    elif account_type =="HFD" :
        return 18
    elif account_type =="ClothApp" :
        return 19
    elif account_type =="LittleOneSleep" :
        return 20
    elif account_type =="YDM" :
        return 21
    elif account_type =="GameStorm" :
        return 22
    elif account_type =="TAU" :
        return 23
    elif account_type =="Velo" :
        return 24
    elif account_type =="Benda" :
        return 25
    elif account_type =="MotorShop" :
        return 26
    elif account_type =="CDEK" :
        return 27
    elif account_type =="BerorHayil" :
        return 28
    elif account_type =="Azrieli" :
        return 29


    else:
        return 0
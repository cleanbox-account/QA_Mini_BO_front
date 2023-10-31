# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.01.02
# version ='1.0'
# ---------------------------------------------------------------------------
""" Orders list page """
# ---------------------------------------------------------------------------from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class OrdersListPage:
    def __init__(self, driver):
        self.driver = driver
        
    result_counter= (By.CSS_SELECTOR,"div[class='list-counter']")
    rows_in_table=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr")
    first_row_in_table=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr:nth-child(1)")
    
    #  M_  for Yad Mordehai / Sde Moshe / Amirim / YDM / BAR / DHL / OneProject / Geffen Madical
    m_edit_btn=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(1)")  
    m_date=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(2)")
    m_pcg_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(3)")
    m_order_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(4)")
    m_mobile_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(5)")
    m_usr_first_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(6)")
    m_usr_last_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(7)")
    m_order_status=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(8)")
    m_created_user=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(9)")
    m_station_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(10)")
    m_extension_date=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(11)")
    m_waybill=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(12)")
    
    #  D_  for Decathlon
    d_edit_btn=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(1)")  
    d_date=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(2)")
    d_pcg_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(3)")
    d_mobile_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(4)")
    d_usr_first_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(5)")
    d_usr_last_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(6)")
    d_order_status=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(7)")
    d_created_user=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(8)")
    d_station_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(9)")
    d_extension_date=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(10)")

    #  S_ for  UPS /  
    s_date=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(1)")
    s_pcg_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(2)")
    s_order_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(3)")
    s_mobile_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(4)")
    s_usr_first_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(5)")
    s_usr_last_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(6)")
    s_order_status=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(7)")
    s_created_user=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(8)")
    s_station_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(9)")
    s_extension_date=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(10)")
    s_waybill=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(11)")
    
    #  T_ for  TAU
    t_edit_btn=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(1)")
    t_date=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(2)")
    t_pcg_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(3)")
    t_order_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(4)")
    t_mobile_number=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(5)")
    t_usr_first_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(6)")
    t_usr_last_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(7)")
    t_order_status=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(8)")
    t_created_user=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(9)")
    t_station_name=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(10)")
    t_extension_date=(By.CSS_SELECTOR,"div.table-container > table > tbody > tr > td:nth-child(11)")


    
    def getResultsAmount(self):
        result=self.driver.find_element(*OrdersListPage.result_counter).text.split(" ")
        return result[1] #return second element(number) from string
    
    # def getRowContent(self,table_type): # table type M_ D_ S_  or T_
    #     order_details=[]
    #     rows=self.driver.find_elements(*OrdersListPage.rows_in_table)
    #     if len(rows)>0:
    #         for row in rows:
    #             if table_type=='D_':
    #                 date=row.find_element(*OrdersListPage.str(table_type+date)).text
    #                 pcg_number=row.find_element(*OrdersListPage.str(table_type+pcg_number)).text
    #                 mobile_number=row.find_element(*OrdersListPage.str(table_type+mobile_number)).text
    #                 usr_first_name=row.find_element(*OrdersListPage.str(table_type+usr_first_name)).text
    #                 usr_last_name=row.find_element(*OrdersListPage.str(table_type+usr_last_name)).text
    #                 order_status=row.find_element(*OrdersListPage.str(table_type+order_status)).text
    #                 created_user=row.find_element(*OrdersListPage.str(table_type+created_user)).text
    #                 station_name=row.find_element(*OrdersListPage.str(table_type+station_name)).text
    #                 order_details={
    #                     'date':date,
    #                     'pcg_number':pcg_number,
    #                     'mobile_number':mobile_number,
    #                     'usr_first_name':usr_first_name,
    #                     'usr_last_name':usr_last_name,
    #                     'order_status':order_status,
    #                     'created_user':created_user,
    #                     'station_name':station_name,
    #                     }
    #                 return order_details
    #             else:
    #                 date=row.find_element(*OrdersListPage.str(table_type+date)).text
    #                 order_number=row.find_element(*OrdersListPage.str(table_type+order_number)).text
    #                 pcg_number=row.find_element(*OrdersListPage.str(table_type+pcg_number)).text
    #                 mobile_number=row.find_element(*OrdersListPage.str(table_type+mobile_number)).text
    #                 usr_first_name=row.find_element(*OrdersListPage.str(table_type+usr_first_name)).text
    #                 usr_last_name=row.find_element(*OrdersListPage.str(table_type+usr_last_name)).text
    #                 order_status=row.find_element(*OrdersListPage.str(table_type+order_status)).text
    #                 created_user=row.find_element(*OrdersListPage.str(table_type+created_user)).text
    #                 station_name=row.find_element(*OrdersListPage.str(table_type+station_name)).text
    #                 order_details={
    #                     'date':date,
    #                     'order_number':order_number,
    #                     'pcg_number':pcg_number,
    #                     'mobile_number':mobile_number,
    #                     'usr_first_name':usr_first_name,
    #                     'usr_last_name':usr_last_name,
    #                     'order_status':order_status,
    #                     'created_user':created_user,
    #                     'station_name':station_name,
    #                     }
    #                 return order_details
    #     else:
    #         return []
        
    def getFirstRow(self,table_type):
        first_row=self.driver.find_element(*OrdersListPage.first_row_in_table)
        if table_type=='D':
            date=first_row.find_element(*OrdersListPage.d_date).text
            pcg_number=first_row.find_element(*OrdersListPage.d_pcg_number).text
            mobile_number=first_row.find_element(*OrdersListPage.d_mobile_number).text
            usr_first_name=first_row.find_element(*OrdersListPage.d_usr_first_name).text
            usr_last_name=first_row.find_element(*OrdersListPage.d_usr_last_name).text
            order_status=first_row.find_element(*OrdersListPage.d_order_status).text
            created_user=first_row.find_element(*OrdersListPage.d_created_user).text
            station_name=first_row.find_element(*OrdersListPage.d_station_name).text
            order_details={
                'date':date,
                'pcg_number':pcg_number,
                'mobile_number':mobile_number,
                'usr_first_name':usr_first_name,
                'usr_last_name':usr_last_name,
                'order_status':order_status,
                'created_user':created_user,
                'station_name':station_name,
                'order_number':'',
                'waybill':''
                }
            return order_details
        elif table_type=='S':
            date=first_row.find_element(*OrdersListPage.s_date).text
            order_number=first_row.find_element(*OrdersListPage.s_order_number).text
            pcg_number=first_row.find_element(*OrdersListPage.s_pcg_number).text
            mobile_number=first_row.find_element(*OrdersListPage.s_mobile_number).text
            usr_first_name=first_row.find_element(*OrdersListPage.s_usr_first_name).text
            usr_last_name=first_row.find_element(*OrdersListPage.s_usr_last_name).text
            order_status=first_row.find_element(*OrdersListPage.s_order_status).text
            created_user=first_row.find_element(*OrdersListPage.s_created_user).text
            station_name=first_row.find_element(*OrdersListPage.s_station_name).text
            waybill=first_row.find_element(*OrdersListPage.s_waybill).text
            order_details={
                'date':date,
                'order_number':order_number,
                'pcg_number':pcg_number,
                'mobile_number':mobile_number,
                'usr_first_name':usr_first_name,
                'usr_last_name':usr_last_name,
                'order_status':order_status,
                'created_user':created_user,
                'station_name':station_name,
                'waybill':waybill
                }
            return order_details
        elif table_type=='M':
            date=first_row.find_element(*OrdersListPage.m_date).text
            order_number=first_row.find_element(*OrdersListPage.m_order_number).text
            pcg_number=first_row.find_element(*OrdersListPage.m_pcg_number).text
            mobile_number=first_row.find_element(*OrdersListPage.m_mobile_number).text
            usr_first_name=first_row.find_element(*OrdersListPage.m_usr_first_name).text
            usr_last_name=first_row.find_element(*OrdersListPage.m_usr_last_name).text
            order_status=first_row.find_element(*OrdersListPage.m_order_status).text
            created_user=first_row.find_element(*OrdersListPage.m_created_user).text
            station_name=first_row.find_element(*OrdersListPage.m_station_name).text
            waybill=first_row.find_element(*OrdersListPage.m_waybill).text
            order_details={
                'date':date,
                'order_number':order_number,
                'pcg_number':pcg_number,
                'mobile_number':mobile_number,
                'usr_first_name':usr_first_name,
                'usr_last_name':usr_last_name,
                'order_status':order_status,
                'created_user':created_user,
                'station_name':station_name,
                'waybill':waybill
                }
            return order_details
        elif table_type=='T':
            date=first_row.find_element(*OrdersListPage.m_date).text
            order_number=first_row.find_element(*OrdersListPage.m_order_number).text
            pcg_number=first_row.find_element(*OrdersListPage.m_pcg_number).text
            mobile_number=first_row.find_element(*OrdersListPage.m_mobile_number).text
            usr_first_name=first_row.find_element(*OrdersListPage.m_usr_first_name).text
            usr_last_name=first_row.find_element(*OrdersListPage.m_usr_last_name).text
            order_status=first_row.find_element(*OrdersListPage.m_order_status).text
            created_user=first_row.find_element(*OrdersListPage.m_created_user).text
            station_name=first_row.find_element(*OrdersListPage.m_station_name).text
            order_details={
                'date':date,
                'order_number':order_number,
                'pcg_number':pcg_number,
                'mobile_number':mobile_number,
                'usr_first_name':usr_first_name,
                'usr_last_name':usr_last_name,
                'order_status':order_status,
                'created_user':created_user,
                'station_name':station_name,
                'waybill':''
                }
            return order_details
        
    
        
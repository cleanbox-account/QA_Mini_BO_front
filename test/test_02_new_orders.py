# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.08.07
# version ='1.0'
# ---------------------------------------------------------------------------
""" testing with pytest tool. Testing of Mini BO for Exelot - new order pages"""
# ---------------------------------------------------------------------------
import random
import pytest
from time import sleep
from Data.all_types import switch_account_type_name
from pages.DecathlonStations import DecathlonStationSelectScreen
from pages.Menu import Menu
from pages.CreateNewOrder import CreateNewOrderPage
from pages.OrdersList import OrdersListPage
from utilsModules.FindUser import get_user
from utilsModules.LoginMiniBO import LoginMiniBO
from utilsModules.BaseClass import BaseClass
import Data.pages_addresses as env
from selenium.webdriver.common.keys import Keys


class TestNewOrders(BaseClass):
    main_page = env.main_page
    orders_list_page=env.orders_list_page
    stations_list_page=env.stations_list_page
    users_list_page=env.users_list_page
    create_new_order_page=env.create_new_order_page
    decathlon_stations_list=env.decathlon_stations_list

    @pytest.mark.parametrize('role', [pytest.param('Amirim' ), #amirim
                                      pytest.param('Bar' ),   #bar
                                      pytest.param('DHL'),  #dhl
                                      pytest.param('Decathlon' ),   #decathlon  
                                      pytest.param('GeffenMedical' ),   #gefenMedical 
                                      pytest.param('HFD' ),   #hfd 
                                      pytest.param('SdeMoshe' ),   #sde moshe       
                                      #pytest.param('UPS' ),   #ups
                                      pytest.param('YadMordechai' ),   #yadmordehai
                                      pytest.param('OneProject' ),   #oneProject
                                      pytest.param('YDM' ),   #ydm
                                      pytest.param('TAU' ),   #TAU                   
                                      pytest.param('Exelot' ),   #Exelot 
                                      pytest.param('BerorHayil')   #BerorHayil
                                      ])
    def test_02_new_orders(self, role):
        log = self.getLogger('test')
        log.info("---"+" "*10+"Create New Order test for <{0}> operator".format(role)+" "*10+"---")
        if not self.driver.current_url== self.main_page :
            menu_panel=Menu(self.driver)
            log.info("Logout try ...")
            try:
                menu_panel.clickMenuOpen()
                if self.verifyElSelectorPresence(menu_panel.logout):
                    menu_panel.clickLogout()
                    assert self.current_url==self.main_page , log.warning("Failed asertion, no logout")
                    log.info("Succeed assertion, login page was opened")
                else:
                    log.error("Logout button has not detected")
            except :
                pass
        assert self.driver.current_url == self.main_page , log.warning("Failed asertion, current page is not Login")
        log.info("Succeed to open login page: %s" % self.driver.current_url)
        user=get_user(role)
        assert not user==None , log.error("Failed assertion, user details was not found")
        log.info("Succeed to find user's details with {0}:".format(role))
        log.info("user first name:"+user["user_f_name"])
        log.info("user last name:"+user["user_l_name"])
        log.info("mobile number:"+user["mobile_number"])
        #log.info("password:"+user["password"])

        logined_yes_not=LoginMiniBO.login_to_mini_bo(self, user["mobile_number"], user["password"], role)
        if not logined_yes_not:
            assert  False
        elif role in ('DHL','Bar','UPS','YDM','HFD','Exelot'):
            assert self.driver.current_url == self.stations_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
        elif role =='Decathlon':
            assert self.driver.current_url == self.decathlon_stations_list, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
            dec_st_page=DecathlonStationSelectScreen(self.driver)
       
            stations_list=dec_st_page.getDecathllonStations()
            st_len=len(stations_list)
            indx=random.randint(0, st_len-1)
            if st_len>0:
                log.info(">>> Was selected '{0}' station".format(stations_list[indx].text))
                stations_list[indx].click()
            else:
                log.error("Was not detected decathlon stations")
                assert False 
            sleep(2)
        elif role in ('GeffenMedical','YadMordechai','SdeMoshe','Amirim','OneProject','TAU','BerorHayil'):
            assert self.driver.current_url == self.orders_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
        else:
            raise log.error("Failed , something well wrong")
        #self.driver.back()
        menu_panel=Menu(self.driver)

        menu_panel.clickMenuOpen()
        menu_panel.getCreateOrderLink()
        assert self.driver.current_url==self.create_new_order_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        
        
        c_order_page=CreateNewOrderPage(self.driver)
       
        has_new_order=False
        
        while not has_new_order:
            usr=get_user("Customer")
            usr_mobile=usr['mobile_number']
            usr_f_name=usr["user_f_name"]
            usr_l_name=usr["user_l_name"]

            new_pcg_number=switch_account_type_name(role)+str(random.randint(10000000, 99999999))
           
            c_order_page.getInputPcgNumber().send_keys(new_pcg_number)
            sleep(1)
            c_order_page.getInputMobileNumber().send_keys(usr_mobile)
            sleep(1)
            c_order_page.getInputFirstName().send_keys(Keys.CONTROL, 'a')
            c_order_page.getInputFirstName().send_keys(Keys.DELETE)
            c_order_page.getInputFirstName().send_keys(usr_f_name)
            sleep(1)
            c_order_page.getInputLastName().send_keys(Keys.CONTROL, 'a')
            c_order_page.getInputLastName().send_keys(Keys.DELETE)
            c_order_page.getInputLastName().send_keys(usr_l_name)
            sleep(1)
            if not role=='OneProject':
                c_order_page.getInputStations().click()
                sleep(1)
            
                station_number="5113"
                log.info("Try to find "+station_number+" ...")
                my_station=c_order_page.findStation(station_number)
                if my_station:
                    log.info("The  {0} station was selected".format(my_station))
                else:    
                    log.warning("Failed to find the relevant station, seems that has fixed station !.......... ")
                sleep(1)
            else:
                c_order_page.clickCreateBtn() #has some error with focus on this button for oneproject, should be double clicked
            c_order_page.clickCreateBtn()
            sleep(1)
            if self.verifyElSelectorPresence(c_order_page.msg_succ):
                log.info("Succeed new order creation!")
                c_order_page.clickCloseMsgBtn()
                has_new_order=True
                
            else:
                log.error("Failed new order creation") 
                c_order_page.clickCloseMsgBtn() 
                has_new_order=False
            
        
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getOrdersLink()
        assert self.driver.current_url==self.orders_list_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        orders_list=OrdersListPage(self.driver)
        log.info("Has {0} results".format(orders_list.getResultsAmount()))

        sleep(2)
        
        table_type='M' #default table form that has maximum columns view
        if role == 'Decathlon':
            table_type='D'
        elif role == 'TAU':
            table_type='T'
        elif role == 'UPS':
            table_type='S'
        else :
            table_type='M'
        
        
        
        first_order=orders_list.getFirstRow(table_type)
        log.info("\n NEW ORDER DETAILS:\n------------\n order: {0} \n pcg.num.: {1}  \n ord.status: {7} \n phone: {2} \n customer: {3} {4} \n station: {5} \n created by: {6}".format(
            first_order["order_number"],
            first_order["pcg_number"],
            first_order["mobile_number"],
            first_order["usr_first_name"],
            first_order["usr_last_name"],
            first_order["station_name"],
            first_order["created_user"],
            first_order["order_status"]
            ))
        sleep(2)
        assert new_pcg_number==first_order["pcg_number"], log.warning("The package number in last order is different from package number that used in new order")
        log.info("Succeed assertion , new created order displayed in orders list")
        sleep(2)
        menu_panel.clickMenuOpen()
        menu_panel.clickLogout()
        assert self.driver.current_url==self.main_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened after logout")
        sleep(1)
        sleep(1)
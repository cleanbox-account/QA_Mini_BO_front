# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.01.01
# version ='1.0'
# ---------------------------------------------------------------------------
""" testing with pytest tool. Testing of Mini BO for Sde Moshe - new order pages"""
# ---------------------------------------------------------------------------
import random
import pytest
from time import sleep
from pages.Menu import Menu
from pages.CreateNewOrder import CreateNewOrderPage
from pages.OrdersList import OrdersListPage
from utilsModules.FindUser import get_user
from utilsModules.LoginMiniBO import LoginMiniBO
from utilsModules.BaseClass import BaseClass
import Data.pages_addresses as env
from selenium.webdriver.common.keys import Keys


class TestAmirimNewOrder(BaseClass):
    main_page = env.main_page
    orders_list_page=env.orders_list_page
    stations_list_page=env.stations_list_page
    users_list_page=env.users_list_page
    create_new_order_page=env.create_new_order_page

    

    @pytest.mark.parametrize('role', [ pytest.param('Amirim' ),   
                                                    ])
    def test_10_for_sde_moshe_new_order(self, role):
        log = self.getLogger('test')
        log.info("---"+" "*10+"Menu overview test for <{0}> operator".format(role)+" "*10+"---")
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
        elif role =='Amirim':
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
        c_order_page.getInputStations().click()
        sleep(1)
        my_station=c_order_page.findStation("5999")
        if my_station:
            log.info("The  {0} station was selected".format(my_station))
        else:    
            log.warning("Failed to find the relevant station ")
        has_new_order=False
        while not has_new_order:
            usr=get_user("Customer")
            usr_mobile=usr['mobile_number']
            usr_f_name=usr["user_f_name"]
            usr_l_name=usr["user_l_name"]
            new_pcg_number="Amirim"+str(random.randint(100000, 999999))
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
            c_order_page.clickCreateBtn()
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
        
        first_order=orders_list.getFirstRow('M')
        log.info("\nLast Order :\n------------\n order - {0} \n pcg.num. - {1}  \n ord.status - {6} \n #{2} - <{3} {4}> - {5}".format(
            first_order["order_number"],
            first_order["pcg_number"],
            first_order["mobile_number"],
            first_order["usr_first_name"],
            first_order["usr_last_name"],
            first_order["station_name"],
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
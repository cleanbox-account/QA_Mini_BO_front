# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.04.30
# version ='1.0'
# ---------------------------------------------------------------------------
""" testing with pytest tool. Testing of OneProjec pages"""
# ---------------------------------------------------------------------------
import pytest
from time import sleep
from pages.Menu import Menu
from utilsModules.FindUser import get_user
from utilsModules.LoginMiniBO import LoginMiniBO
from utilsModules.BaseClass import BaseClass
import Data.pages_addresses as env


class TestOneProjectNewOrderAPI(BaseClass):
    main_page = env.main_page
    orders_list_page=env.orders_list_page
    stations_list_page=env.stations_list_page
    users_list_page=env.users_list_page
    reports_page=env.reports_page
    scan_order_page=env.scan_order_page

    
    def test_12_oneprj_neworder_api(self):
        log = self.getLogger('test')
        log.info("---"+" "*10+"OneProject Menu overview test for 'OneProject' operator"+" "*10+"---")
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
        user=get_user("OneProject")
        assert not user==None , log.error("Failed assertion, user details was not found")
        log.info("Succeed to find user's details")
        log.info("user first name:"+user["user_f_name"])
        log.info("user last name:"+user["user_l_name"])
        log.info("mobile number:"+user["mobile_number"])
        #log.info("password:"+user["password"])

        logined_yes_not=LoginMiniBO.login_to_mini_bo(self, user["mobile_number"], user["password"], "OneProject")
        if logined_yes_not:
            assert self.driver.current_url == self.orders_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for 'OneProject' role has opened".format(self.driver.current_url))
        else:
            raise log.error("Failed , something well wrong")
        #self.driver.back()
        menu_panel=Menu(self.driver)
        
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getOrdersLink()
        assert self.driver.current_url==self.orders_list_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getScanLink()
        assert self.driver.current_url==self.scan_order_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.clickLogout()
        assert self.driver.current_url==self.main_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened after logout")
        sleep(1)
# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2022.12.27
# version ='1.0'
# ---------------------------------------------------------------------------
""" testing with pytest tool. Testing Login to Mini Backoffice web application"""
# ---------------------------------------------------------------------------
import pytest
from time import sleep
from pages.Menu import Menu
from utilsModules.LoginMiniBO import LoginMiniBO
from utilsModules.BaseClass import BaseClass
from utilsModules.FindUser import get_user
import Data.pages_addresses as env


class TestStartBAC(BaseClass):
    main_page = env.main_page
    orders_list_page=env.orders_list_page
    decathlon_stations_list=env.decathlon_stations_list
    stations_list_page=env.stations_list_page
        
    @pytest.mark.parametrize('role', [pytest.param('DHL'),  #dhl
                                                pytest.param('Bar' ),   #bar
                                                pytest.param('UPS' ),   #ups
                                                pytest.param('Decathlon' ),   #decathlon
                                                pytest.param('GeffenMedical' ),   #gefenMedical
                                                pytest.param('YadMordechai' ),   #yadmordehai
                                                pytest.param('SdeMoshe' ),   #sde moshe
                                                pytest.param('Amirim' ),   #amirim
                                                pytest.param('OneProject' ),   #oneProject
                                                pytest.param('Customer', marks=pytest.mark.xfail )   #customer
                                               ])
    def test_01_login_from_json(self, role):
        log = self.getLogger('test')
        log.info("---"+" "*10+"Mini BO login test for <{0}> operator".format(role)+" "*10+"---")
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
        elif role in ('DHL','Bar','UPS'):
            assert self.driver.current_url == self.stations_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
        elif role =='Decathlon':
            assert self.driver.current_url == self.decathlon_stations_list, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
        elif role in ('GeffenMedical','YadMordechai','SdeMoshe','Amirim','OneProject'):
            assert self.driver.current_url == self.orders_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
        else:
            raise log.error("Failed , something well wrong")
        #self.driver.back()
        menu_panel=Menu(self.driver)
        log.info("Logout try ...")
        try:
            menu_panel.clickMenuOpen()
            if self.verifyElSelectorPresence(menu_panel.logout):
                menu_panel.clickLogout()
                assert self.current_url==self.main_page , log.warning("Failed asertion, no logout")
                log.info("Succeed assertion, login page was opened")
            else:
                log.war("Logout button has not detected")
                
        except :
            log.warning("Use back command...")
            self.driver.back()
        sleep(1)
        
    
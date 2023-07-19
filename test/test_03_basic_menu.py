# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.01.01
# version ='1.0'
# ---------------------------------------------------------------------------
""" testing with pytest tool. Testing of DHL/Bar/UPS pages"""
# ---------------------------------------------------------------------------
import pytest
from time import sleep
from pages.Menu import Menu
from utilsModules.FindUser import get_user
from utilsModules.LoginMiniBO import LoginMiniBO
from utilsModules.BaseClass import BaseClass
import Data.pages_addresses as env


class TestBasicSuppliersBO(BaseClass):
    main_page = env.main_page
    orders_list_page=env.orders_list_page
    stations_list_page=env.stations_list_page
    users_list_page=env.users_list_page
    reports_page=env.reports_page
    create_new_order_page=env.create_new_order_page

    

    @pytest.mark.parametrize('role', [pytest.param('DHL'),  #dhl
                                                pytest.param('Bar' ),   #bar
                                                pytest.param('UPS' ),   #ups
                                                pytest.param('YDM' ),   #ydm
                                                pytest.param('TAU' ),   #TAU
                                                pytest.param('YadMordechai' ),   #yadmordehai
                                                pytest.param('Amirim' ),   #amirim
                                                pytest.param('SdeMoshe' ),  #sde moshe
                                                pytest.param('GeffenMedical' ),  #GeffenMedical
                                                pytest.param('HFD' )  #HFD
                                                    ])
    def test_02_menu_overview(self,role):
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
        elif role in ('DHL','Bar','UPS','YDM','HFD'):
            assert self.driver.current_url == self.stations_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
        elif role in ('GeffenMedical','YadMordechai','SdeMoshe','Amirim','TAU'):
            assert self.driver.current_url == self.orders_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
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
        menu_panel.getStationsLink()
        assert self.driver.current_url==self.stations_list_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getUsersLink()
        assert self.driver.current_url==self.users_list_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getReportsLink()
        assert self.driver.current_url==self.reports_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        
        if role in ('YDM','TAU','YadMordechai','SdeMoshe','Amirim','GeffenMedical','HFD'):
            menu_panel.clickMenuOpen()
            menu_panel.getCreateOrderLink()
            assert self.driver.current_url==self.create_new_order_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
            log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
            sleep(1)
            
        menu_panel.clickMenuOpen()
        menu_panel.clickLogout()
        assert self.driver.current_url==self.main_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened after logout")
        sleep(1)
# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.01.01
# version ='1.0'
# ---------------------------------------------------------------------------
""" testing with pytest tool. Testing of DHL/Bar/UPS pages"""
# ---------------------------------------------------------------------------
import random
import pytest
from time import sleep
from pages.DecathlonStations import DecathlonStationSelectScreen
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
    decathlon_stations_list=env.decathlon_stations_list
    failed_sms_page=env.failed_sms_page

    @pytest.mark.parametrize('role', [pytest.param('Amirim' ), #amirim
                                      pytest.param('Bar' ),   #bar
                                      pytest.param('DHL'),  #dhl
                                      pytest.param('Decathlon' ),   #decathlon  
                                      pytest.param('GeffenMedical' ),   #gefenMedical 
                                      pytest.param('HFD' ),   #hfd 
                                      pytest.param('SdeMoshe' ),   #sde moshe       
                                      pytest.param('UPS' ),   #ups
                                      pytest.param('YadMordechai' ),   #yadmordehai
                                      pytest.param('OneProject' ),   #oneProject
                                      pytest.param('YDM' ),   #ydm
                                      pytest.param('TAU' ),   #TAU                   
                                      pytest.param('Exelot' ),   #Exelot   
                                      pytest.param('BerorHayil' ),   #BerorHayil   
                                                    ])
    def test_01_login_and_menu_overview(self,role):
        log = self.getLogger('test')
        log.info("---"+" "*10+"Login and menu overview test for <{0}> operator".format(role)+" "*10+"---")
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
        elif role in ('GeffenMedical','YadMordechai','SdeMoshe','Amirim','TAU','OneProject','BerorHayil'):
            assert self.driver.current_url == self.orders_list_page, log.error("Failed assertion, wrong url...")
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
        
        if not role =='OneProject':
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
        
        if  role not in ('Decathlon','TAU'):
            menu_panel.clickMenuOpen()
            menu_panel.getReportsLink()
            assert self.driver.current_url==self.reports_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
            log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
            sleep(1)
        
        menu_panel.clickMenuOpen()
        menu_panel.getCreateOrderLink()
        assert self.driver.current_url==self.create_new_order_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
                    
        menu_panel.clickMenuOpen()
        menu_panel.getFailedSMSLink()
        assert self.driver.current_url==self.failed_sms_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(3)
                    
        menu_panel.clickMenuOpen()
        menu_panel.clickLogout()
        assert self.driver.current_url==self.main_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened after logout")
        sleep(1)
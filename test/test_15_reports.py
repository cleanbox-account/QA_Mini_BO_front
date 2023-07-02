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
from pages.Reports import ReportScreen
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

    
    @pytest.mark.parametrize('role', [pytest.param('DHL'),  #dhl
                                                pytest.param('Bar' ),   #bar
                                                pytest.param('UPS' ),   #ups
                                                #pytest.param('Decathlon' ),   #decathlon
                                                pytest.param('GeffenMedical' ),   #gefenMedical
                                                pytest.param('YadMordechai' ),   #yadmordehai
                                                pytest.param('SdeMoshe' ),   #sde moshe
                                                pytest.param('Amirim' ),   #amirim
                                                pytest.param('Customer', marks=pytest.mark.xfail )   #customer
                                               ])
    def test_15_report_screen_overview(self,role):
        log = self.getLogger('test')
        log.info("---"+" "*10+"Package Debit Report test for <{0}> operator".format(role)+" "*10+"---")
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
        elif role in ('Decathlon','GeffenMedical','YadMordechai','SdeMoshe','Amirim'):
            assert self.driver.current_url == self.orders_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
        else:
            raise log.error("Failed , something well wrong")
        #self.driver.back()
        menu_panel=Menu(self.driver)
        
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getReportsLink()
        assert self.driver.current_url==self.reports_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        reports_page=ReportScreen(self.driver)
        reports_page.getYearList()
        log.info("Selected year - {0}".format(reports_page.selectYear(2)) )#2023
        sleep(2)
        # reports_page.getYearList()
        # log.info("Selected year - {0}".format(reports_page.selectYear(0)) ) #2021
        # sleep(2)
        # reports_page.getYearList()
        # log.info("Selected year - {0}".format(reports_page.selectYear(1)) ) #2022
        # sleep(2)
        reports_page.getMonthList() 
        log.info("Selected month - {0}".format(reports_page.selectMoth(0)) ) #jan
        sleep(2)
        # reports_page.getMonthList()
        # log.info("Selected month - {0}".format(reports_page.selectMoth(2)) ) #mar
        # sleep(2)
        # reports_page.getMonthList()
        # log.info("Selected month - {0}".format(reports_page.selectMoth(3)) ) #apr
        # sleep(2)
        # reports_page.getMonthList()
        # log.info("Selected month - {0}".format(reports_page.selectMoth(6)) ) #yul
        # sleep(2)
        # reports_page.getMonthList()
        # log.info("Selected month - {0}".format(reports_page.selectMoth(8)) ) #sep
        # sleep(2)
        reports_page.downloadReport()
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.clickLogout()
        assert self.driver.current_url==self.main_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened after logout")
        sleep(1)
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
from pages.OrdersList import OrdersListPage
from utilsModules.FindUser import get_user
from utilsModules.LoginMiniBO import LoginMiniBO
from utilsModules.BaseClass import BaseClass
import Data.pages_addresses as env


class TestDecathlonBO(BaseClass):
    main_page = env.main_page
    decathlon_stations_list=env.decathlon_stations_list
    orders_list_page=env.orders_list_page
    stations_list_page=env.stations_list_page
    users_list_page=env.users_list_page
    create_new_order_page=env.create_new_order_page
    update_msg_page=env.update_msg_page
    reports_page=env.reports_page

    @pytest.mark.parametrize('role', [pytest.param('Decathlon' )])
    def test_03_for_decathlon_menu_overview(self, role):
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
        elif role == 'Decathlon':
            assert self.driver.current_url == self.decathlon_stations_list, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
        else:
            raise log.error("Failed , something well wrong")

        dec_st_page=DecathlonStationSelectScreen(self.driver)
       
        stations_list=dec_st_page.getDecathllonStations()
        st_len=len(stations_list)
        if st_len>0:
            for i in range(st_len):
                log.info("{0} - {1}".format(i+1,stations_list[i].text))
        else:
            log.error("Was not detected decathlon stations")
            assert False 
        sleep(2)
        indx=random.randint(0, st_len-1)
        log.info(">>> Was selected '{0}' station".format(stations_list[indx].text))
        stations_list[indx].click()
        assert self.driver.current_url == self.orders_list_page, log.error("Failed assertion, wrong url...")
        log.info("Succeed Assertion, the <{0}> page for selected station has opened".format(self.driver.current_url,role))
        menu_panel=Menu(self.driver)
        
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getOrdersLink()
        assert self.driver.current_url==self.orders_list_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        orders_list=OrdersListPage(self.driver)
        log.info("Has {0} results".format(orders_list.getResultsAmount()))
        
        first_order=orders_list.getFirstRow('D') #decathloc table type
        log.info("\n   Last Order :\n pcg.num. - {0}  \n ord.status - {5} \n #{1} - <{2} {3}> - {4}".format(

            first_order["pcg_number"],
            first_order["mobile_number"],
            first_order["usr_first_name"],
            first_order["usr_last_name"],
            first_order["station_name"],
            first_order["order_status"]
            ))
        sleep(2)
        menu_panel.clickMenuOpen()
        menu_panel.getStationsLink()
        assert self.driver.current_url==self.stations_list_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getCreateOrderLink()
        assert self.driver.current_url==self.create_new_order_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getUsersLink()
        assert self.driver.current_url==self.users_list_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.getEditMsgLink()
        assert self.driver.current_url==self.update_msg_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        menu_panel.clickMenuOpen()
        menu_panel.clickLogout()
        assert self.driver.current_url==self.main_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened after logout")
        sleep(1)
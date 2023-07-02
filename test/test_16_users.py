# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.02.07
# version ='1.0'
# ---------------------------------------------------------------------------
""" testing with pytest tool. Testing Users page to Mini Backoffice web application"""
# ---------------------------------------------------------------------------
import random
import pytest
from time import sleep
from pages.DecathlonStations import DecathlonStationSelectScreen
from pages.Menu import Menu
from pages.NewUser import NewUserPage
from pages.UsersList import UsersListePage
from utilsModules.LoginMiniBO import LoginMiniBO
from utilsModules.BaseClass import BaseClass
from utilsModules.FindUser import get_user
import Data.pages_addresses as env
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestUsersPage(BaseClass):
    main_page = env.main_page
    orders_list_page=env.orders_list_page
    decathlon_stations_list=env.decathlon_stations_list
    stations_list_page=env.stations_list_page
    new_user_page=env.new_user_page
    users_list_page=env.users_list_page
        
    @pytest.mark.parametrize('role', [pytest.param('DHL'),  #dhl
                                                pytest.param('Bar' ),   #bar
                                                pytest.param('UPS' ),   #ups
                                                pytest.param('Decathlon' ),   #decathlon
                                                pytest.param('GeffenMedical' ),   #gefenMedical
                                                pytest.param('YadMordechai' ),   #yadmordehai
                                                pytest.param('SdeMoshe' ),   #sde moshe
                                                pytest.param('Amirim' ),   #amirim
                                               ])
    def test_16_new_user(self, role):
        log = self.getLogger('test')
        log.info("---"+" "*10+"Mini BO users page test for <{0}> operator".format(role)+" "*10+"---")
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
            dec_st_page=DecathlonStationSelectScreen(self.driver)
       
            stations_list=dec_st_page.getDecathllonStations()
            st_len=len(stations_list)
            if st_len>0:
                indx=random.randint(0, st_len-1)
                log.info(">>> Was selected '{0}' station".format(stations_list[indx].text))
                stations_list[indx].click()
            else:
                log.error("Was not detected decathlon stations")
                assert False 
            sleep(2)
            
            assert self.driver.current_url == self.orders_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for selected station has opened".format(self.driver.current_url,role))
        elif role in ('GeffenMedical','YadMordechai','SdeMoshe','Amirim'):
            assert self.driver.current_url == self.orders_list_page, log.error("Failed assertion, wrong url...")
            log.info("Succeed Assertion, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
        else:
            raise log.error("Failed , something well wrong")
        #self.driver.back()
        menu_panel=Menu(self.driver)
        menu_panel.clickMenuOpen()
        menu_panel.getUsersLink()
        assert self.driver.current_url==self.users_list_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        
        usr_page=UsersListePage(self.driver)
        log.info("Try to open New User Form")
        usr_page.getNewUser()
        assert self.driver.current_url==self.new_user_page , log.error("Failed assertion, wrong url...{0}".format(self.driver.current_url))
        log.info("Succeed assertion , correct url has opened...{0}".format(self.driver.current_url))
        sleep(1)
        
        new_usr_pg=NewUserPage(self.driver)
        new_fname="first {0}".format(role)
        new_lname="last {0}".format(role)
        new_phone="0570"+str(random.randint(100000, 999999))
        
        new_usr_pg.getFirstNameInput().send_keys(new_fname)
        new_usr_pg.getLastNameInput().send_keys(new_lname)
        new_usr_pg.getMobileNumberInput().send_keys(new_phone)
        log.info("New User details were inputted : \n{0} {1} - #{2}".format(new_fname,new_lname,new_phone))
        sleep(1)
        new_usr_pg.saveNewUser()
        
        if self.verifyElSelectorPresence(new_usr_pg.poped_msg):
            log.info("Has popped message, try to close popped message")
            new_usr_pg.closePoppedMsg()
            sleep(2)
        else:
            assert False , log.error("Failed to create new user")
            
        #find new user in table
        self.verifyCurrentURL(self.users_list_page)
        usr_list=usr_page.getUserRows()
        has_usr=False
        
        for usr in usr_list:
            if usr.find_element(By.CSS_SELECTOR,"td:nth-child(3)").text==new_phone:
                
                log.info("Succeed to find new user in the table: \n>>> {0} {1} - #{2} <<<".format(usr.find_element(By.CSS_SELECTOR,"td:nth-child(1)").text,
                                                                                          usr.find_element(By.CSS_SELECTOR,"td:nth-child(2)").text,
                                                                                          usr.find_element(By.CSS_SELECTOR,"td:nth-child(3)").text))
                has_usr=True
                sleep(2)
                usr.find_element(By.CSS_SELECTOR,"td:nth-child(5)").click()
                if self.verifyElSelectorPresence(usr_page.yes_no_del_usr):
                    log.info("Try to delete New User...")
                    try :
                        usr_page.DeleteNewUser()
                        log.info("Succeed New User deletion")
                    except:
                        
                        assert False,log.error("Failed to delete New User...")
                else:
                    log.error("Something gones wrong...no popped message about deletion")
                exit
                
        assert has_usr , log.error("Failed assertion, the new user is not been found")
        sleep(2)

    
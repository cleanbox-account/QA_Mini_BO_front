# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.01.13
# version ='1.0'
# ---------------------------------------------------------------------------
""" LoginMiniBO class for login proccess in Mini Backoffice web application"""
# ---------------------------------------------------------------------------

from utilsModules.BaseClass import BaseClass
from pages.LoginPage import LoginScreen
from selenium.webdriver.common.keys import Keys

# ---------------------------------------------------------------------------
class LoginMiniBO(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def login_to_mini_bo(self, my_phone, my_pass, role):
        log = self.getLogger('test')
        log.info("Login try for {0}...".format(role))
        loginpage = LoginScreen(self.driver)
        loginpage.getPhoneInput().send_keys(Keys.CONTROL, 'a')
        loginpage.getPhoneInput().send_keys(Keys.DELETE)
        loginpage.getPasswordInput().send_keys(Keys.CONTROL, 'a')
        loginpage.getPasswordInput().send_keys(Keys.DELETE)
       
        loginpage.getPhoneInput().send_keys(my_phone)
        loginpage.getPasswordInput().send_keys(my_pass)

        try:
            loginpage.getSignInBtn()
            if self.verifyElSelectorPresence(loginpage.bad_login_msg):
                loginpage.getCloseErrBtn()
                log.warning("Has Error popped message, Failed Login...")
                return False   
            else:  
                log.info("Succeed login, the <{0}> page for <{1}> role has opened".format(self.driver.current_url,role))
                return True
        except Exception as err:
            log.warning("Failed to login with %s phone number " % my_phone)
            log.warning("Has error, : \n %s" % err)
            return False
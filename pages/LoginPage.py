from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginScreen:

    def __init__(self, driver):
        self.driver = driver

    phone_num_input = (By.CSS_SELECTOR, "div.input-field:nth-child(1) input[class*='infl-wrapper undefined infl-err  infl-mandatory']")
    password_input = (By.CSS_SELECTOR, "div.input-field:nth-child(2) input[class*='infl-wrapper undefined infl-err  infl-mandatory']")
   
    signIn_btn = (By.CSS_SELECTOR,"button[class='circle-button']")
    bad_login_msg = (By.CSS_SELECTOR,"div[class*='message-wrapper error']")
    close_err_msg=(By.CSS_SELECTOR,"div[class='message-button']")
    

    def getPhoneInput(self):
        return self.driver.find_element(*LoginScreen.phone_num_input)

    def getPasswordInput(self):
        return self.driver.find_element(*LoginScreen.password_input)
    
    def getErrorMsg(self):
        try:
            err_msg = self.driver.find_element(*LoginScreen.bad_login_msg)
            return err_msg
        except:
            return False

    def getCloseErrBtn(self):
        return self.driver.find_element(*LoginScreen.close_err_msg).click()
    
    def getSignInBtn(self):
        return self.driver.find_element(*LoginScreen.signIn_btn).click()
            

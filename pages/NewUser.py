# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.02.07
# version ='1.0'
# ---------------------------------------------------------------------------
""" New User page """
# ---------------------------------------------------------------------------from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class NewUserPage:
    def __init__(self, driver):
        self.driver = driver
        
    new_usr= (By.CSS_SELECTOR,"div[class='btn-new-user']")
    
    new_usr_input_fname=(By.CSS_SELECTOR,"input[id='firstName']")
    new_usr_input_lname=(By.CSS_SELECTOR,"input[id='lastName']")
    new_usr_input_mobile=(By.CSS_SELECTOR,"input[id='mobilePhone']")
    new_usr_save_btn=(By.CSS_SELECTOR,"button[class='button undefined']")
    
    poped_msg=(By.CSS_SELECTOR,"div[class*='noti-modal-container']")
    close_msg=(By.CSS_SELECTOR,"div[class='rectangle-button noti-modal-button']")
    

    def getFirstNameInput(self):
        return self.driver.find_element(*NewUserPage.new_usr_input_fname)

    def getLastNameInput(self):
        return self.driver.find_element(*NewUserPage.new_usr_input_lname)

    def getMobileNumberInput(self):
        return self.driver.find_element(*NewUserPage.new_usr_input_mobile)
    
    def saveNewUser(self):
        return self.driver.find_element(*NewUserPage.new_usr_save_btn).click()
    
    def closePoppedMsg(self):
        return self.driver.find_element(*NewUserPage.close_msg).click()
    
    
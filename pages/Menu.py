# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2022.04.07
# version ='1.0'
# ---------------------------------------------------------------------------
""" Home Page, links to some pages, links for supplier environment : scan orders for sending and receiving """
# ---------------------------------------------------------------------------from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Menu:
    def __init__(self, driver):
        self.driver = driver

        
    menu_active = (By.CSS_SELECTOR, "div[class='plate plate4 active']")
    menu_no_active = (By.CSS_SELECTOR, "div[class='plate plate4']")
    
    menu_list_content=(By.CSS_SELECTOR,"div[class='menu-item']")
    menu_list=(By.CSS_SELECTOR,"div[class='menu-items-wrapper']")
    
    orders=(By.XPATH,"//div[text()='הזמנות']")
    create_oreders=(By.XPATH,"//div[text()='יצירת הזמנה']")
    edit_messages=(By.XPATH,"//div[text()='עדכון הודעה']")
    stations=(By.XPATH,"//div[text()='עמדות']")
    users=(By.XPATH,"//div[text()='משתמשים']")
    reports=(By.XPATH,"//div[text()='דוח חיובי חבילות']")
    scan=(By.XPATH,"//div[text()='סריקה']")
    logout=(By.XPATH,"//div[text()='התנתק']")

    def getOrdersLink(self):
        try :
            self.driver.find_element(*Menu.orders).click()
            return True
        except:
            return False
        
    def getCreateOrderLink(self):
        try :
            self.driver.find_element(*Menu.create_oreders).click()
            return True
        except:
            return False
        
    def getEditMsgLink(self):
        try :
            self.driver.find_element(*Menu.edit_messages).click()
            return True
        except:
            return False
        
    def getStationsLink(self):
        try :
            self.driver.find_element(*Menu.stations).click()
            return True
        except:
            return False
        
    def getUsersLink(self):
        try :
            self.driver.find_element(*Menu.users).click()
            return True
        except:
            return False
        
    def getReportsLink(self):
        try :
            self.driver.find_element(*Menu.reports).click()
            return True
        except:
            return False
        
    def getScanLink(self):
        try :
            self.driver.find_element(*Menu.scan).click()
            return True
        except:
            return False
        
    def clickLogout(self):
        return self.driver.find_element(*Menu.logout).click()
             
        
        
    
    def clickMenuOpen(self):
        return self.driver.find_element(*Menu.menu_no_active).click()
    
    def clickMenuClose(self):
        return self.driver.find_element(*Menu.menu_active).click()
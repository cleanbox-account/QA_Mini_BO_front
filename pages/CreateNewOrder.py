# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2023.06.19
# version ='1.0'
# ---------------------------------------------------------------------------
""" Create New Order page """
# ---------------------------------------------------------------------------from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CreateNewOrderPage:
    def __init__(self, driver):
        self.driver = driver
        
    #stations input    
    #station_input=(By.CSS_SELECTOR,"input[id='react-select-2-input']")
    station_input=(By.CSS_SELECTOR,"div[class*='station-selector']  input")
    station_menu=(By.CSS_SELECTOR,"div[class*='station-selector']")
    #stations_in_list=(By.CSS_SELECTOR,"div[id='react-select-2-listbox'] > div > div")
    #stations_in_list=(By.CSS_SELECTOR,"div[class*='station-selector']:nth-child(2)>div>div div")
    stations_in_list=(By.CSS_SELECTOR,"div[class*='station-selector'] *:nth-child(4)>div div")

    pcg_num_input=(By.CSS_SELECTOR,"input[placeholder='*מספר חבילה']")
    mobile_num_input=(By.CSS_SELECTOR,"input[placeholder='*מספר טלפון']")
    first_name_input=(By.CSS_SELECTOR,"input[placeholder='*שם פרטי']")
    last_name_input=(By.CSS_SELECTOR,"input[placeholder='*שם משפחה']")
    
    back_btn=(By.CSS_SELECTOR,"button[class='button back']")
    create_btn=(By.CSS_SELECTOR,"button[class='button undefined']")
    
    msg_succ = (By.CSS_SELECTOR,"div[class*='message-wrapper success']")
    close_msg = (By.CSS_SELECTOR,"div[class='message-button']")

    
    def getInputStations(self):
        return self.driver.find_element(*CreateNewOrderPage.station_input)
    
    def getInputPcgNumber(self):
        return self.driver.find_element(*CreateNewOrderPage.pcg_num_input)
    
    def getInputFirstName(self):
        return self.driver.find_element(*CreateNewOrderPage.first_name_input)
    
    def getInputLastName(self):
        return self.driver.find_element(*CreateNewOrderPage.last_name_input)
    
    def getInputMobileNumber(self):
        return self.driver.find_element(*CreateNewOrderPage.mobile_num_input)
    
    def clickBackBtn(self):
        return self.driver.find_element(*CreateNewOrderPage.back_btn).click()
    
    def clickCreateBtn(self):
        try:
            create_btn= WebDriverWait(self.driver,2).until(EC.element_to_be_clickable(CreateNewOrderPage.create_btn))

            return create_btn.click()
        except :
            return False
    def clickCloseMsgBtn(self):
        return self.driver.find_element(*CreateNewOrderPage.close_msg).click()
    
    def findStation(self,station_key):
        stations=[]
        try:
            stations=self.driver.find_elements(*CreateNewOrderPage.stations_in_list)
            len_st=len(stations)
            if len_st>0:
                for st in stations:
                    if station_key in st.text:
                        station_name=st.text
                        try:
                            st.click()
                        except Exception:
                            st.find_element_by_xpath("..").click()
                
                        return station_name  
                      
                return stations[0].click()     
            else:
                return False
        except NoSuchElementException:
            return False
        
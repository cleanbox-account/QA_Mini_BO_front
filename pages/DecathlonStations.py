from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class DecathlonStationSelectScreen:

    def __init__(self, driver):
        self.driver = driver

    decathlon_stations = (By.CSS_SELECTOR, "div[class='decathlon-station-select']> div")

    

    def getDecathllonStations(self):
        return self.driver.find_elements(*DecathlonStationSelectScreen.decathlon_stations)



            


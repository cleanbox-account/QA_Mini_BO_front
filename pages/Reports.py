from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ReportScreen:

    def __init__(self, driver):
        self.driver = driver

    month_list = (By.CSS_SELECTOR, "div[id='month']")
    year_list = (By.CSS_SELECTOR, "div[id='year']")

    months=(By.CSS_SELECTOR,"div[id='month'] option")
    years=(By.CSS_SELECTOR,"div[id='year'] option")
    
    download=(By.CSS_SELECTOR,"input[class='download-file-button']")

    def getMonthList(self):
        return self.driver.find_element(*ReportScreen.month_list).click()

    def getYearList(self):
        return self.driver.find_element(*ReportScreen.year_list).click()

    def selectYear(self,yr=0):
        years=self.driver.find_elements(*ReportScreen.years)
        sel_yr=years[yr].text
        years[yr].click()
        return sel_yr

    def selectMoth(self,mnth=0):
        months= self.driver.find_elements(*ReportScreen.months)
        sel_mnth= months[mnth].text
        months[mnth].click()
        return sel_mnth    

    def downloadReport(self):
        return self.driver.find_element(*ReportScreen.download).click()
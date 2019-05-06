from selenium.webdriver.common.keys import Keys
class WorkMarket_Home_Page():

    def __init__(self, driver):
        self.driver = driver

        self.find_talent_xpath = "//div[text()='Find Talent']"
        self.search_workers_id = "input-text"

    def click_find_talent(self):
        self.driver.find_element_by_xpath(self.find_talent_xpath).click()

    def search_worker(self, word):
        self.driver.find_element_by_id(self.search_workers_id).send_keys(word)
        self.driver.find_element_by_id(self.search_workers_id).send_keys(Keys.ENTER)


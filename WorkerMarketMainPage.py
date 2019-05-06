from selenium import webdriver
driver = webdriver.Chrome()
driver.get(
    'https://dev.workmarket.com/register/campaign/10081C503B209A0C8E7F05FDCC1AA98D4C904DEEF5F73265CAE38C744E7EAD3E')

# Element Locator for sing in Page Dev

join_as_individual_xpath = "//span[text()='Join as an individual']"
first_name_id = "firstname"
last_name_id = 'lastname'
email_input_id = 'email'
password_input_id = 'password'
check_box_css = "input[type='checkbox']"
register_button_xpath = "//span[text()='Register']"


# Enter Credential for Login_Page_Dev

driver.find_element_by_xpath(join_as_individual_xpath).click()
driver.find_element_by_id(first_name_id).send_keys("John")
driver.find_element_by_id(last_name_id).send_keys("Smith")
driver.find_element_by_id(email_input_id).send_keys("WorkMarket2017@gmail.com")
driver.find_element_by_id(password_input_id).send_keys("Summer2019@@")
driver.find_element_by_css_selector(check_box_css).click()
driver.find_element_by_xpath(register_button_xpath).click()


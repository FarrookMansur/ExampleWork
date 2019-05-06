class WorkMarket_Login_Page():

    def __init__(self, driver):
        self.driver = driver

        self.login_email_id = "login-email"
        self.password_id = "login-password"
        self.checkbox_id = "credentials__remember-me"
        self.login_button_id = "login_page_button"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.login_email_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)

    def select_checkbox(self):
        self.driver.find_element_by_id(self.checkbox_id).click()

    def click_login_btn(self):
        self.driver.find_element_by_id(self.login_button_id).click()

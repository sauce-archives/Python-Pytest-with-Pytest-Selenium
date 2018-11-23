from selenium import webdriver

class SamplePage(object):
    
    def __init__(self, selenium):
        self.driver = selenium

    def login_as(self, username, password):
        self.driver.find_element_by_css_selector('[data-test="username"]').send_keys(username)
        self.driver.find_element_by_css_selector('[data-test="password"]').send_keys(password)
        self.driver.find_element_by_css_selector('.login-button').click()

    def get_title(self):
        return self.driver.title

    def get_header_text(self):
        return self.driver.find_element_by_id('header_container').text

    def is_login_error_visible(self):
        return self.driver.find_element_by_css_selector('.error-button').is_visible()

    def visit(self):
        self.driver.get('https://www.saucedemo.com')

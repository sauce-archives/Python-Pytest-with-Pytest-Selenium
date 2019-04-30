from selenium import webdriver

class SamplePage(object):
    
    def __init__(self, selenium):
        self.driver = selenium

    def login_as(self, username, password):
        self.driver.find_element_by_id('user-name').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_css_selector('.btn_action').click()

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_header_text(self):
        return self.driver.find_element_by_id('header_container').text

    def is_login_error_visible(self):
        return self.driver.find_element_by_css_selector('.error-button').is_displayed()

    def visit(self):
        self.driver.get('https://www.saucedemo.com')
    
class InventoryPage(object):
    
    def __init__(self, selenium):
        self.driver = selenium

    def add_item_to_cart(self):
        self.driver.find_element_by_css_selector('.btn_primary').click()

    def remove_item_from_cart(self):
        self.driver.find_element_by_css_selector('.btn_secondary').click()

    def get_items_in_cart(self):
        return self.driver.find_element_by_css_selector('.shopping_cart_badge').text
    
    def get_current_url(self):
        return self.driver.current_url

    def visit(self):
        self.driver.get('https://www.saucedemo.com/inventory.html')    

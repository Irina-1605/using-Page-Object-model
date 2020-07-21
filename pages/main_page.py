from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from pages.login_page import ProductPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def go_to_login_page(self):
        button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        button.click() 
        alert = self.browser.switch_to.alert
        alert.accept() 
        message_text_elt = self.browser.find_element_by_class(".alert.alert-safe.alert-noicon.alert-success.fade.in")
        message_text = message_text_elt.text

        assert "The shellcoder's handbook" == message_text

        price_text_elt = self.browser.find_element_by_class("p.price_color")
        price_text = price_text_elt.text

        assert "£9.99" == price_text

        
              

    
           

    
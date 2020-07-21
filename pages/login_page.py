from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in browser.current_url(), "Login is not present in current url"
        
    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login from is not presented"  
        
    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register from is not presented"
        
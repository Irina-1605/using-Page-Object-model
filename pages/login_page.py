from selenium.webdriver.common.by import By
from pages.base_page import BasePage
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
        assert self.is_element_present(*MainPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_field.send_keys(email)
        passworf_field = self.browser.find_element(*LoginPageLocators.PASSWORD)
        passworf_field.send_keys(password)
        confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        confirm_password_field.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        

        
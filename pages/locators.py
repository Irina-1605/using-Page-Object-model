from selenium.webdriver.common.by import By


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1") 
    BOOK_NAME_MATCHES_TEXT = (By.CSS_SELECTOR, "div.alertinner>strong:nth-child(1)")
    PRICE_TEXT = (By.CSS_SELECTOR, ".col-sm-6>p.price_color")
    PRICE_TEXT_MATCHES_TEXT = (By.CSS_SELECTOR, ".col-sm-6>p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner>strong:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "span>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    ITEMS_IN_BASKET = (By.CSS_SELECTOR, "h2.col-sm-6")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")    
    EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")	
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password2']")		
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")    


	



    
           

    
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


	



    
           

    
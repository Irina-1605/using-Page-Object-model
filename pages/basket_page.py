from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasePageLocators
from .locators import BasketPageLocators
from pages.base_page import BasePage
import time


class BasketPage(BasePage):
 
    def add_product_to_basket(self):
        time.sleep(5)
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()

    def should_not_be_items_in_basket(self):
        time.sleep(5)
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_BASKET), \
            "Items are presented, but should not be"

    def should_be_message_basket_is_empty(self):
        time.sleep(5)
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), \
            "Basket is not empty, but should be"

    def should_be_matched_book_name(self):
        book_name_text_elt = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
        book_name = book_name_text_elt.text
        book_name_message_text_elt = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MATCHES_TEXT)
        book_name_message_text = book_name_message_text_elt.text
        print(book_name)
        print(book_name_message_text)
        assert book_name == book_name_message_text

    def should_be_matched_price(self):
        price_text_elt = self.browser.find_element(*ProductPageLocators.PRICE_TEXT)
        price_text = price_text_elt.text
        price_text_matches_text_elt = self.browser.find_element(*ProductPageLocators.PRICE_TEXT_MATCHES_TEXT)
        price_text_matches_text = price_text_matches_text_elt.text
        print(price_text)
        print(price_text_matches_text)
        assert price_text == price_text_matches_text_elt.text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

              
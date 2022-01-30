from .base_page import BasePage
from locators import BasePageLocators


class BasketPage(BasePage):

    def go_to_basket_page(self):
        basket = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket.click()

    def should_be_empty_basket(self):
        assert not self.is_element_present(*BasePageLocators.EMPTY_BASKET), 'The basket is not empty'

    def should_be_msg_about_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.TEXT_EMPTY_BASKET), 'The text about empty basket is not found'
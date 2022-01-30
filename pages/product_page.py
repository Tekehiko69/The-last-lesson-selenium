from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def add_product_to_basket_te(self):
        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        add_btn.click()

    def add_product_to_basket(self):

        self.should_be_add_btn()
        self.should_be_name_of_product()
        self.should_be_price_of_product()

        add_btn = self.browser.find_element(*ProductPageLocators.ADD_BTN)
        add_btn.click()

        self.solve_quiz_and_get_code()
        time.sleep(10)
        self.should_be_msg_adding()
        self.compare_basket_and_price()


    def should_be_add_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BTN), 'Add button is not presented'

    def should_be_name_of_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Product name is not presented'

    def should_be_price_of_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_VALUE), 'Price value is not presented'

    def should_be_msg_adding(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        msg = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text

        assert product_name in msg, 'Product name is not on message'

    def compare_basket_and_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRICE_VALUE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_VALUE).text

        assert product_price == basket_price, 'Price and basket value is not equal'

    def not_should_be_msg_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), 'The success msg is not found (pre)'

    def not_should_be_msg_disappered(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), 'The success msg is not found (dis)'


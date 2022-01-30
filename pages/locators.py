from selenium.webdriver.common.by import By


class MainPageLocator():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REG_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ADD_BTN = (By.CSS_SELECTOR, '#add_to_basket_form')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRICE_VALUE = (By.CSS_SELECTOR, '.price_color:nth-child(2)')
    BASKET_VALUE = (By.CSS_SELECTOR, '.alertinner p strong')
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage


@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        self.product.delete()

    def test_guest_should_see_login_link_on_product_page(browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

#@pytest.mark.parametrize('link', [n if n != 7 else pytest.param(n, marks=pytest.mark.xfail) for n in range(10)])
#def test_guest_can_add_product_to_basket(browser, link):

    #link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'  # Измени потом на {link}
    #page = ProductPage(browser, link)
    #page.open()
    #page.add_product_to_basket()


#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket_te()
#    page.not_should_be_msg_element_present()
#
#def test_guest_cant_see_success_message(browser):
#
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
#    page = ProductPage(browser, link)
#    page.open()
#    page.not_should_be_msg_element_present()
#
#def test_message_dissappeeared_after_adding_product_to_basket(browser):
#
#    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_product_to_basket_te()
#    page.not_should_be_msg_disappered()


#def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#    link = 'https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
#    page = BasketPage(browser, link)
#    page.open()
#    page.go_to_basket_page()
#    page.should_be_empty_basket()
#    page.should_be_msg_about_empty_basket()
from .base_page import BasePage
from locators import MainPageLocator


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

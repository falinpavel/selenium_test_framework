import pytest
from config.data import Data
from pages.auth_page.auth_page import AuthPage
from pages.main_page.main_page import MainPage


class BaseTest:
    data: Data
    auth_page: AuthPage
    main_page: MainPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.data = Data()
        request.cls.auth_page = AuthPage(driver)
        request.cls.main_page = MainPage(driver)
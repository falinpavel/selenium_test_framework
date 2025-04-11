import pytest
from config.data import Data
from pages.auth_page.auth_page import AuthPage
from pages.home_page.home_page import HomePage


class BaseTest:
    data: Data
    auth_page: AuthPage
    home_page: HomePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.data = Data()
        request.cls.auth_page = AuthPage(driver)
        request.cls.home_page = HomePage(driver)
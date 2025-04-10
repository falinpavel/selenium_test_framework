import pytest
from config.data import Data
from pages.auth_page.auth_page import AuthPage


class BaseTest:
    data: Data
    auth_page: AuthPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.auth_page = AuthPage(driver)
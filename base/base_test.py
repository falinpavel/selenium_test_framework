import pytest
from config.data import Data


class BaseTest:

    data: Data

    # login_page: LoginPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        # request.cls.login_page = LoginPage(driver)
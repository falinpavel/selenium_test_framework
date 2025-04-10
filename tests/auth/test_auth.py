import pytest
import allure
from base.base_test import BaseTest


@allure.feature(f"Authorization on the site")
class TestAuth(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.ui
    @allure.title("Successful authorization with valid credentials")
    @allure.severity("blocker")
    @allure.story("Successful authorization")
    @allure.description("""
    Authorization with valid credentials, 
    for this test used valid email and password""")
    def test_successful_authorization(self):
        self.auth_page.open_page()
        self.auth_page.page_is_opened()
        self.auth_page.filling_credentials_fields(self.data.LOGIN, self.data.PASSWORD)
        self.auth_page.click_login()

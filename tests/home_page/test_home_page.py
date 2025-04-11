import pytest
import allure
from base.base_test import BaseTest


@allure.feature(f"Main page")
class TestHomePage(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.ui
    @allure.title("Check that home page")
    @allure.severity("major")
    @allure.story("Home page")
    @allure.description("Check that home page is opened, click on language dropdown and get all languages")
    def test_home_page_is_opened(self):
        self.home_page.open_page()
        self.home_page.page_is_opened()
        self.home_page.click_language_dropdown()
        self.home_page.get_all_languages()
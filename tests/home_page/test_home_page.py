import pytest
import allure
from base.base_test import BaseTest


@allure.feature(f"Home page")
class TestHomePage(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.ui
    @allure.title("Check home page header contains all languages")
    @allure.severity("major")
    @allure.story("Home page header")
    @allure.description("Check home page header contains all languages in dropdown, and click on it")
    def test_home_page_header(self):
        self.home_page.open_page()
        self.home_page.page_is_opened()
        self.home_page.click_language_dropdown()
        self.home_page.get_names_of_all_languages_buttons()
import pytest
import allure
from base.base_test import BaseTest


@allure.feature(f"Main page")
class TestMainPage(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.ui
    @allure.title("Check that main page")
    @allure.severity("major")
    @allure.story("Main page")
    @allure.description("Check that main page is opened, click on language dropdown and get all languages")
    def test_main_page_is_opened(self):
        self.main_page.open_page()
        self.main_page.page_is_opened()
        self.main_page.click_language_dropdown()
        self.main_page.get_all_languages()
import allure
from base.base_page import BasePage
from config.links import Links
import pages.main_page.main_locators as LOCATOR


class MainPage(BasePage):
    PAGE_URL = Links.MAIN_PAGE

    @allure.step("Click language dropdown")
    def click_language_dropdown(self):
        self.simple_click_to_element(*LOCATOR.LANGUAGE_DROPDOWN)

    @allure.step("Click language")
    def get_all_languages(self):
        self.get_all_attributes(*LOCATOR.LIST_OF_LANGUAGES)
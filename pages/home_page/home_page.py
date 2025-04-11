import allure
import pages.home_page.home_page_locators as LOCATOR
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from config.links import Links


class HomePage(BasePage):
    PAGE_URL = Links.HOME_PAGE

    @allure.step("Click language dropdown")
    def click_language_dropdown(self):
        self.simple_click_to_element(*LOCATOR.LANGUAGE_DROPDOWN)

    @allure.step("Click language and check names of all languages")
    def get_names_of_all_languages_buttons(self):
        self.wait.until(EC.element_to_be_clickable(LOCATOR.LANGUAGE_DROPDOWN))
        get_all_languages = self.find_elements(LOCATOR.LANGUAGE_DROPDOWN, LOCATOR.LIST_OF_LANGUAGES)
        languages: set = set()
        for language in get_all_languages:
            languages.add(language.text)
        expected_languages = {
            'Germany', 'French', 'Russian',
            'Turkish', 'Chinese', 'English', 'Arabic'
        }
        assert expected_languages.issubset(languages), \
            f"Expected languages are not present. Expected: {expected_languages}, Got: {languages}"

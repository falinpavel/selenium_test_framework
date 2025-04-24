import allure
import pages.home_page.home_page_locators as LOCATOR
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from config.links import Links


class HomePage(BasePage):
    PAGE_URL = Links.HOME_PAGE

    @allure.step("Click language dropdown")
    def click_language_dropdown(self):
        self.simple_click_to_element(
            *LOCATOR.LANGUAGE_DROPDOWN
        )

    @allure.step("Click language dropdown and check names of all languages")
    def get_names_of_all_languages_buttons(self):
        language_dropdown = self.wait.until(
            EC.element_to_be_clickable(
                LOCATOR.LANGUAGE_DROPDOWN
            ))
        language_dropdown.click()
        expected_languages = {
            'Germany', 'French', 'Russian',
            'Turkish', 'Chinese', 'English', 'Arabic'
        }
        assert self.wait.until(
            EC.visibility_of_any_elements_located(LOCATOR.LIST_OF_LANGUAGES),
        )
        self.check_elements_are_present(
            LOCATOR.LANGUAGE_DROPDOWN,
            LOCATOR.LIST_OF_LANGUAGES,
            expected_languages
        )

    @allure.step("Get all languages links and click on all")
    def click_on_all_language_links(self):
        self.click_on_all_visible_elements(
            LOCATOR.LANGUAGE_DROPDOWN,
            LOCATOR.LIST_OF_LANGUAGES
        )

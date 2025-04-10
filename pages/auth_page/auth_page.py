import allure
from base.base_page import BasePage
from config.links import Links
import pages.auth_page.auth_locators as LOCATOR
from selenium.webdriver.support import expected_conditions as EC


class AuthPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    def filling_credentials_fields(self, login: str, password: str):
        with allure.step("Clear username and password fields"):
            self.wait.until(EC.visibility_of_element_located(LOCATOR.USERNAME_FIELD)).clear()
            self.wait.until(EC.visibility_of_element_located(LOCATOR.PASSWORD_FIELD)).clear()
        with allure.step("Fill username and password fields"):
            self.wait.until(EC.element_to_be_clickable(LOCATOR.USERNAME_FIELD)).send_keys(login)
            self.wait.until(EC.element_to_be_clickable(LOCATOR.PASSWORD_FIELD)).send_keys(password)
        with allure.step("Check that username and password fields are filled"):
            assert (self.find(*LOCATOR.USERNAME_FIELD).get_attribute("value") == login
                    and self.find(*LOCATOR.PASSWORD_FIELD).get_attribute("value") == password)

    def click_login_button(self):
        with allure.step("Click login button"):
            self.click_base_button(*LOCATOR.LOGIN_BUTTON)
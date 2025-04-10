import allure
from base.base_page import BasePage
from config.links import Links
import pages.auth_page.auth_locators as LOCATOR


class AuthPage(BasePage):
    PAGE_URL = Links.LOGIN_PAGE

    @allure.step("Filling username and password fields")
    def filling_credentials_fields(self, login: str, password: str):
        with allure.step(f"Clear username and password fields, fill new login: {login}, password: {password}"):
            self.clear_and_send_keys(LOCATOR.USERNAME_FIELD, login)
            self.clear_and_send_keys(LOCATOR.PASSWORD_FIELD, password)

    @allure.step("Click login button")
    def click_login(self):
        with allure.step("Click login button"):
            self.simple_click_to_element(*LOCATOR.LOGIN_BUTTON)

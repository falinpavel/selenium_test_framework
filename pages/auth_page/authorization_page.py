import time
import allure
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AuthorizationPage(BasePage):
    PAGE_URL = "https://phptravels.net/"
    CUSTOMER_BUTTON = "//span[normalize-space()='Customer']"
    DRD_LOGIN_BUTTON = "//small[text()='Login']"
    USERNAME_FIELD = "//input[@id='email']"
    PASSWORD_FIELD = "//input[@id='password']"
    REMEMBER_ME_CHECKBOX = "//input[@id='rememberchb']"
    LOGIN_BUTTON = "//span[normalize-space()='Login']"

    def click_button(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.CUSTOMER_BUTTON))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.DRD_LOGIN_BUTTON))).click()
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from base.base_test import BaseTest


class TestAuthorization(BaseTest):

    @pytest.mark.usefixtures("driver")
    def test_unsuccessful_authorization(self):
        self.driver.get()
        # customer_button = self.driver.find_element(By.XPATH, "//span[normalize-space()='Customer']")
        # customer_button.click()
        # login_button = self.driver.find_element(By.XPATH, "//small[text()='Login']")
        # login_button.click()
        # email_field = self.driver.find_element(By.XPATH, "//input[@id='email']")
        # email_field.send_keys("j5lIY@example.com")
        # sleep(3)
        # password_field = self.driver.find_element(By.XPATH, "//input[@id='password']")
        # password_field.send_keys("password123123")
        # sleep(3)
        # # check_box_remember_me = self.driver.find_element(By.XPATH, "//input[@id='rememberchb']")
        # # check_box_remember_me.click()
        # login_button = self.driver.find_element(By.XPATH, "//span[normalize-space()='Login']")
        # login_button.click()
        # sleep(3)
        customer_button = self.EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Customer']"))
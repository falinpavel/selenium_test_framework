import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    PAGE_URL = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, 1)

    def open_page(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            if self.PAGE_URL:
                self.driver.get(self.PAGE_URL)
            else:
                raise ValueError("PAGE_URL is not defined")

    def page_is_opened(self):
        with allure.step(f"Check that {self.PAGE_URL} page is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def make_screenshot(self, screenshot_name: str):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def find(self, *locator: tuple):
        return self.driver.find_element(*locator)

    def click_base_button(self, *locator: tuple):
        self.find(*locator).click()
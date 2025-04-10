import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
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

    @allure.step("Find element")
    def find(self, *locator: tuple[str, str]):
        return self.driver.find_element(*locator)

    @allure.step("Click element")
    def simple_click_to_element(self, *locator: tuple[str, str]):
        self.find(*locator).click()

    @allure.step("Search field, clear and send keys new value")
    def clear_and_send_keys(self, locator: tuple[str, str], text: str):
        with allure.step("Clear field"):
            field = self.wait.until(EC.element_to_be_clickable(locator))
            field.clear()
            assert field.get_attribute("value") == ""
        with allure.step("Send keys"):
            field.send_keys(text)
            assert field.get_attribute("value") == text

    @allure.step("Get all attributes from element")
    def get_all_attributes(self, locator: tuple[str, str]):
        return self.find(*locator).get_attribute("class")
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

    @allure.step("Find one element")
    def find(self, *locator: tuple):
        return self.driver.find_element(*locator)

    @allure.step("Find all elements")
    def find_all(self, *locator: tuple):
        return self.driver.find_elements(*locator)

    @allure.step("Click element")
    def simple_click_to_element(self, *locator: tuple):
        with allure.step(f"Click element: {locator}"):
            self.find(*locator).click()

    @allure.step("Check element is visible")
    def check_element_is_visible(self, *locator: tuple):
        return self.wait.until(EC.visibility_of_element_located(*locator)).is_displayed()

    @allure.step("Search field, clear and send keys new value")
    def clear_field_and_send_keys(self, locator: tuple[str, str], text: str):
        with allure.step("Clear field"):
            field = self.wait.until(EC.element_to_be_clickable(locator))
            field.clear()
            assert field.get_attribute("value") == ""
        with allure.step(f"Send keys new value: {text}"):
            field.send_keys(text)
            assert field.get_attribute("value") == text

    @allure.step("Get all attributes from element (find elements into element)")
    def find_elements(self, locator: tuple, to_get_all_locator: tuple):
        parent_element = self.find(*locator)
        result = parent_element.find_elements(*to_get_all_locator)
        return result

    @allure.step("Check that all expected elements are present")
    def check_elements_are_present(self, parent_locator: tuple[str, str], child_locator: tuple, expected_texts: set):
        parent_element = self.wait.until(EC.visibility_of_element_located(parent_locator))
        actual_texts = set()
        for element in parent_element.find_elements(*child_locator):
            actual_texts.add(element.text)
        assert actual_texts | expected_texts

    @allure.step("Click on all visible elements")
    def click_on_all_visible_elements(self, parent_locator, child_locator):
        self.wait.until(EC.visibility_of_element_located(parent_locator))
        all_elements = self.find_elements(parent_locator, child_locator)
        for element in all_elements:
            if element.is_displayed():
                with allure.step(f"Click on element: {element.text}"):
                    self.simple_click_to_element(*element)

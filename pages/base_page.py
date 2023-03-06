from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    """This class is the parent for all pages,
    it contains all generics method and utilities"""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click(self, locator) -> None:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def find_element(self, locator) -> WebElement:
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).find_element(*locator)

    def find_elements(self, locator) -> list:
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).find_elements(*locator)

    def send_keys(self, locator, text: str) -> None:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self, locator, text: str) -> str:
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text).text

    def is_enabled(self, locator) -> bool:
        return bool(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)))

    def get_title(self, title: str) -> str:
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def open_page(self, url: str) -> None:
        self.driver.get(url)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_title(self) -> str:
        return self.driver.title

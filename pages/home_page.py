from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    CARD = (By.XPATH, "//h5[contains(text(), '{}')]/../../..")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def click_on_card(self, text: str) -> None:
        self.click((self.CARD[0], self.CARD[1].format(text)))


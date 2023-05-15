from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    """This is a class that contains selectors
     and methods related to the homepage         """

    CARD = (By.XPATH, "//h5[contains(text(), '{}')]/ancestor::div[contains(@class, 'top-card')]")
    CARD_BODY = (By.XPATH, "//h5")
    BANNER_IMAGE = (By.XPATH, "//img[@class='banner-image']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def get_cards_body_text(self, text: str) -> list:
        return [elem.text for elem in self.waiter_find_elements((self.CARD[0], self.CARD[1].format(text)))]

    def click_on_card(self, text: str) -> None:
        self.waiter_click((self.CARD[0], self.CARD[1].format(text)))

    def get_banner_image(self) -> WebElement:
        return self.waiter_find_element(self.BANNER_IMAGE)


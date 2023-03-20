import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage


class HomePageSteps:
    """This is a class that contains allure steps
        method with definition related to the homepage"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.home_page = HomePage(self.driver)

    @allure.step('Click homepage card {text}')
    def click_homepage_card(self, text: str) -> None:
        self.home_page.click_on_card(text)

    @allure.step('Get homepage cards body text')
    def get_homepage_cards_body_text(self) -> list:
        return self.home_page.get_cards_body_text("")

    @allure.step('Check that banner image displayed')
    def is_banner_image_displayed(self) -> None:
        assert self.home_page.get_banner_image().is_displayed() == True, "Banner image isn't displayed"

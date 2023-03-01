import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.home_page import HomePage


class HomePageSteps:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.home_page = HomePage(self.driver)

    @allure.step('Click homepage card {text}')
    def click_homepage_card(self, text: str) -> None:
        self.home_page.click_on_card(text)

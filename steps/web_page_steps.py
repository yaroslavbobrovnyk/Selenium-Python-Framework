import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class WebPageSteps:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_page = BasePage(self.driver)

    @allure.step('Open page with url={url}')
    def open_page(self, url: str) -> None:
        self.base_page.open_page(url)

    @allure.step('Get current url')
    def get_current_url(self) -> str:
        return self.base_page.get_current_url()




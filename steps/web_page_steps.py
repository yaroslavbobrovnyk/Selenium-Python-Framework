import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class WebPageSteps:
    """This is a class that contains allure steps
    method with definition related to the general actions"""

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_page = BasePage(self.driver)

    @allure.step('Open page with url={url}')
    def open_page(self, url: str) -> None:
        self.base_page.open_page(url)

    @allure.step('Get current url')
    def get_current_url(self) -> str:
        return self.base_page.get_current_url()

    @allure.step('Get page title')
    def get_page_title(self) -> str:
        return self.base_page.get_page_title()

    @allure.step('Switch to new open window')
    def switch_to_new_window(self) -> None:
        self.base_page.switch_to_window()

    @allure.step('Upload file')
    def file_upload(self, file_path: str, element: WebElement) -> None:
        element.send_keys(file_path)




import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.login_page import LoginPage


class LoginPageSteps:
    """This is a class that contains allure steps
        method with definition related to the homepage"""

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.login_page = LoginPage(self.driver)

    @allure.step('Login to the book store')
    def login(self, username: str, password: str) -> None:
        self.login_page.get_username_field().send_keys(username)
        self.login_page.get_password_field().send_keys(password)
        self.login_page.get_login_button().click()

    @allure.step('Check that profile wrapper is displayed')
    def is_profile_wrapper_displayed(self) -> None:
        print()
        assert self.login_page.get_profile_wrapper().is_displayed() == True


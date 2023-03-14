from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class LoginPage(BasePage):
    """This is a class that contains selectors
     and methods related to the login page"""

    LOGIN_BUTTON = (By.XPATH, "//button[@id='login']")
    REGISTER_BUTTON = (By.XPATH, "//button[@id='register']")
    NEW_USER_BUTTON = (By.XPATH, "//button[@id='newUser']")

    USERNAME_FIELD = (By.XPATH, "//input[@id='userName']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    FIRSTNAME_FIELD = (By.XPATH, "//input[@id='firstname']")
    LASTNAME_FIELD = (By.XPATH, "//input[@id='lastname']")

    PROFILE_WRAPPER = (By.XPATH, "//div[@class='profile-wrapper']")
    CAPTCHA_CHECKBOX = (By.XPATH, "//span[@id='recaptcha-anchor']")
    CAPTCHA_FRAME = (By.XPATH, "//form[@id='userForm']//iframe")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_username_field(self) -> WebElement:
        return self.waiter_find_element(self.USERNAME_FIELD)

    def get_password_field(self) -> WebElement:
        return self.waiter_find_element(self.PASSWORD_FIELD)

    def get_login_button(self) -> WebElement:
        return self.waiter_find_element(self.LOGIN_BUTTON)

    def get_new_user_button(self) -> WebElement:
        return self.waiter_find_element(self.NEW_USER_BUTTON)

    def get_register_button(self) -> WebElement:
        return self.waiter_find_element(self.NEW_USER_BUTTON)

    def get_firstname_field(self) -> WebElement:
        return self.waiter_find_element(self.FIRSTNAME_FIELD)

    def get_lastname_field(self) -> WebElement:
        return self.waiter_find_element(self.LASTNAME_FIELD)

    def get_profile_wrapper(self) -> WebElement:
        return self.waiter_find_element(self.PROFILE_WRAPPER)

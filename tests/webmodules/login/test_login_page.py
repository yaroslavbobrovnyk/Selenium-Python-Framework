import os

import allure
import pytest
from steps.login_page_steps import LoginPageSteps
from steps.web_page_steps import WebPageSteps
from tests.test_base import TestBase
from utils.constants import *


class TestLogin(TestBase):
    """This class a test class that contains
    test methods related to the login"""

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.web_page_steps = WebPageSteps(self.driver)
        self.login_steps = LoginPageSteps(self.driver)

        self.web_page_steps.open_page(os.getenv("BASE_URL") + "login")

    @allure.title("Check that user is logged in")
    def test_login(self):
        self.login_steps.login(USERNAME, PASSWORD)

        self.login_steps.is_profile_wrapper_displayed()

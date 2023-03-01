import allure
import pytest

from steps.assert_steps import AssertSteps
from steps.home_page_steps import HomePageSteps
from steps.web_page_steps import WebPageSteps
from tests.test_base import TestBase
from dotenv import load_dotenv
import os


class TestHomePage(TestBase):

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.web_page_steps = WebPageSteps(self.driver)

        load_dotenv("utils/env/.env.prod")

        self.web_page_steps.open_page(os.getenv("BASE_URL"))

    @allure.title("Check that homepage cards redirects to the correct url")
    @pytest.mark.parametrize("card_name, url_path",
                             [("Elements", "elements"),
                              ("Forms", "forms"),
                              ("Alerts, Frame & Windows", "alertsWindows"),
                              ("Widgets", "widgets"),
                              ("Interactions", "interaction"),
                              ("Book Store Application", "books")])
    def test_search_python(self, card_name: str, url_path: str):
        self.home_page_steps = HomePageSteps(self.driver)
        self.assert_steps = AssertSteps()

        self.home_page_steps.click_homepage_card(card_name)

        self.assert_steps.check_url_ends_with(self.web_page_steps.get_current_url(), url_path)


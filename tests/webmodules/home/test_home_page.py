import allure
import pytest

from steps.assert_steps import AssertSteps
from steps.home_page_steps import HomePageSteps
from steps.web_page_steps import WebPageSteps
from tests.test_base import TestBase
import os


class TestHomePage(TestBase):
    """This class a test class that contains
    test methods related to the homepage"""

    cards_list = [("Elements", "elements"), ("Forms", "forms"), ("Alerts, Frame & Windows", "alertsWindows"),
                  ("Widgets", "widgets"), ("Interactions", "interaction"), ("Book Store Application", "books")]

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.web_page_steps = WebPageSteps(self.driver)
        self.home_page_steps = HomePageSteps(self.driver)
        self.assert_steps = AssertSteps()

        self.web_page_steps.open_page(os.getenv("BASE_URL"))

    @allure.title("Check that title on the homepage is correct")
    def test_homepage_title(self):
        expected_title: str = "DEMOQA"
        self.assert_steps.check_strings_equals(self.web_page_steps.get_page_title(), expected_title)

    @allure.title("Check that banner image is displayed on the homepage")
    def test_banner_image(self):
        self.home_page_steps.is_banner_image_displayed()

    @allure.title("Check that all homepage cards is displayed on homepage")
    def test_homepage_cards_displayed(self):
        homepage_cards: list = self.home_page_steps.get_homepage_cards_body_text()

        expected_cards_list = [card[0] for card in self.cards_list]

        self.assert_steps.check_lists_equals(homepage_cards, expected_cards_list)

    @allure.title("Check that homepage cards redirects to the correct url")
    @pytest.mark.parametrize("card_name, url_path", cards_list)
    def test_homepage_cards_redirection(self, card_name: str, url_path: str):
        self.home_page_steps = HomePageSteps(self.driver)

        self.home_page_steps.click_homepage_card(card_name)

        self.assert_steps.check_url_ends_with(self.web_page_steps.get_current_url(), url_path)

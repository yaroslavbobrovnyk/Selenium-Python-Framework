import os

import allure
import pytest

from steps.assert_steps import AssertSteps
from steps.nav_bar_steps.elements_steps import ElementsSteps
from steps.web_page_steps import WebPageSteps
from tests.test_base import TestBase
from utils.enums.nav_bar_items import *
from utils.constants import USERNAME, EMAIL, ADDRESS, PERMANENT_ADDRESS


class TestElements(TestBase):
    """This class a test class that contains
        test methods related to the elements module"""

    @pytest.fixture(autouse=True)
    def set_up(self):
        self.web_page_steps = WebPageSteps(self.driver)
        self.elements_steps = ElementsSteps(self.driver)
        self.assert_steps = AssertSteps()

        self.web_page_steps.open_page(os.getenv("BASE_URL") + "elements")

    @allure.title("Check that nav_bar title is displayed")
    def test_title(self):
        expected_title = "Please select an item from left to start practice."

        actual_title = self.elements_steps.get_elements_title()

        self.elements_steps.check_elements_title(expected_title, actual_title)

    @allure.title("Check text box module can be filled and submitted")
    def test_text_box(self):
        self.elements_steps.click_item_button(NavBarItems.TEXT_BOX.value)
        self.elements_steps.fill_text_box(USERNAME, EMAIL, ADDRESS, PERMANENT_ADDRESS)
        self.elements_steps.click_submit_button()

        expected_output_string = f"Name:{USERNAME}\nEmail:{EMAIL}\n" \
                                 f"Current Address :{ADDRESS}\nPermananet Address :{PERMANENT_ADDRESS}"
        actual_result_string = self.elements_steps.get_output()

        self.elements_steps.check_result(expected_output_string, actual_result_string)

    @allure.title("Check check box can be clicked")
    def test_check_box(self):
        checkbox_item = "Home"

        self.elements_steps.click_item_button(NavBarItems.CHECK_BOX.value)
        self.elements_steps.click_checkbox(checkbox_item)

        actual_result_string = self.elements_steps.get_result()

        self.elements_steps.check_result(checkbox_item.lower(), actual_result_string)

    @allure.title("Check radio button can be selected")
    def test_radio_button(self):
        radio_button = "Impressive"

        self.elements_steps.click_item_button(NavBarItems.RADIO_BUTTON.value)
        self.elements_steps.click_radio_button(radio_button)

        radio_button_message = self.elements_steps.get_radio_button_message()

        self.elements_steps.check_result(radio_button, radio_button_message)

    @allure.title("Check table row can be deleted")
    def test_table_row_delete(self):
        self.elements_steps.click_item_button(NavBarItems.WEB_TABLES.value)

        table_row_text_before_delete: str = self.elements_steps.get_table_row_text()

        self.elements_steps.delete_table_row()

        table_row_text_after_delete: str = self.elements_steps.get_table_row_text()

        self.assert_steps.check_strings_not_equals(table_row_text_before_delete, table_row_text_after_delete)

    @allure.title("Check double click button")
    def test_double_click_button(self):
        self.elements_steps.click_item_button(NavBarItems.BUTTONS.value)

        self.elements_steps.double_click_button()

        expected_title = "You have done a double click"

        actual_title = self.elements_steps.get_elements_title()

        self.elements_steps.check_elements_title(expected_title, actual_title)




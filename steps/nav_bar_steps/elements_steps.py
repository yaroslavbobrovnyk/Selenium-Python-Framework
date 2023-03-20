import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver

from pages.nav_bar.elements_page import ElementsPage


class ElementsSteps:
    """This is a class that contains allure steps method with
    definition related to the elements module from the nav bar"""

    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver
        self.elements_page = ElementsPage(self.driver)

    @allure.step('Click on the item={item} button')
    def click_item_button(self, item: str) -> None:
        self.elements_page.get_item(item).click()

    @allure.step('Fill the text box with username, email, current address and permanent address')
    def fill_text_box(self, username: str, email: str, address: str, permanent_address: str) -> None:
        self.elements_page.fill_input("userName", username)
        self.elements_page.fill_input("userEmail", email)
        self.elements_page.fill_input("currentAddress", address)
        self.elements_page.fill_input("permanentAddress", permanent_address)

    @allure.step('Click on the submit button')
    def click_submit_button(self) -> None:
        self.elements_page.get_submit_button().click()

    @allure.step('Click on the checkbox item={item}')
    def click_checkbox(self, item: str) -> None:
        self.elements_page.get_checkbox_item(item).click()

    @allure.step('Click on the radio button item={item}')
    def click_radio_button(self, item: str) -> None:
        self.elements_page.get_radio_button(item).click()

    @allure.step('Delete table row')
    def delete_table_row(self) -> None:
        self.elements_page.get_table_row_delete_button().click()

    @allure.step('Double click on button')
    def double_click_button(self) -> None:
        action = ActionChains(self.driver)

        double_click_button = self.elements_page.get_double_click_button()

        action.double_click(double_click_button)

        action.perform()

    @allure.step('Get output')
    def get_output(self) -> str:
        return self.elements_page.get_output()

    @allure.step('Get elements title')
    def get_elements_title(self) -> str:
        return self.elements_page.get_elements_title()

    @allure.step('Get result')
    def get_result(self) -> str:
        return self.elements_page.get_result()

    @allure.step('Get table row text')
    def get_table_row_text(self) -> str:
        return self.elements_page.get_table_row().text

    @allure.step('Get radio button message')
    def get_radio_button_message(self) -> str:
        return self.elements_page.get_radio_button_message()

    @allure.step('Check that title text={expected} is displayed')
    def check_elements_title(self, expected: str, actual: str) -> None:
        assert expected in actual, \
            f"Title text={actual} doesn't equal expected title text={expected}"

    @allure.step('Check the actual result field={actual_result} contains string={expected_result_string}')
    def check_result(self, expected_result_string: str, actual_result: str) -> None:
        assert expected_result_string in actual_result, \
            f"Result={actual_result} doesn't contains expected result ={expected_result_string}"

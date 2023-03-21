from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class ElementsPage(BasePage):
    """This is a class that contains selectors and methods
    related to the elements module from the nav bar"""

    ELEMENTS_TITLE = (By.XPATH, "//div[contains(@class, 'col-md-6')]")
    INPUT_FIELD = (By.XPATH, "//*[@id='{}']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
    ELEMENTS_ITEM = (By.XPATH, "//span[contains(text(), '{}')]//parent::li")
    OUTPUT =(By.XPATH, "//div[@id='output']")
    RESULT = (By.XPATH, "//div[@id='result']")
    CHECKBOX_ITEM = (By.XPATH, "//span[contains(text(), '{}')]/parent::label")
    RADIO_BUTTON = (By.XPATH, "//label[contains(text(), '{}')]//parent::div")
    RADIO_BUTTON_MESSAGE = (By.XPATH, "//p[@class='mt-3']")
    TABLE_ROW = (By.XPATH, "//div[@class='rt-tr-group']")
    TABLE_DELETE_BUTTON =(By.XPATH, "//span[@title='Delete']")
    DOUBLE_CLICK_BUTTON = (By.XPATH, "//button[@id='doubleClickBtn']")
    LINK = (By.XPATH, "//div[@id='linkWrapper']//a[.='{}']")
    FILE_UPLOAD =(By.XPATH, "//input[@id='uploadFile']")
    UPLOAD_MESSAGE = (By.XPATH, "//p[@id='uploadedFilePath']")

    def __init__(self, driver: WebDriver) -> None:
        super().__init__(driver)

    def get_elements_title(self) -> str:
        return self.waiter_find_element(self.ELEMENTS_TITLE).text

    def fill_input(self, field_id: str, text: str) -> None:
        self.waiter_send_keys((self.INPUT_FIELD[0], self.INPUT_FIELD[1].format(field_id)), text)

    def get_submit_button(self) -> WebElement:
        return self.waiter_find_element(self.SUBMIT_BUTTON)

    def get_item(self, item: str) -> WebElement:
        return self.waiter_find_element((self.ELEMENTS_ITEM[0], self.ELEMENTS_ITEM[1].format(item)))

    def get_link(self, item: str) -> WebElement:
        return self.waiter_find_element((self.LINK[0], self.LINK[1].format(item)))

    def get_checkbox_item(self, item: str) -> WebElement:
        return self.waiter_find_element((self.CHECKBOX_ITEM[0], self.CHECKBOX_ITEM[1].format(item)))

    def get_radio_button(self, item: str) -> WebElement:
        return self.waiter_find_element((self.RADIO_BUTTON[0], self.RADIO_BUTTON[1].format(item)))

    def get_radio_button_message(self) -> str:
        return self.waiter_find_element(self.RADIO_BUTTON_MESSAGE).text

    def get_upload_button_message(self) -> str:
        return self.waiter_find_element(self.UPLOAD_MESSAGE).text

    def get_output(self) -> str:
        return self.waiter_find_element(self.OUTPUT).text

    def get_result(self) -> str:
        return self.waiter_find_element(self.RESULT).text

    def get_table_row(self) -> WebElement:
        return self.waiter_find_element(self.TABLE_ROW)

    def get_table_row_delete_button(self) -> WebElement:
        return self.get_table_row().find_element(*self.TABLE_DELETE_BUTTON)

    def get_double_click_button(self) -> WebElement:
        return self.waiter_find_element(self.DOUBLE_CLICK_BUTTON)

    def get_file_upload(self) -> WebElement:
        return self.waiter_find_element(self.FILE_UPLOAD)
import pytest
from utils.driver import get_driver, quit_driver
from selenium.webdriver.remote.webdriver import WebDriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="get browser name"
    )


@pytest.fixture(scope="class")
def init_driver(request):
    browser: str = request.config.getoption("--browser")
    driver: WebDriver = get_driver(browser)
    request.cls.driver = driver
    yield
    quit_driver(driver)

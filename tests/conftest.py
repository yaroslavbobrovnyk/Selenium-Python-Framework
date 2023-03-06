import pytest
from dotenv import load_dotenv

from utils.driver import get_driver, quit_driver
from selenium.webdriver.remote.webdriver import WebDriver


"""This is a class that contains pytest fixtures for tests"""


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="get browser name")
    parser.addoption("--env", action="store", default="prod", help="get environment variable")


@pytest.fixture(scope="class")
def init_driver(request):
    browser: str = request.config.getoption("--browser")
    driver: WebDriver = get_driver(browser)
    request.cls.driver = driver
    yield
    quit_driver(driver)


@pytest.fixture(scope="class")
def get_env(request):
    env: str = request.config.getoption("--env")
    load_dotenv("utils/env/.env.{}".format(env))

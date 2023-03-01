from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


def get_driver(browser: str) -> WebDriver:
    """
    Returns a new instance of the WebDriver.
    """

    def chrome_driver_setup(headless: bool):
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-infobars")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-browser-side-navigation")

        if headless:
            chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()

        return driver

    if browser == "chrome":
        return chrome_driver_setup(False)
    elif browser == "firefox":
        raise NotImplementedError
    elif browser == "headless":
        return chrome_driver_setup(True)
    else:
        return chrome_driver_setup(False)


def quit_driver(driver: WebDriver) -> None:
    """
    Quits the given WebDriver instance.
    """
    driver.quit()

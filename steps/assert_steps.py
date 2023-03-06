import allure


class AssertSteps:
    """This is a class that contains allure steps
    method with definition related to the assertions"""

    @allure.step('Check that url="{url}" ends with string="{text}"')
    def check_url_ends_with(self, url: str, text: str) -> None:
        assert url.endswith(text), f"Actual url={url} doesn't ends with string={text}"

    @allure.step('Check that string="{actual_string}" equals to string="{expected_string}"')
    def check_strings_equals(self, actual_string: str, expected_string: str) -> None:
        assert actual_string == expected_string, \
            f"Actual string={actual_string} doesn't equal to expected string={expected_string}"

    @allure.step('Check that url="{url}" ends with string="{text}"')
    def check_url_ends_with(self, url: str, text: str) -> None:
        assert url.endswith(text), f"Actual url={url} doesn't ends with string={text}"

    @allure.step('Check that list="{actual_list}" equals to list="{expected_list}"')
    def check_lists_equals(self, actual_list: list, expected_list: list) -> None:
        assert actual_list == expected_list, \
            f"Actual list={actual_list} doesn't equal to expected list={expected_list}"

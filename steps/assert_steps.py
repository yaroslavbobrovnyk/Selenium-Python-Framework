import allure


class AssertSteps:

    @allure.step('Check that url="{url}" ends with string="{text}"')
    def check_url_ends_with(self, url: str, text: str) -> None:
        assert url.endswith(text), f"Actual url={url} doesn't ends with string={text}"

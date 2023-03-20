import pytest


@pytest.mark.usefixtures("get_env")
class TestBase:
    """This class is the parent for all test classes,
    it uses driver initialization and environment setup fixtures"""
    pass

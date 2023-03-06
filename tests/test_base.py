import pytest


@pytest.mark.usefixtures("init_driver", "get_env")
class TestBase:
    """This class is the parent for all test classes,
    it uses driver initialization and environment setup fixtures"""
    pass

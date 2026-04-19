import pytest


@pytest.fixture(scope="module")
def prework():
    print("prework run at common")
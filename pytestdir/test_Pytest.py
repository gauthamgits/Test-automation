import pytest




@pytest.fixture(scope="function")
def prework():
    print("prework run")




@pytest.fixture(scope="function")
def secondprework():
    print("prework run second")
    yield
    print("yielded run after the config second")



def test_initalcheck1(prework, secondprework):
    print("test run")
@pytest.mark.skip
def test_initalcheck11(prework, secondprework):
    print("test run2")
@pytest.mark.smoke
def test_initalcheck111(prework,secondprework):
    print("test run3")
    assert secondprework=="pass"
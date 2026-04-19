import pytest
from cv2.version import headless


@pytest.fixture(scope="session")
def user_credentials(request):
    return request.params

#this is to tell what is the parameters that you are passing through the parameters while running the test.
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")


@pytest.fixture
def browserInstance(playwright, request):

    browser_name=request.config.getoption("browser_name")
    if browser_name.lower() == "chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name.lower() == "firefox":
        browser = playwright.firefox.launch(headless=False)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()


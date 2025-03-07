from urllib import request
import toml
from drivers.webdrivers import webdrivers
from _pytest.nodes import Item
import pytest


drivers = ("chrome", "firefox", "chrome_headless", "remote")


def pytest_addoption(parser):
    parser.addoption(
        "--driver",
        action="store",
        choices=drivers,
        default="chrome",
        help="specify the driver to run the test"
    )
    

def pytest_runtest_setup(item:Item)->None:
    """
    Pytest fixture for setting up a WebDriver instance before each test.
    Reads configuration from `pyproject.toml` and initializes the driver.
    """
    try:
        config = toml.load("pyproject.toml") #load the the toml file 
        base_url = config.get("tool", {}).get("myapp", {}).get("base_url", "default_url")  # Get the base url from the toml file 
    except FileNotFoundError:
        print("Warning: pyproject.toml not found, using default URL")
        base_url = "default_url"
    except toml.TomlDecodeError:
        print("Warning: pyproject.toml is invalid, using default URL")
        base_url = "default_url"

    browser = item.config.getoption("--driver") 
    print(f"Running test in browser: {browser}")

    webdriver_instance=webdrivers()
    try:
        webdriver_instance.start_browser(browser=browser)
        driver = webdriver_instance._browser
        driver.get(base_url)
    except Exception as e:
        pytest.skip(f"Failed to initialize WebDriver: {e}")

    # Attach driver to the test class if it exists
    if item.cls is not None:
        item.cls.driver = driver
    else:
        # For function-based tests, attach to item (less common)
        item.driver = driver

# # Cleanup in a teardown hook
# def pytest_runtest_teardown(item: Item) -> None:
#     if hasattr(item, "driver"):
#         try:
#             item.driver.quit()
#         except Exception as e:
#             print(f"Warning: Failed to quit driver: {e}")
#     elif item.cls and hasattr(item.cls, "driver"):
#         try:
#             item.cls.driver.quit()
#         except Exception as e:
#             print(f"Warning: Failed to quit driver: {e}")


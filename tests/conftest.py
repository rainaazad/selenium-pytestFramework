import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

driver = None
# driver_app = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        # driver_app = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        # driver_app = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "IE":
        driver = webdriver.Ie(IEDriverManager().install())
        # driver_app = webdriver.Ie(IEDriverManager().install())
    driver.maximize_window()
    # driver_app.maximize_window()
    # driver_app.get("https://www.saucedemo.com/")

    driver.get("https://matr3-dev-ed.lightning.force.com/lightning/setup/SetupOneHome/home")

    request.cls.driver = driver  # return driver
    # request.cls.driver_app = driver_app
    yield  # as yield statement and return statement does not work together , so we will use request.cls.driver
    driver.close()
    # driver_app.close()


# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#     Extends the Pytest Plugin to take and embed screenshot in html report,whenever test fails.
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == "call" or report.when == "setup":
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#     driver.get_screenshot_as_file(name)

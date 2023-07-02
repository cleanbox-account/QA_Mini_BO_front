# ----------------------------------------------------------------------------
# Created By  : Edi Tchaevsky
# Created Date: 2022.12.27
# version ='1.0'
# ---------------------------------------------------------------------------
"""  pytest configuration , driver initializion in setup for classes , screenshoter """
# ---------------------------------------------------------------------------
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import Data.pages_addresses as env
import os
import shutil
driver = None

@pytest.fixture(scope="class")
def setup(request):
    mini_bo_url = env.mini_bo_url
    global driver
    # browser_name = request.config.getoption("browser_name")
    # try to detect another drivers and close them
    print("FIND AND CLOSE DRIVER BEFORE INITIALIZE")

    options = webdriver.ChromeOptions()
    # service = Service("chromedriver.exe")
    # options.headless=True
    options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--incognito")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(service=service, options=options)
    driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()) )
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get(mini_bo_url)
    driver.maximize_window()
    # print("URL and Session ID")
    # print(driver.current_url)
    # print(driver.session_id)

    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.mark.hookwrapper  # for html report with screenshots
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

    sourcepath = env.sourcepath

    sourcefiles = os.listdir(sourcepath)
    destinationpath = env.destinationpath

    for file in sourcefiles:
        if file.endswith('.png'):
            shutil.move(os.path.join(sourcepath, file),
                        os.path.join(destinationpath, file))


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

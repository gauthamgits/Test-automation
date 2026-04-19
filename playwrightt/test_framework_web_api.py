import json
import re
import time


import pytest
from cv2.version import headless
from playwright.sync_api import Page, expect, Playwright

from pageObjects.dashboardPage import DashBoardPage
from utils.apiBaseframework import apiutils
from pageObjects.loginPage import LoginPage


from pathlib import Path
import json

DATA_FILE = Path(__file__).resolve().parent / "Data" / "credentials.json"

with open(DATA_FILE) as f:
    test_data = json.load(f)
    test_cred_list = test_data["credentials"]

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials',test_cred_list)
def test_e2e_web_api(playwright:Playwright,browserInstance,user_credentials):

    api_utils=apiutils()
    orderid=api_utils.creatOrder(playwright,user_credentials)

    loginobject = LoginPage(browserInstance)
    loginobject.navigate()
    dashboardObject=loginobject.login(user_credentials)
    orderhistorypageobject=dashboardObject.gotoOrderspage()
    orderDetailsobject=orderhistorypageobject.gotoorderdetails(orderid)
    orderDetailsobject.verifyorderdetails()


from playwright.sync_api import Page

from playwrightt.pageObjects.dashboardPage import DashBoardPage


class LoginPage:

    def __init__(self, page):
        self.page=page

    def navigate(self):
        self.page.goto("https:///rahulshettyacademy.com/client")


    def login(self, user_credentials):
        useremail=user_credentials["userEmail"]
        userpassword=user_credentials["userPassword"]
        self.page.get_by_placeholder("email@example.com").fill(useremail)
        self.page.get_by_placeholder("enter your passsword").fill(userpassword)
        self.page.get_by_role("button", name="login").click()
        dashboardobject=DashBoardPage(self.page)
        return dashboardobject
from playwrightt.pageObjects.orderHistoryPage import OrderHistoryPage


class DashBoardPage:

    def __init__(self,page):
        self.page=page

    def gotoOrderspage(self):
        self.page.get_by_role("button", name="  ORDERS").click()
        orderhistoryobject=OrderHistoryPage(self.page)
        return orderhistoryobject
from playwrightt.pageObjects.orderDetailsPage import OrderDetailPage


class OrderHistoryPage:

    def __init__(self,page):
        self.page=page

    def gotoorderdetails(self,orderid):
        row = self.page.locator("tr").filter(has_text=orderid)
        row.get_by_role("button", name="View").click()
        orderdetailsobject=OrderDetailPage(self.page)
        return orderdetailsobject
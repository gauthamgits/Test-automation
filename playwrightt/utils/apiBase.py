from playwright.sync_api import Playwright

from playwrightt.conftest import user_credentials

ordersPayload ={"orders":[{"country":"India","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}
class apiutils:

    def gettoken(self, playwright:Playwright):
        #useremail=user_credentials["userEmail"]
        #userpassword=user_credentials["userPassword"]
        api_request_context = playwright.request.new_context(base_url="https:///rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"})
        assert response.ok
        responseBody=response.json()
        return responseBody["token"]

    def creatOrder(self, playwright:Playwright, user_credentials):
        token= self.gettoken(playwright)
        api_request_context=playwright.request.new_context(base_url="https:///rahulshettyacademy.com")
        response=api_request_context.post("/api/ecom/order/create-order",
                                 data=ordersPayload,
                                 headers={"Authorization":token,
                                          "Content-Type":"application/json"})
        responseJson=response.json()
        orderId= responseJson["orders"][0]
        print(orderId)
        return orderId
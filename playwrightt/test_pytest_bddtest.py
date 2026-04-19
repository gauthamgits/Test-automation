import pytest
from pytest_bdd import given, when, then, parsers, scenarios

from wrapt import when_imported


from playwrightt.pageObjects.loginPage import LoginPage
from playwrightt.utils.apiBaseframework import apiutils

scenarios('features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return{}

@given(parsers.parse('the user has placed an order with {username} and {password}'))
def place_order(playwright,username,password,shared_data):
    user_credentials={'userEmail' : username, 'userPassword' : password}
    api_utils = apiutils()
    orderid = api_utils.creatOrder(playwright, user_credentials)
    shared_data['orderid']=orderid

@given('the user is on landing page')
def user_on_landingpage(playwright,browserInstance,shared_data):
    loginobject = LoginPage(browserInstance)
    loginobject.navigate()
    shared_data['loginpage']=loginobject

@when(parsers.parse('i login to the portal with {username} and {password}'))
def logintopage(username,password,shared_data):
    user_credentials={'userEmail' : username, 'userPassword' : password}
    loginobject=shared_data['loginpage']
    dashboardObject = loginobject.login(user_credentials)
    shared_data['dashboardobject']=dashboardObject

@when('navigate to the orders page')
def navigate_to_order(shared_data):
    dashboardObject=shared_data['dashboardobject']
    orderhistorypageobject = dashboardObject.gotoOrderspage()
    shared_data['orderhistorypageobject']=orderhistorypageobject

@when('select the orderid')
def select_orderid(shared_data):
    orderhistorypageobject=shared_data['orderhistorypageobject']
    orderDetailsobject=orderhistorypageobject.gotoorderdetails(shared_data['orderid'])
    shared_data['oderdetailsobject']=orderDetailsobject

@then('order message is successfully displayed')
def check_order_message(shared_data):
    orderdetailsobject=shared_data['oderdetailsobject']
    orderdetailsobject.verifyorderdetails()






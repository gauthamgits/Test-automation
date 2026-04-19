import re
import time
from pydoc import pager

import pytest
from cv2.version import headless
from playwright.sync_api import Page, expect, Playwright
from utils.apiBase import apiutils


def test_playwrightbasics(playwright):
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.goto("https://rahulshettyacademy.com")

#default uses chromium headless mode.
def test_playwrightshortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_corelocations(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2)")
    page.get_by_role("combobox").select_option("teach")
    #page.get_by_role("checkbox", name="terms").click()
    page.locator("#terms").check() # #terms is css based on id and .class is the css based on class.
    page.get_by_role("button", name="Sign In").click()

def test_incorrectcreds(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@83srs0$3mK2)")
    page.get_by_role("combobox").select_option("teach")
    #page.get_by_role("checkbox", name="terms").click()
    page.locator("#terms").check() # #terms is css based on id and .class is the css based on class.
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

def test_filtration(page:Page):
    page.goto("https://rahulshettyacademy.com/angularpractice/shop", wait_until="domcontentloaded")
    samsungphone=page.locator("app-card").filter(has_text="Samsung Note 8")
    samsungphone.get_by_role("button", name="Add ").click()
    nokiaphone=page.locator("app-card").filter(has_text="Nokia Edge")
    nokiaphone.get_by_role("button", name="Add ").click()
    page.get_by_text(" Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)
    expect(page.locator(".media-heading").filter(has_text="Samsung Note 8")).to_have_text("Samsung Note 8")
    expect(page.locator(".media-heading").filter(has_text="Nokia Edge")).to_have_text("Nokia Edge")

    time.sleep(5)

def test_childwindow(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as newpage_info:
        page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()
        childpage = newpage_info.value
        texcontent=childpage.locator(".red").text_content()
        print(texcontent)
        emailmatch = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', texcontent)
        if emailmatch:
            print(emailmatch.group())
            assert emailmatch.group() == "mentor@rahulshettyacademy.com"


def test_moreunitest(page:Page):
    #how to handle alerts
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()
    time.sleep(4)

    #page.locator("#mousehover").hover().

    #Frames handling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("Link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")

def test_seletest(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            colvalue=index
            print(f'index values i {colvalue}')
            break

    ricerow = page.locator("tr").filter(has_text="Rice")
    riceprice=ricerow.locator("td").nth(colvalue).text_content()
    print(f'rice price is {riceprice}')

def test_e2e_web_api(playwright:Playwright):
    browser= playwright.chromium.launch()
    context=browser.new_context()
    page=context.new_page()

    api_utils=apiutils()
    orderid=api_utils.creatOrder(playwright)

    page.goto("https:///rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="  ORDERS").click()
    row=page.locator("tr").filter(has_text=orderid)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    print("done done done")

fakepayloadorderresponse={"data": [], "message": "No Orders"}
def intercept_response(route):
    route.fulfill(
        json = fakepayloadorderresponse
    )

def test_network_intercept_reponse(page:Page):

    page.goto("https:///rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="  ORDERS").click()
    ordertext=page.locator(".mt-4").text_content()
    print(ordertext)



def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

@pytest.mark.smoke
def test_network_intercept_request(page:Page):

    page.goto("https:///rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="login").click()
    page.get_by_role("button", name="  ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    text=page.locator(".blink_me").text_content()
    print(text)


def test_session_storage(playwright:Playwright):
    api_utils=apiutils()
    token=api_utils.gettoken(playwright)
    browser=playwright.chromium.launch(headless=True)
    context=browser.new_context()
    page=context.new_page()
    #inject token to local storage
    page.add_init_script(f"""localStorage.setItem('token':'{token}')""")
    page.goto("https:///rahulshettyacademy.com/client")
    page.get_by_role("button", name="  ORDERS").click()
    expect(page.get_by_text('Your Orders')).to_be_visible()





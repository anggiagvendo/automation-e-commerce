import pytest 
from playwright.sync_api import Page, expect

def test_click_testcase(page : Page):
    page.goto("https://www.automationexercise.com/",timeout=60000)
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_text("New User Signup!")).to_be_visible
    page.get_by_role("textbox", name="Name").fill("Anggi")
    page.locator("form").filter(has_text= "Signup").get_by_placeholder("Email Address").fill("anggi1@anggi.com")
    page.get_by_role("button", name="Signup").click()
    expect(page.get_by_text("Enter Account Information")).to_be_visible
    page.get_by_text("Mr.").click()
    page.get_by_role("textbox", name="Password *").fill("123456")
    page.locator("#days").select_option("26")
    page.locator("#months").select_option("September")
    page.locator("#years").select_option("2003")
    page.get_by_role("checkbox", name="Sign up for our newsletter!").check()
    page.get_by_role("checkbox", name="Receive special offers from").check()
    page.get_by_role("textbox", name="First name *").fill("Auo")
    page.get_by_role("textbox", name="Last name *").fill("Iuo")
    page.get_by_role("textbox", name="Company", exact=True).fill("Independent")
    page.get_by_role("textbox", name="Address * (Street address, P.").fill("Jl. Damai")
    page.get_by_role("textbox", name="Address 2").fill("RT 1")
    page.get_by_label("Country *").select_option("Canada")
    page.get_by_role("textbox", name="State").fill("Sleman")
    page.get_by_role("textbox", name="City * Zipcode *").fill("Yogyakarta")
    page.locator("#zipcode").fill("223444")
    page.get_by_role("textbox", name="Mobile Number *").fill("01239021848")
    page.get_by_role("button", name="Create Account").click()
    expect(page.get_by_text("Account Created!")).to_be_visible
    page.get_by_role("link", name="Continue").click()
    page.get_by_text("Logged in as Anggi").click()
    page.get_by_role("link", name="Delete Account").click()
    expect(page.get_by_text("Account Deleted!")).to_be_visible
    page.get_by_role("link", name="Continue").click()





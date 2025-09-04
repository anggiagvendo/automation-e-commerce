import pytest 
from playwright.sync_api import Page, expect

def test_click_testcase(page : Page):
    page.goto("https://www.automationexercise.com/",timeout=60000)
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Signup").click()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()
    page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address").fill("aaa@aaa.com")
    page.get_by_role("textbox", name="Password").fill("123456")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Your email or password is incorrect!")).to_be_visible()
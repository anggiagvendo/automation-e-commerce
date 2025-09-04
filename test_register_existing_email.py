import pytest
from playwright.sync_api import Page, expect

def test_register_existing_email (page: Page):
    page.goto("https://www.automationexercise.com/",timeout=60000)
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Signup / Login").click()
    expect(page.get_by_role("heading", name="New User Signup!")).to_be_visible()
    page.get_by_role("textbox", name="Name").fill("anggi")
    page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address").fill("anggi@anggi.com")
    page.get_by_role("button", name="Signup").click()
    expect(page.get_by_text("Email Address already exist!")).to_be_visible
              
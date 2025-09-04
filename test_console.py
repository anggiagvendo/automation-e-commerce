import pytest
from playwright.sync_api import Page, expect

def test_console(page:Page):
    ##page.goto("https://www.automationexercise.com/")
    ##expect(page).to_have_title("Automation Exercise")
    print("heheheee")
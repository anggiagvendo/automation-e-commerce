import pytest
from playwright.sync_api import Page, expect

def test_search_prodcut (page:Page):
    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    page.locator('xpath=//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a').click()
    expect(page).to_have_title("Automation Exercise - All Products")
    page.locator('xpath=//*[@id="search_product"]').fill("Blue Top")
    page.locator('xpath=//*[@id="submit_search"]').click()
    page.wait_for_timeout(5000)
    expect(page.get_by_text("Searched Products")).to_be_visible
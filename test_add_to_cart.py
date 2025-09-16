import pytest
from playwright.sync_api import Page, expect

def test_add_to_cart (page : Page):
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_title("Automation Exercise - All Products")
    page.locator('xpath=/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a').click()
    page.locator('xpath=//*[@id="cartModal"]/div/div/div[3]/button').click()
    page.locator('xpath=/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a').click()
    page.locator('xpath=//*[@id="cartModal"]/div/div/div[2]/p[2]/a').click()

    expect(page.locator('xpath=//*[@id="product-1"]')).to_be_visible()
    expect(page.locator('xpath=//*[@id="product-2"]')).to_be_visible()
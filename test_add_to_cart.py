import pytest
from playwright.sync_api import Page, expect

def test_add_to_cart (page : Page):
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_title("Automation Exercise - All Products")

    start_div = 2
    end_div = 5
    current_div = start_div
    count_div = 1
    count = end_div - start_div

    while current_div <= end_div:
        page.locator('xpath=/html/body/section[2]/div/div/div[2]/div/div['+str(current_div)+']/div/div[1]/div[1]/a').click()
        page.locator('xpath=//*[@id="cartModal"]/div/div/div[3]/button').click()
        current_div += 1
        
    page.get_by_role("link", name="Cart").click()

    while count_div <= end_div-1:
        expect(page.locator('xpath=//*[@id="product-'+str(count_div)+'"]')).to_be_visible()
        count_div += 1

    page.pause()
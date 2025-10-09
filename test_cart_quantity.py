import pytest
from playwright.sync_api import Page, expect

def test_cart_quantity (page:Page):

    ##open page - open product page
    page.goto("https://automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_title("Automation Exercise - All Products")

    ##repetition : add item to cart based on end_count
    start_count = 0
    end_count = 5

    while start_count < end_count:
        page.locator('xpath=/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a').click()
        page.locator('xpath=//*[@id="cartModal"]/div/div/div[3]/button').click()
        start_count += 1

    ##open cart page
    page.get_by_role("link", name="Cart").click()
    
    ##get quantity of items that has been added to cart
    quantity_count = page.locator('xpath=//*[@id="product-1"]/td[4]/button').inner_text()

    ##compare quantity based on real cart with declared on repetition
    assert int(quantity_count) == start_count, f"Quantity is wrong! quantity count is {quantity_count} and start count is {start_count}"
    print (f"quantity = {quantity_count}, start count = {start_count}")
    page.pause()
import pytest
from playwright.sync_api import Page, expect

def test_add_to_cart_complex(page: Page):
    page.goto("https://automationexercise.com/", timeout=60000)
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Products").click()
    expect(page).to_have_title("Automation Exercise - All Products")

    start_div = 2
    end_div = 5
    current_div = start_div

    # store product details here
    products_added = []

    # loop: add to cart + capture name & price
    while current_div <= end_div:
        product_name = page.locator(
            f'xpath=/html/body/section[2]/div/div/div[2]/div/div[{current_div}]/div/div[1]/div[1]/p'
        ).inner_text()

        product_price = page.locator(
            f'xpath=/html/body/section[2]/div/div/div[2]/div/div[{current_div}]/div/div[1]/div[1]/h2'
        ).inner_text()

        products_added.append({"name": product_name, "price": product_price})

        # click add-to-cart button
        page.locator(
            f'xpath=/html/body/section[2]/div/div/div[2]/div/div[{current_div}]/div/div[1]/div[1]/a'
        ).click()

        # close modal
        page.locator('xpath=//*[@id="cartModal"]/div/div/div[3]/button').click()

        current_div += 1

    # Go to cart
    page.get_by_role("link", name="Cart").click()

    # validate cart items against stored list
    for idx, product in enumerate(products_added, start=1):
        row = page.locator(f'//*[@id="product-{idx}"]')
        expect(row).to_be_visible()

        cart_name = row.locator("td.cart_description h4 a").inner_text()
        cart_price = row.locator("td.cart_price p").inner_text()

        assert product["name"] == cart_name, f"Expected {product['name']}, got {cart_name}"
        assert product["price"] == cart_price, f"Expected {product['price']}, got {cart_price}"

    page.pause()

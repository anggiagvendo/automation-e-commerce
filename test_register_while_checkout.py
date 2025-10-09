import pytest
from playwright.sync_api import Page, expect

def test_register_while_checkout(page:Page):
    ##Basic homepage
    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")

    ##Go to product page and add product into cart
    page.locator('xpath=//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a').click()
    expect(page).to_have_title("Automation Exercise - All Products")
    page.locator('xpath=/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a').click()
    page.locator('xpath=//*[@id="cartModal"]/div/div/div[3]/button').click()

    ##Go to cart page
    page.locator('xpath=//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a').click()
    expect(page).to_have_title("Automation Exercise - Checkout")

    ##Click proceed to checkout and trigger login/register pop-up
    page.locator('xpath=/html/body/section/div/section/div[1]/div/div/a').click()
    page.locator('xpath=//*[@id="checkoutModal"]/div/div/div[2]/p[2]/a').click()

    ##Start sign-up process

    register_name = "retut12344"
    first_name = "retut"
    last_name = "1234"
    email = "retut12344@retut.com"

    ##Sign-up process from front
    page.get_by_role("textbox", name="Name").fill(register_name)
    page.locator("form").filter(has_text= "Signup").get_by_placeholder("Email Address").fill(email)
    page.get_by_role("button", name="Signup").click()

    ##Registration form filling
    expect(page.get_by_text("Enter Account Information")).to_be_visible
    page.get_by_text("Mr.").click()
    page.get_by_role("textbox", name="Password *").fill("123456")
    page.locator("#days").select_option("26")
    page.locator("#months").select_option("September")
    page.locator("#years").select_option("2003")
    page.get_by_role("checkbox", name="Sign up for our newsletter!").check()
    page.get_by_role("checkbox", name="Receive special offers from").check()
    page.get_by_role("textbox", name="First name *").fill(first_name)
    page.get_by_role("textbox", name="Last name *").fill(last_name)
    page.get_by_role("textbox", name="Company", exact=True).fill("Independent")
    page.get_by_role("textbox", name="Address * (Street address, P.").fill("Jl. Damai")
    page.get_by_role("textbox", name="Address 2").fill("RT 1")
    page.get_by_label("Country *").select_option("Canada")
    page.get_by_role("textbox", name="State").fill("Sleman")
    page.get_by_role("textbox", name="City * Zipcode *").fill("Yogyakarta")
    page.locator("#zipcode").fill("223444")
    page.get_by_role("textbox", name="Mobile Number *").fill("01239021848")
    page.get_by_role("button", name="Create Account").click()

    ##Account is created and click continue
    expect(page.get_by_text("Account Created!")).to_be_visible
    page.locator('xpath=//*[@id="form"]/div/div/div/div/a').click()

    ##Detect username
    username_ui = page.locator('xpath=//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a').inner_text()
    username_ui = username_ui.replace("Logged in as", "").strip()
    assert username_ui == register_name, f"Different username, at UI : {username_ui} and at form : {register_name}"

    ##Go to cart page
    page.locator('xpath=//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a').click()
    expect(page).to_have_title("Automation Exercise - Checkout")

    ##Click proceed to checkout
    page.locator('xpath=/html/body/section/div/section/div[1]/div/div/a').click()

    ##Can compare address appear at UI and inserted form 

    ##Input comment and click place order
    page.locator('xpath=//*[@id="ordermsg"]/textarea').fill("This is comment content")
    page.locator('xpath=//*[@id="cart_items"]/div/div[7]/a').click()

    ##Input credit card information and click continue
    page.locator('xpath=//*[@id="payment-form"]/div[1]/div/input').fill("name cc")
    page.locator('xpath=//*[@id="payment-form"]/div[2]/div/input').fill("cc number")
    page.locator('xpath=//*[@id="payment-form"]/div[3]/div[1]/input').fill("111")
    page.locator('xpath=//*[@id="payment-form"]/div[3]/div[1]/input').fill("111")
    page.locator('xpath=//*[@id="payment-form"]/div[3]/div[2]/input').fill("08")
    page.locator('xpath=//*[@id="payment-form"]/div[3]/div[3]/input').fill("1990")
    page.locator('xpath=//*[@id="submit"]').click()

    ##Verify text order placed and click continue
    expect(page.locator('xpath=//*[@id="form"]/div/div/div/h2/b')).to_be_visible()
    page.locator('xpath=//*[@id="form"]/div/div/div/div/a').click()

    ##Delete account
    page.locator('xpath=//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a').click()
    expect(page.locator('xpath=//*[@id="form"]/div/div/div/h2/b')).to_be_visible()

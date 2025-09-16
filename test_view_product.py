import pytest
from playwright.sync_api import Page, expect

def test_view_product (page:Page):
    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")

    page.locator('xpath=//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a').click()
    expect(page).to_have_title("Automation Exercise - All Products")

    page.locator('xpath=/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a').click()
    expect(page).to_have_title("Automation Exercise - Product Details")

    ##product name
    expect(page.locator('xpath=/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2')).to_be_visible

    ##category
    expect(page.locator('xpath=/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[1]')).to_be_visible

    ##price
    expect(page.locator('xpath=/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span')).to_be_visible

    ##availability
    expect(page.locator('xpath=/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[2]')).to_be_visible

    ##Condition
    expect(page.locator('xpath=/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[3]')).to_be_visible

    ##Brand
    expect(page.locator('xpath=/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[4]')).to_be_visible

    expect(page.get_by_role("link", name="Write Your Review")).to_be_visible
    page.get_by_role("link", name="Write Your Review").click()

    ##add indicators
    
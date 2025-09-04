import pytest
from playwright.sync_api import Page, expect

def test_submit_contact_form(page:Page):
    page.goto("https://www.automationexercise.com/",timeout=60000)
    expect(page).to_have_title("Automation Exercise")
    page.get_by_role("link", name="Contact Us").click()
    expect(page.get_by_role("heading", name="Contact Us")).to_be_visible()
    ##expect(page.get_by_role("textbox", name="Name")).to_be_editable()
    page.wait_for_timeout(5000)
    page.get_by_role("textbox", name="Name").fill("It's me")
    page.get_by_role("textbox", name="Email", exact=True).fill("test@gmail.com")
    page.get_by_role("textbox", name="Subject").fill("email subject short text")
    page.get_by_role("textbox", name="Your Message Here").fill("message message message")
    page.set_input_files("input[type='file']", "attachment/text-attachment.txt")
    
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator('//*[@id="contact-us-form"]/div[6]/input').click()
    expect(page.locator('//*[@id="contact-page"]/div[2]/div[1]/div/div[2]')).to_be_visible()
    ##page.pause()
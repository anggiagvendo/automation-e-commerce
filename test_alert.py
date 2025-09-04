import pytest
from playwright.sync_api import Page, expect

def test_alert (page: Page):
    page.goto("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt", timeout=60000)
    
    ##dialog handler
    page.on("dialog", lambda dialog: dialog.accept("Testuser"))
    
    ##click an element inside an iframe
    frame = page.frame(name="iframeResult")
    frame.get_by_role("button", name="Try it").click()

    ##click an element using xpath
    page.locator('//*[@id="getwebsitebtn"]').click()
    ##page.pause()
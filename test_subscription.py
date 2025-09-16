import pytest
from playwright.sync_api import Page, expect

##fixtures is usable component of test for any functioons later
@pytest.fixture(scope="function")
def opening_page(browser, request):

    ##defining context and page, MUST HAVE!
    context = browser.new_context()
    page = context.new_page()

    ##tracing start here
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    ##testcase steps
    page.goto("https://www.automationexercise.com/")
    expect(page).to_have_title("Automation Exercise")
    
    ##code before yield will run durin the test, after the yield will run after the test
    yield page

    ##tracing ends here
    trace_name= f"trace_{request.node.name}.zip"
    context.tracing.stop(path=trace_name)

    context.close()


def test_subscription_success (opening_page:Page):
    page = opening_page
    page.locator('xpath=//*[@id="susbscribe_email"]').fill("test@gmail.com")
    page.locator('xpath=//*[@id="subscribe"]').click()
    expect(page.get_by_text("You have been successfully subscribed!")).to_be_visible

def test_subscription_failed_empty (opening_page:Page):
    page = opening_page
    page.locator('xpath=//*[@id="subscribe"]').click()
    expect(page.get_by_text("You have been successfully subscribed!")).not_to_be_visible
from playwright.sync_api import Page, Playwright
from pytest_playwright.pytest_playwright import playwright

URL = "https://demo.realworld.show/"

def browser_launch(playwright: Playwright, page: Page):
    chromium = playwright.chromium.launch(headless=False)
    page.goto(URL)
    yield chromium
    chromium.close()





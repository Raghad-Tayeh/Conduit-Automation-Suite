import pytest
from playwright.sync_api import Page

URL = "https://demo.realworld.show/"

@pytest.fixture
def browser_launch(page: Page):
    page.goto(URL)
    yield page






import os
from dotenv import load_dotenv
from conftest import browser_launch
from pages.login_page import LoginPage

load_dotenv()

TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

def test_rgd_login(browser_launch):
    log_in = LoginPage(browser_launch)
    log_in.login(TEST_EMAIL, TEST_PASSWORD)
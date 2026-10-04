import os
from dotenv import load_dotenv
from pages.login_page import LoginPage

load_dotenv()

TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

def user_can_login(page):
    log_in = LoginPage(page)
    log_in.login(TEST_EMAIL, TEST_PASSWORD)
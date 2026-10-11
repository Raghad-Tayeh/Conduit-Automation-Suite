import re
from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.sign_in_nav_link = page.get_by_role("link", name= "Sign in")
        self.sign_in_button = page.get_by_role("button", name= re.compile("Sign in", re.IGNORECASE))
        self.email_field = page.get_by_placeholder("email")
        self.password_field = page.get_by_placeholder("password")

    def login(self, email, password):
        self.click(self.sign_in_nav_link)
        self.fill(self.email_field, email)
        self.fill(self.password_field, password)
        self.click(self.sign_in_button)
        '''try:
            expect(self.get_by_text("Welcome")).to_be_visible()
            print("✅ Element found!")
        except AssertionError:
            print("❌ Element NOT found")
        '''

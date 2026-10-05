from pages.base_page import BasePage
import sign_up_data_feeder as signup
import re

class SignUpPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.signup_nav_link = page.get_by_role("link", name= "Sign up")
        self.username_field = page.get_by_placeholder("Username")
        self.email_field = page.get_by_placeholder("Email")
        self.password_field = page.get_by_placeholder("Password")
        self.signup_button = page.get_by_role("button", name= re.compile("Sign up", re.IGNORECASE))

    def signup(self, username, email, password):
        self.click(self.signup_nav_link)
        self.fill(self.username_field, username)
        self.fill(self.email_field, email)
        self.fill(self.password_field, password)
        self.click(self.signup_button)
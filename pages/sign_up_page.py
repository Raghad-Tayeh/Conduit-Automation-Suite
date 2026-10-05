from pages.base_page import BasePage
import re

class SignUpPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.signup_nav_link = page.get_by_role("link", name= "Sign up")
        self.username_field = page.get_by_placeholder("Username")
        self.email_field = page.get_by_placeholder("Email")
        self.password_field = page.get_by_placeholder("Password")
        self.signup_button = page.get_by_role("Sign up", name= re.compile("Sign up", re.IGNORECASE))

    def signup(self):
        self.click(self.signup_nav_link)
        self.fill(self.username_field, )
        self.fill(self.email_field, )
        self.fill(self.password_field, )
        self.click(self.signup_button)
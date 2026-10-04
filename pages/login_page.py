from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.email_input = self.page.get_by_placeholder("raghad_auto@test.com")
        self.password_input = self.page.get_by_placeholder("rgdauto")
        self.sign_in_button = self.page.get_by_role("button", "Sign In")

    def login(self, email, password):
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.sign_in_button.click()

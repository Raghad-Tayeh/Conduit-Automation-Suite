class BasePage:
    def __init__(self, page):
        self.page = page

    def load_page(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def hover(self, locator):
        self.page.locator(locator).hover()

    def scroll(self, locator):
        self.page.locator(locator).scroll()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)
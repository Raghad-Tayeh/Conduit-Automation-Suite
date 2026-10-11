class BasePage:
    def __init__(self, page):
        self.page = page

    def load_page(self, url):
        self.page.goto(url)

    def click(self, locator):
        locator.click()

    def hover(self, locator):
        locator.hover()

    def scroll(self, locator):
        locator.scroll()

    def fill(self, locator, text):
        locator.fill(text)
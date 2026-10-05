from pages.base_page import BasePage


class ArticlePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.new_article_nav_link = page.get_by_role("link", name= "New Article")
        
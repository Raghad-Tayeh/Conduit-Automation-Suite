from pages.base_page import BasePage

class ArticlePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.new_article_nav_link = page.get_by_role("link", name= "New Article")
        self.article_title_field = page.get_by_placeholder("Article Title")
        self.article_about_field = page.get_by_placeholder("What's this article about?")
        self.article_field = page.get_by_placeholder("Write your article (in markdown)")
        self.tage_field = page.get_by_placeholder("Enter tags")
        self.publish_article_button = page.get_by_role("button", name= "Publish Article")

    def article_filler(self, title, about, article, tags):
        self.click(self.new_article_nav_link)
        self.fill(self.article_title_field, title)
        self.fill(self.article_about_field, about)
        self.fill(self.article_field, article)
        self.fill(self.tage_field, tags)
        self.click(self.publish_article_button)


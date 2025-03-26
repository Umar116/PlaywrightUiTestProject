class BasePage:

    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        self.page.goto(url)
        return self

    def get_title(self):
        return self.page.title()

    def screenshot(self, name="screenshot.png"):
        self.page.screenshot(path=name)
import allure

from pages.base_page import BasePage
from core.actions import fill, click


class NavBar(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.search_field = page.locator('input[class="oxd-input oxd-input--active"]')
        self.navigate_button = page.locator('span[class="oxd-text oxd-text--span oxd-main-menu-item--name"]')
        self.navigate_dashboard = lambda name: page.get_by_text(name)

    @allure.step('Input {text} in search field')
    def input_search_field(self, text):
        fill(locator=self.search_field, value=text)
        return self

    @allure.step('Get nav bar values')
    def dashboard_nav_bar(self):
        button = self.navigate_button
        return button

    @allure.step('Get page title')
    def get_page_title(self):
        title = self.page.locator('h6[class="oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module"]')
        return title

    @allure.step('Click {page_name} navigate')
    def navigate_to_page(self, page_name):
        click(self.navigate_dashboard(page_name))
        return self

    @allure.step('Success notification')
    def success_notification(self):
        text = self.page.locator('div[id="app"]')
        return text

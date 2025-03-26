import allure
from playwright.sync_api import expect

from core.actions import fill, submit, click
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.login_field = self.page.locator('input[name="username"]')
        self.password_field = self.page.locator('input[name="password"]')
        self.submit_button = self.page.locator('button[type="submit"]')
        self.owner_dropdown_button = self.page.locator('p[class="oxd-userdropdown-name"]')
        self.error_notification = page.locator(
            'span[class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"]')
        self.credentions_error = page.locator('p[class="oxd-text oxd-text--p oxd-alert-content-text"]')

    @allure.step('Login: input login {login}, password {password}')
    def login(self, login: str = 'Admin', password: str = 'admin123'):
        fill(locator=self.login_field, value=login)
        fill(locator=self.password_field, value=password)
        submit(locator=self.submit_button)
        return self

    @allure.step('Click login')
    def submit_authorization(self) -> None:
        submit(locator=self.submit_button)

    @allure.step('Check error on user field')
    def submit_and_validate_required_errors(self) -> None:
        click(locator=self.submit_button)
        expect(self.error_notification).to_have_count(2)

import allure
from playwright.sync_api import expect

from pages.base_page import BasePage
from core.actions import fill, click


class AdminPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.employ_name_field = page.locator('input[placeholder="Type for hints..."]')
        self.user_name_field = page.locator('input.oxd-input.oxd-input--active').nth(1)
        self.password_field = page.locator('input[type="password"]').nth(0)
        self.confirm_password_field = page.locator('input[type="password"]').nth(1)
        self.submit_button = page.locator('button[type="submit"]')
        self.open_user_form_button = page.locator('button[class="oxd-button oxd-button--medium oxd-button--secondary"]')
        self.user_form_title = page.locator('h6[class="oxd-text oxd-text--h6 orangehrm-main-title"]')
        self.user_list = page.locator('div[class="oxd-table-cell oxd-padding-cell"]')
        self.user_list_title = page.locator('h5[class="oxd-text oxd-text--h5 oxd-table-filter-title"]')
        self.error_notification = page.locator(
            'span[class="oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message"]')
        self.password_security_status = page.locator('span[class="oxd-chip oxd-chip--default orangehrm-password-chip"]')

    @allure.step('Get admin page title')
    def get_user_form_title(self):
        title = self.user_form_title
        return title

    @allure.step('Select new user {role}')
    def select_user_role(self, role: str = None):
        click(locator=self.page.get_by_text('-- Select --').first)
        click(locator=self.page.get_by_role('option', name=role))
        return self

    @allure.step('Select new user {status}')
    def select_user_status(self, status: str = None):
        click(locator=self.page.get_by_text("-- Select --"))
        click(locator=self.page.get_by_role('option', name=status))
        return self

    @allure.step('Open create user form')
    def open_create_user_form(self):
        click(self.open_user_form_button)
        expect(self.get_user_form_title()).to_contain_text('Add User')
        return self

    @allure.step('input user name {name}')
    def input_name(self, name: str = None):
        fill(locator=self.user_name_field, value=name)
        return self

    @allure.step('input user name {password}')
    def input_password(self, password: str = None):
        fill(locator=self.password_field, value=password)
        return self

    @allure.step('input user password {password}, confirm password {confirm_password}')
    def input_full_password(self, password: str = None, confirm_password: str = None):
        fill(locator=self.password_field, value=password)
        fill(locator=self.confirm_password_field, value=confirm_password)
        return self

    @allure.step('Click create user')
    def confirm_user_form(self):
        click(self.submit_button)
        return self

    @allure.step('Choose employ {name}')
    def add_employed(self, name: str = None):
        fill(locator=self.employ_name_field, value=name)
        click(locator=self.page.get_by_text(name))
        return self

    @allure.step('Get user list')
    def get_user_list(self):
        users = self.user_list
        return users

    @allure.step('Get user list title')
    def get_user_list_title(self):
        users = self.user_list_title
        return users

    @allure.step('Check error on user field')
    def submit_and_validate_required_errors(self) -> None:
        click(locator=self.submit_button)
        expect(self.error_notification).to_have_count(6)

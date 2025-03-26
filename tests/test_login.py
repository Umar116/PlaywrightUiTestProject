import allure
from playwright.sync_api import expect

from pages.login_page import LoginPage
from utils.config import BASE_URL


class TestLogin:

    @allure.title('Test Authentication')
    @allure.story('Authentication')
    def test_user_logs_in(self, page) -> None:
        login = LoginPage(page)
        login.navigate(BASE_URL)
        login.login()

        expect(login.owner_dropdown_button).to_be_visible(timeout=10000)

    @allure.title('Check displaying error notification for empty field')
    @allure.story('Authentication')
    def test_error_when_error_when_required_fields_are_empty(self, page) -> None:
        login = LoginPage(page)
        login.navigate(BASE_URL)
        login.submit_and_validate_required_errors()

    @allure.title('Check displaying error when password incorrect')
    @allure.story('Authentication')
    def test_error_when_password_is_incorrect(self, page) -> None:
        login = LoginPage(page)
        login.navigate(BASE_URL)
        login.login(password='sdfsdfssdfsdfs')

        expect(login.credentions_error).to_contain_text('Invalid credentials', timeout=10000)

    @allure.title('Check displaying error when name incorrect')
    @allure.story('Authentication')
    def test_error_when_login_is_incorrect(self, page) -> None:
        login = LoginPage(page)
        login.navigate(BASE_URL)
        login.login(login='sdfsdfssdfsdfs')

        expect(login.credentions_error).to_contain_text('Invalid credentials', timeout=10000)

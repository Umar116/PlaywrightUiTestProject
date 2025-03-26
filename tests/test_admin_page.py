import allure
import pytest
from playwright.sync_api import expect

from core.dates import fake_name
from pages.admin_page import AdminPage
from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from utils.config import BASE_URL


class TestAdminPage:

    @allure.title('New admin user with status {status} displayed in user list')
    @allure.story('Admin page')
    @pytest.mark.parametrize('status', ['Enabled', 'Disabled'])
    def test_new_admin_displayed_in_user_list(self, page, status) -> None:
        login = LoginPage(page)
        nav_bar = NavBar(page)
        admin = AdminPage(page)
        user_name = fake_name()
        login.navigate(BASE_URL) \
            .login()

        nav_bar.navigate_to_page('Admin')
        expect(nav_bar.get_page_title()).to_contain_text('Admin')

        admin.open_create_user_form() \
            .input_name(user_name) \
            .add_employed('James Butler') \
            .input_full_password('1234qwerty', '1234qwerty') \
            .select_user_role('Admin') \
            .select_user_status(status) \
            .confirm_user_form()

        expect(nav_bar.success_notification()).to_be_visible(timeout=10000)
        expect(admin.get_user_list_title()).to_be_visible(timeout=10000)
        name = ''
        for i in admin.get_user_list().all_inner_texts():
            if user_name in i:
                name = 'found'
                break
            else:
                name = 'not found'
        assert name == 'found'

    @allure.title('New ess user with status {status} displayed in user list')
    @allure.story('Admin page')
    @pytest.mark.parametrize('status', ['Enabled', 'Disabled'])
    def test_new_ess_displayed_in_user_list(self, page, status) -> None:
        login = LoginPage(page)
        nav_bar = NavBar(page)
        admin = AdminPage(page)
        user_name = fake_name()

        login.navigate(BASE_URL)
        login.login()

        nav_bar.navigate_to_page('Admin')
        expect(nav_bar.get_page_title()).to_contain_text('Admin')

        admin.open_create_user_form() \
            .input_name(user_name) \
            .add_employed('James Butler') \
            .input_full_password('1234qwerty', '1234qwerty') \
            .select_user_role('ESS') \
            .select_user_status(status) \
            .confirm_user_form()

        expect(nav_bar.success_notification()).to_be_visible(timeout=10000)
        expect(admin.get_user_list_title()).to_be_visible(timeout=10000)
        name = ''
        for i in admin.get_user_list().all_inner_texts():
            if user_name in i:
                name = 'found'
                break
            else:
                name = 'not found'
        assert name == 'found'

    @allure.title('Error displayed when required fields are empty')
    @allure.story('Admin page')
    def test_error_when_required_fields_are_empty(self, page) -> None:
        login = LoginPage(page)
        nav_bar = NavBar(page)
        admin = AdminPage(page)

        login.navigate(BASE_URL)
        login.login()

        nav_bar.navigate_to_page('Admin')
        expect(nav_bar.get_page_title()).to_contain_text('Admin', timeout=10000)

        admin.open_create_user_form()
        admin.submit_and_validate_required_errors()

    @allure.title('Error displayed when password is not matched')
    @allure.story('Admin page')
    def test_error_when_passwords_is_not_matched(self, page) -> None:
        login = LoginPage(page)
        nav_bar = NavBar(page)
        admin = AdminPage(page)

        login.navigate(BASE_URL)
        login.login()

        nav_bar.navigate_to_page('Admin')
        expect(nav_bar.get_page_title()).to_contain_text('Admin')

        admin.open_create_user_form() \
             .input_full_password('1234qwerty', '1234qwewwvwrty')

        expect(admin.error_notification).to_contain_text('Passwords do not match', timeout=10000)

    @allure.title("Security password changed in password field")
    @allure.story('Admin page')
    def test_password_security_status_changed(self, page) -> None:
        login = LoginPage(page)
        nav_bar = NavBar(page)
        admin = AdminPage(page)

        login.navigate(BASE_URL)
        login.login()

        nav_bar.navigate_to_page('Admin')
        expect(nav_bar.get_page_title()).to_contain_text('Admin', timeout=10000)

        admin.open_create_user_form()
        status = {'1': 'Very Weak',
                  '23qf': 'Weak',
                  'sdfwf3f': 'Better',
                  'cda2er2wa1': 'Strong',
                  'fasfa23f2fwefw': 'Strongest'
                  }

        for value, sec_status in status.items():
            admin.input_password(value)
            expect(page.get_by_text(sec_status)).to_be_visible(timeout=10000)
            admin.input_password("")

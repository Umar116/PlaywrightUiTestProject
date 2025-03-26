import allure
import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.nav_bar import NavBar
from utils.config import BASE_URL


class TestSearchField:

    @allure.title("Navigate button found by search field with value {name}")
    @allure.story("Search field")
    @pytest.mark.parametrize('name', ['Ad', 'Admin', 'Admin ', ' Admin', ' Admin ', 'ADMIN', 'admin'])
    def test_find_navigate_button(self, page, name) -> None:
        login = LoginPage(page)
        nav_bar = NavBar(page)
        login.navigate(BASE_URL)
        login.login()
        nav_bar.input_search_field(name)
        expect(nav_bar.dashboard_nav_bar()).to_contain_text('Admin', timeout=10000)

    @allure.title('Dashboard is empty when value not found with value {name}')
    @allure.story('Search field')
    @pytest.mark.parametrize('name', ['09876', ' ', 'asfasdf', '!@#$%^&', 'Админ'])
    def test_empty_board_when_nav_button_not_found(self, page, name) -> None:
        login = LoginPage(page)
        nav_bar = NavBar(page)
        login.navigate(BASE_URL)
        login.login()
        nav_bar.input_search_field(name)
        expect(nav_bar.dashboard_nav_bar()).not_to_be_visible()

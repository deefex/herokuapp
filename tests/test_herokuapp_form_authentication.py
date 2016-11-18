import pytest
import unittest

from selenium import webdriver

from herokuapp.model.herokuapp_form_authenication_page import LoginPage, SecureAreaPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://the-internet.herokuapp.com/login")

    def tearDown(self):
        self.driver.quit()

    def test_form_authentication_successful_login(self):
        login_page = LoginPage(self.driver)
        login_page.attempt_login("tomsmith", "SuperSecretPassword!")
        secure_area_page = SecureAreaPage(self.driver)
        assert secure_area_page.is_loaded(secure_area_page.SECURE_AREA_TITLE), "Login secure area failed to load"

    def test_form_authentication_invalid_username(self):
        login_page = LoginPage(self.driver)
        login_page.attempt_login("bobsmith", "SuperSecretPassword!")
        assert login_page.login_error_displayed()
        assert "Your username is invalid!" in self.driver.page_source

    def test_form_authentication_invalid_password(self):
        login_page = LoginPage(self.driver)
        login_page.attempt_login("tomsmith", "NotMyPassword!")
        assert login_page.login_error_displayed()
        assert "Your password is invalid!" in self.driver.page_source



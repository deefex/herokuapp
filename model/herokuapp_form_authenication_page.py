from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

    def is_loaded(self, page_locator):
        try:
            WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(page_locator))
            return True
        except TimeoutException:
            return False


class LoginPage(BasePage):
    """Page class for https://the-internet.herokuapp.com/login"""

    USERNAME_FIELD = (By.ID, 'username')
    PASSWORD_FIELD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'radius')
    ERROR_MESSAGE = (By.ID, "flash")

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    def attempt_login(self, username, password):
        self.driver.find_element(*LoginPage.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*LoginPage.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()

    def login_error_displayed(self):
        return self.driver.find_element(*LoginPage.ERROR_MESSAGE).is_displayed()


class SecureAreaPage(BasePage):
    """Page class for https://the-internet.herokuapp.com/secure"""

    SECURE_AREA_FLASH = (By.CLASS_NAME, 'flash success')
    SECURE_AREA_TITLE = (By.CLASS_NAME, 'icon-lock')
    # LOGOUT_BUTTON = (By.CLASS_NAME, 'button secondary radius')

    def click_logout_button(self):
        # self.driver.find_element(*SecureAreaPage.LOGOUT_BUTTON).click()
        self.driver.find_element_by_link_text('Logout').click()

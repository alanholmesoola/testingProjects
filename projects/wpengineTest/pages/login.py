from pages.browser import Browser
from selenium import webdriver
from locators import WrongPasswordPageLocators, LoginPageLocators
import time


class LoginPage(Browser):

    def __init__(self):
        self.LOGIN = '/'

    def log_in_as(self, username, password):
        """
        Locates username & password elements
        and sends credentials and clicks submit 
        """
        self.visit(self.LOGIN)
        time.sleep(1)# temp messure before implicit waits
        username_field = self.find_element(*LoginPageLocators.username_field)
        password_field = self.find_element(*LoginPageLocators.password_field)
        submit_btn = self.find_element(*LoginPageLocators.submit_btn)
        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_btn.click()

    def get_auth_message(self):
        """
        Locates and verifies
        dashboard message after authentication.
        """
        return self.find_element(*LoginPageLocators.message)


    def get_page_error(self):
        """
        Returns the login page error message
        """
        return self.find_element(*WrongPasswordPageLocators.error_message)
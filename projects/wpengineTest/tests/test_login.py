import unittest

from config import Config
from selenium import webdriver
from pages.login import LoginPage


class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.login_page = LoginPage()
        configuration = Config('config.json')
        
        # Test Data - Setup
        self.user = configuration.user
        self.password = configuration.password

    def testUserLogin(self):
        # Happy Path - Login Success
        #login with credentials
        
        #Arrange
        self.login_page.log_in_as(self.user, self.password)
        #look for dashboard message to confirm login successful
        
        # Act
        welcome_message = self.login_page.get_auth_message()
        
        # Assert
        self.assertIn('Dashboard', welcome_message.text)
        
        # Quit
        self.login_page.quit()


    def testLoginFail(self):
        #Login with wrong credentials
        
        # Arrange
        unregistered_user = 'otherUser'
        bad_password = 'some_bad_password'
        
        # Act
        self.login_page.log_in_as(unregistered_user, bad_password)
        # Search for error message after failed login
        message = self.login_page.get_page_error()
        
        # Assert 
        self.assertIn('ERROR', message.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)

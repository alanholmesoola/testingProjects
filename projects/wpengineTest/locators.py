from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    username_field = (By.CSS_SELECTOR, '#user_login')
    password_field = (By.CSS_SELECTOR, '#user_pass')
    submit_btn = (By.NAME, 'wp-submit')
    message = (By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/div[3]/h1')


class WrongPasswordPageLocators(object):
    error_message = (By.CSS_SELECTOR, '#login_error')

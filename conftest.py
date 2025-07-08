import pytest
import requests
import random
import string
from selenium import webdriver
from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.account_page import AccountPage
from data import BASE_URL, USERS_URL, REGISTER_URL, CHANGE_URL, url_login
from data import browser_name


# фикстура для двух браузеров
@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        browser_name = 'Chrome'
        driver = webdriver.Chrome()
    else:
        browser_name = 'Firefox'
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

# фикстура для главной страницы
@pytest.fixture
def main_page(driver):
    return MainPage(driver, browser_name)

# фикстура для страницы личного кабинета
@pytest.fixture
def account_page(driver):
    return AccountPage(driver, browser_name)


# фикстура создания пользователя со всеми обязат.полями
@pytest.fixture()
def create_and_login_user():
    # Генерируем уникальные данные для пользователя
    def generate_random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    
    email = generate_random_string(10) + "@mail.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)

    # Регистрация пользователя
    registration_payload = {
        "name": name,
        "email": email,
        "password": password  
    }
    response = requests.post(f'{BASE_URL}{USERS_URL}{REGISTER_URL}', json=registration_payload)
    access_token = response.json().get("accessToken")

    yield {
        'email': email,
        'password': password, 
        'access_token': access_token,
    }

    # Удаление пользователя после теста
    if access_token:
        headers = {
            'Authorization': access_token 
        }
    delete_response = requests.delete(f'{BASE_URL}{USERS_URL}{CHANGE_URL}', headers=headers)
    delete_response.raise_for_status() # Проверка успешного удаления)


# фикстура логинации пользователя
@pytest.fixture()
def login_user(create_and_login_user, account_page):
    email = create_and_login_user['email']
    password = create_and_login_user['password']
    account_page.go_to_url(url_login)
    account_page.login_user_to_account(email, password) 
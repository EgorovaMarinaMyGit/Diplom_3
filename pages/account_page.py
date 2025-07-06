import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators
from data import user_email


class AccountPage(BasePage):

    @allure.step("Проверка видимости надписи «Восстановление пароля» после нажатия ' \
    'на кнопку «Восстановить пароль»")
    def click_to_recover_button_for_recover_password(self): 
        self.click_to_element(AccountPageLocators.RECOVER_PASSWORD_BUTTON)
        return self.check_displaying_of_element(AccountPageLocators.TITLE_RECOVER_PASSWORD)

    
    @allure.step("Проверка видимости надписи «Введите код из письма» после ввода почты ' \
    'в поле email и нажатия на кнопку «Войти»")
    def enter_email_to_recover_password(self):
        self.click_to_element(AccountPageLocators.RECOVER_PASSWORD_BUTTON)
        self.add_text_to_element(AccountPageLocators.EMAIL_FIELD, user_email)
        self.click_to_element(AccountPageLocators.RECOVER_LOCATOR)
        self.find_element_with_wait(AccountPageLocators.ENTER_CODE_FROM_EMAIL)
        return self.check_displaying_of_element(AccountPageLocators.ENTER_CODE_FROM_EMAIL)


    @allure.step("Проверка активности поля email после нажати кнопки 'показать/скрыть пароль'")
    def check_active_email_field(self):
        self.click_element(AccountPageLocators.EYE_NOT_ACTIVE)
        self.find_element_with_wait(AccountPageLocators.FIELD_ACTIVE)
        return self.check_displaying_of_element(AccountPageLocators.FIELD_ACTIVE)


    @allure.step("Проверка перехода в «Личный кабинет» по клику")
    def check_go_to_personal_account(self):
        self.click_element(AccountPageLocators.PERSONAL_ACCOUNT)
        self.find_element_with_wait(AccountPageLocators.TITLE_PROFILE)
        return self.check_displaying_of_element(AccountPageLocators.TITLE_PROFILE)
    

    @allure.step("Залогинить пользователя")
    def login_user_to_account(self, email, password):
        self.add_text_to_element(AccountPageLocators.EMAIL_FIELD, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_FIELD, password)
        self.click_element(AccountPageLocators.ENTER_BUTTON)
        self.find_element_with_wait(AccountPageLocators.COLLECT_BURGER)

    # в ТЗ не указано откуда должен быть переход - проверяю находясь в Личном кабинете
    @allure.step("Проверка перехода в раздел «История заказов» по клику")
    def check_go_to_orders_history(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)
        return self.check_displaying_of_element(AccountPageLocators.ORDER_HISTORY_BUTTON_ACTIVE)
    

    @allure.step("Проверка выхода из аккаунта по клику на «Выход»")
    def click_to_exit(self):
        self.click_to_element(AccountPageLocators.EXIT_BUTTON)
        self.find_element_with_wait(AccountPageLocators.TITLE_ENTER)
        return self.check_displaying_of_element(AccountPageLocators.TITLE_ENTER)
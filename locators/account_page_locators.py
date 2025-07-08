from selenium.webdriver.common.by import By


class AccountPageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # надпись "Личный кабинет"
    RECOVER_PASSWORD_BUTTON = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]") # кнопка "Восстановить пароль"
    TITLE_RECOVER_PASSWORD = (By.XPATH, "//h2[contains(text(),'Восстановление пароля')]") # надпись "Восстановление пароля"
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*") # поле emai
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']") # поле "Пароль"
    REGISTER_BUTTON_FOOTER = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]") # кнопка "Зарегистрироваться"
    RECOVER_LOCATOR = (By.XPATH, "//button[contains(text(),'Восстановить')]") # кнопка "Восстановить"
    EYE_NOT_ACTIVE = (By.XPATH, "//*[name()='path' and contains(@d,'M12 4C14.0')]") # локатор для глаза - пароль не виден
    FIELD_ACTIVE = (By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']") # локатор для поля email после нажатия на глаз
    TITLE_PROFILE = (By.XPATH, "//a[contains(text(),'Профиль')]") # надпись "Профиль"
    ENTER_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]") # кнопка "Войти"
    ENTER_CODE_FROM_EMAIL = (By.XPATH, "//label[contains(text(),'Введите код из письма')]") # надпись "Введите код из письма"
    NAME_FIELD = (By.XPATH, "//input[@name='name']") # поле "Имя"
    REGISTER_BUTTON_FOOTER = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]") # кнопка "Зарегистрироваться"
    ENTER_AFTER_REGISTRATION_BUTTON = (By.XPATH, "//a[contains(text(),'Войти')]") # кнопка "Войти" после регистрации
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]") # "История заказов"
    ORDER_HISTORY_BUTTON_ACTIVE = (By.XPATH, '//a[contains(@class, "Account_link_active")]') # кнопка "История заказов" в нажатом состоянии (активная)
    EXIT_BUTTON =  (By.XPATH, "//button[contains(text(),'Выход')]") # кнопка "Выход"
    COLLECT_BURGER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]") # надпись "Соберите бургер"
    OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr") # overlay
    TITLE_ENTER = (By.XPATH, "//h2[contains(text(),'Вход')]") # надпись "Вход"

   

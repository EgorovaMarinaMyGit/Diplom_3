from selenium.webdriver.common.by import By

class MainPageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # надпись "Личный кабинет"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]") # кнопка "Конструкор"
    ORDERS_FEED = (By.XPATH, "//p[contains(text(),'Лента Заказов')]") # кнопка "Лента заказов"
    TITLE_ORDERS_FEED = (By.XPATH, "//h1[contains(text(),'Лента заказов')]") # надпись "Лента заказов"
    COLLECT_BURGER = (By.XPATH, "//h1[contains(text(),'Соберите бургер')]") # надпись "Соберите бургер"
    BULKA_IMAGE = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']") # флуорисцентная булка (1й ингредиент)
    UPPER_PLACE_FOR_INGREDIENT = (By.XPATH, "//span[contains(text(),'Перетяните булочку сюда')]") # место для ингредиента "Перетяните булочку сюда"
    INGREDIENT_DETAILS = (By.XPATH, "//h2[contains(text(),'Детали ингредиента')]") # надпись "Детали ингредиента"
    CROSS_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']") # крестик в модальном окне "Детали ингредиента"
    INGREDIENT_MODAL_WINDOW = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']") # модальное окно с деталями заказа
    COUNTER_OF_INGREDIENT = (By.XPATH, "//p[@class='counter_counter__num__3nue1']") # каунтер у ингредиента
    ORDER_IN_ORDERS_FEED = (By.XPATH, "//div[@class='OrderHistory_textBox__3lgbs mb-6']") # заказ в Ленте заказов
    PLACE_AN_ORDER_BUTTON = (By.XPATH, "//button[contains(text(),'Оформить заказ')]") # надпись "Оформить заказ"
    CREATED_ORDER_NUMBER = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']") # номер заказа в модальном окне после нажатия кнопки "Оформить заказ"
    STATUS_OF_CREATED_ORDER = (By.XPATH, "//p[contains(text(),'Ваш заказ начали готовить')]") # надпись "Ваш заказ начали готовить"
    CROSS_BUTTON_IN_ORDER_WINDOW = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]") # крестик в окне созданного заказа
    ORDER_LOCATOR = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']") # локатор заказа в Ленте заказов
    TITLE_COMPOUND = (By.XPATH, "//a[@class='OrderHistory_link__1iNby']") # надпись "Состав"
    TOTAL_COUNTER_OF_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p") # счётчик "Выполнено за все время"
    TODAY_COUNTER_OF_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p") # счётчик "Выполнено за сегодня"
    TITLE_9999 = (By.XPATH, "//*[contains(text(), '9999')]") # номер 9999
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[contains(text(),'История заказов')]") # "История заказов"
    TITLE_IN_WORK = (By.XPATH, "//p[contains(text(), 'В работе')]") # надпись "В работе"




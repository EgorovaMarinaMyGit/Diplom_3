import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data import url_main_page, url_profile_orders


class MainPage(BasePage):


    @allure.step("Проверка перехода в Конструктор по клику")
    def check_go_to_constructor(self):
        self.click_element(MainPageLocators.ORDERS_FEED)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        self.find_element_with_wait(MainPageLocators.COLLECT_BURGER)
        return self.check_displaying_of_element(MainPageLocators.COLLECT_BURGER)
    

    @allure.step("Проверка перехода в Ленту заказов по клику")
    def check_go_to_orders_feed(self):
        self.click_element(MainPageLocators.ORDERS_FEED)
        self.find_element_with_wait(MainPageLocators.TITLE_ORDERS_FEED)
        return self.check_displaying_of_element(MainPageLocators.TITLE_ORDERS_FEED)
    

    @allure.step("Проверка отображения модального окна с деталями ингредиента после нажатия на ингредиент")
    def check_appearance_window_with_ingredient_details(self):
        self.click_element(MainPageLocators.BULKA_IMAGE)
        self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS)
        return self.check_displaying_of_element(MainPageLocators.INGREDIENT_MODAL_WINDOW)
    

    @allure.step("Проверка закрытия модального окна с деталями заказа после нажатия на крестик")
    def check_close_window_after_click(self):
        self.click_element(MainPageLocators.BULKA_IMAGE)
        self.find_element_with_wait(MainPageLocators.INGREDIENT_DETAILS)
        self.click_element(MainPageLocators.CROSS_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(MainPageLocators.INGREDIENT_DETAILS))
        return True
    

    @allure.step("Проверка, что при добавлении ингредиента каунтер у ингредиента увеличивается")
    def check_increase_counter_after_adding_ingredient(self):
        counter_of_ingredient = self.get_text_from_element(MainPageLocators.COUNTER_OF_INGREDIENT)
        source_element = self.find_element_with_wait(MainPageLocators.BULKA_IMAGE)
        target_element = self.find_element_with_wait(MainPageLocators.UPPER_PLACE_FOR_INGREDIENT)
        self.drag_and_drop_element(source_element, target_element)
        counter_of_ingredient_after_adding = self.get_text_from_element(MainPageLocators.COUNTER_OF_INGREDIENT)
        return counter_of_ingredient, counter_of_ingredient_after_adding
    

    @allure.step("Оформление заказа пользователем")
    def create_order(self):
        source_element = self.find_element_with_wait(MainPageLocators.BULKA_IMAGE)
        target_element = self.find_element_with_wait(MainPageLocators.UPPER_PLACE_FOR_INGREDIENT)
        self.drag_and_drop_element(source_element, target_element)
        self.click_element(MainPageLocators.PLACE_AN_ORDER_BUTTON)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(MainPageLocators.TITLE_9999))
        order_number = self.get_text_from_element(MainPageLocators.CREATED_ORDER_NUMBER)
        status_of_order = self.get_text_from_element(MainPageLocators.STATUS_OF_CREATED_ORDER)
        self.find_element_with_wait(MainPageLocators.CROSS_BUTTON_IN_ORDER_WINDOW)
        self.scroll_to_element(MainPageLocators.CROSS_BUTTON_IN_ORDER_WINDOW)
        self.click_element(MainPageLocators.CROSS_BUTTON_IN_ORDER_WINDOW)
        return order_number, status_of_order
    

    @allure.step("Проверка отображения модального окна с деталями заказа после нажатия на заказ")
    def check_appearance_window_with_order_details(self):
        self.click_element(MainPageLocators.ORDERS_FEED)
        self.find_element_with_wait(MainPageLocators.ORDER_LOCATOR)
        self.click_element(MainPageLocators.ORDER_LOCATOR)
        self.find_element_with_wait(MainPageLocators.TITLE_COMPOUND)
        return self.check_displaying_of_element(MainPageLocators.TITLE_COMPOUND)


    @allure.step("Проверка, что номер заказа пользователя из истории заказов отображается в Ленте заказов")
    def check_created_order_in_orders_feed(self):
        order_number, status_of_order = self.create_order()
        self.click_element(MainPageLocators.PERSONAL_ACCOUNT)
        self.find_element_with_wait(MainPageLocators.ORDER_HISTORY_BUTTON)
        self.click_element(MainPageLocators.ORDER_HISTORY_BUTTON)
        order_locator = (By.XPATH, f"//p[text()='#0{order_number}']")
        order = self.find_element_with_wait(order_locator)
        if order:
            self.go_to_url(url_main_page)
        self.click_element(MainPageLocators.ORDERS_FEED)
        self.find_element_with_wait(MainPageLocators.ORDER_LOCATOR)
        self.find_element_with_wait(order_locator)
        return self.check_displaying_of_element(order_locator)

        
    @allure.step("Проверка, что после оформления заказа номер появляется в разделе «В работе»")
    def check_new_order_number_appears_in_work_section(self):
        order_number, status_of_order = self.create_order()
        self.click_element(MainPageLocators.ORDERS_FEED)
        self.find_element_with_wait(MainPageLocators.TITLE_IN_WORK)
        order_locator = (By.XPATH, f"//li[contains(@class, 'text_type_digits-default') and contains(normalize-space(.), '{order_number}')]")
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element(order_locator, order_number))
        return self.check_displaying_of_element(order_locator)
    

    @allure.step("Проверка, что при создании заказа увеличивается счётчик «Выполнено за всё время»")
    def check_increse_counter_done_for_all_time(self):
        self.click_element(MainPageLocators.ORDERS_FEED)
        counter_for_all_time = self.get_text_from_element(MainPageLocators.TOTAL_COUNTER_OF_ORDERS)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        order_number, status_of_order = self.create_order()
        self.click_element(MainPageLocators.ORDERS_FEED)
        counter_after_create_order = self.get_text_from_element(MainPageLocators.TOTAL_COUNTER_OF_ORDERS)
        return counter_for_all_time, counter_after_create_order
    

    @allure.step("Проверка, что при создании заказа увеличивается счётчик «Выполнено за сегодня»")
    def check_increse_counter_done_for_today(self):
        self.click_element(MainPageLocators.ORDERS_FEED)
        counter_for_today = self.get_text_from_element(MainPageLocators.TODAY_COUNTER_OF_ORDERS)
        self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)
        order_number, status_of_order = self.create_order()
        self.click_element(MainPageLocators.ORDERS_FEED)
        counter_after_create_order = self.get_text_from_element(MainPageLocators.TODAY_COUNTER_OF_ORDERS)
        return counter_for_today, counter_after_create_order
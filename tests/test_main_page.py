import allure
from data import url_main_page


class TestMainPage:


    @allure.title("Переход в Конструктор после нажатия на кнопку «Конструктор»")
    def test_go_to_constructor_after_click(self, main_page):
        main_page.go_to_url(url_main_page)
        assert main_page.check_go_to_constructor() == True


    @allure.title("Переход в Ленту заказов после нажатия на кнопку «Лента Заказов»")
    def test_go_to_orders_feed_after_click(self, main_page):
        main_page.go_to_url(url_main_page)
        assert main_page.check_go_to_orders_feed() == True


    @allure.title("Появление окна с деталями ингредиента при нажатии на ингредиент")
    def test_appearance_window_with_ingredient_details_after_click(self, main_page):
        main_page.go_to_url(url_main_page)
        assert main_page.check_appearance_window_with_ingredient_details() == True


    @allure.title("Модальное окно с деталями ингредиента закрывается если нажать на крестик")
    def test_close_window_after_click_on_cross(self, main_page):
        main_page.go_to_url(url_main_page)
        assert main_page.check_close_window_after_click() == True


    @allure.title("При добавлении ингредиента в заказ увеличивается каунтер данного ингредиента")
    def test_increase_counter_after_adding_ingredient(self, main_page):
        main_page.go_to_url(url_main_page)
        counter_of_ingredient, counter_of_ingredient_after_adding = main_page.check_increase_counter_after_adding_ingredient()
        assert counter_of_ingredient, counter_of_ingredient_after_adding == ('0', '2')


    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order_by_logined_user(self, login_user, main_page):
        order_number, status_of_order = main_page.create_order()
        expected_status = 'Ваш заказ начали готовить'
        assert status_of_order == expected_status


    @allure.title("Появление окна с деталями заказа при нажатии на заказ")
    def test_appearance_window_with_order_details_after_click(self, main_page):
        main_page.go_to_url(url_main_page)
        assert main_page.check_appearance_window_with_order_details() == True


    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_user_order_is_displayes_in_order_feed(self, login_user, main_page):
        assert main_page.check_created_order_in_orders_feed() == True


    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_number_appears_in_work_section(self, login_user, main_page):
        assert main_page.check_new_order_number_appears_in_work_section() == True


    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_increse_counter_done_for_all_time(self, login_user, main_page):
        counter_for_all_time, counter_after_create_order = main_page.check_increse_counter_done_for_all_time()
        assert counter_after_create_order > counter_for_all_time


    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_increse_counter_done_for_today(self, login_user, main_page):
        counter_for_today, counter_after_create_order = main_page.check_increse_counter_done_for_today()
        assert counter_after_create_order > counter_for_today
import allure
from data import url_login


class TestAccount:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_recover_password(self, account_page):
        account_page.go_to_url(url_login)
        assert account_page.click_to_recover_button_for_recover_password() is True


    @allure.title("Восстановление пароля через ввод email и кнопку «Восстановить»")
    def test_enter_email_to_recover_password(self, account_page):
        account_page.go_to_url(url_login)
        assert account_page.enter_email_to_recover_password() is True


    @allure.title("Активность поля email после нажатия кнопки 'показать/скрыть пароль'")
    def test_active_email_field_after_push_eye(self, account_page):
        account_page.go_to_url(url_login)
        assert account_page.check_active_email_field() is True
        

    # не было указано должен ли быть залогинен пользователь (я проверяла с залогиненым)
    @allure.title("Переход в личный кабинет после нажатия кнопки «Личный кабинет»")
    def test_go_to_personal_account_after_click(self, login_user, account_page):
        assert account_page.check_go_to_personal_account() is True


    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_orders_history(self, login_user, account_page):
        account_page.check_go_to_personal_account()
        assert account_page.check_go_to_orders_history() is True
        

    @allure.title("Выход из профиля")
    def test_exit_from_account(self, login_user, account_page):
        account_page.check_go_to_personal_account()
        assert account_page.click_to_exit() is True
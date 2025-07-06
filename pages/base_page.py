from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import browser_name


class BasePage:
    
    def __init__(self, driver, browser_name):
        self.driver = driver
        self.browser_name = browser_name
        self.wait = WebDriverWait(self.driver, 5)


    @allure.step("Перейти по URL'у")
    def go_to_url(self, url):
        self.driver.get(url)


    @allure.step("Найти элемент")
    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator) 
    

    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
    
   
    @allure.step("Кликнуть на элемент")
    def click_element(self, locator):
        if self.browser_name == "Chrome":
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        else:
            target = self.wait.until(EC.element_to_be_clickable(locator))
            click = ActionChains(self.driver)
            click.move_to_element(target).click().perform()


    @allure.step("Кликнуть на элемент")
    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()


    @allure.step("Добавить тест в элемент")
    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)


    @allure.step("Получить текст у элемента")
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text
    

    @allure.step("Отформатировать локатор")
    def formatted_locator(self, f_locator, num):
        method, locator = f_locator
        locator = locator.format(num)
        return method, locator
    
    @allure.step('Проверить кликабельность элемента')
    def check_element_is_clickable(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
    

    @allure.step("Доскроллить до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element) 


    @allure.step("Перетащить элемент")
    def drag_and_drop_element(self, source_element, target_element):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
             var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        self.driver.execute_script(script, source_element, target_element)



    
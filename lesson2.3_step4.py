from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

# Математическая функция со страницы
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Жмем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Конфирмим алерт
    alert = browser.switch_to.alert
    alert.accept()

    # Код, который считает математическую функцию от x
    x_element = browser.find_element_by_id("input_value").text
    x_value = int(x_element)
    x = x_value
    y = calc(x)

    # Заполняем ответ
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)

    # Жмем кнопку
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
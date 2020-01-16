from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html" #адрес веб страницы
    browser = webdriver.Chrome()
    browser.get(link) #открываем линк

    # Код, который считает сумму чисел на странице
    xs = browser.find_element_by_id("num1").text #первое число
    ys =  browser.find_element_by_id("num2").text #второе число
    x = int(xs)
    y = int(ys)
    z = str(x+y) #сумма чисел

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z) # ищем элемент со значением суммы чисел

    # Отправляем выбранный ответ
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
import time
import math

# Математическая функция со страницы
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который считает математическую функцию от x
    x_element =  browser.find_element_by_id ("input_value").text
    x_value = int(x_element)
    x = x_value
    y = calc(x)

    # Отправляем заполненную форму
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    # Проскролливаем до кнопки так как она ниже всего
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    #Жмем сабмит
    button.click()
    assert True

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
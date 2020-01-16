from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код, который считает математическую функцию от x
    x_element =  browser.find_element_by_tag_name ("img")
    x_value = x_element.get_attribute ("valuex")
    x = x_value
    y = calc(x)

#    x_element = driver.findElement(By.TAG_NAME("img")).getAttribute("valuex")
#    x = x_element.text
#    y = calc(x)


    # Отправляем заполненную форму
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
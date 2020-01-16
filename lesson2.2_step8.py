from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Прикрепляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    choosefile = browser.find_element_by_name("file")
    choosefile.send_keys(file_path)

    # Заполняем форму
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Pupkin")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("ipupkin@test.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
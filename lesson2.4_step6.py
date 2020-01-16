from selenium import webdriver

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Жмем кнопку
    button = browser.find_element_by_id("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

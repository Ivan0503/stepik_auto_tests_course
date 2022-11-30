from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    # 1. Открыть страницу http://suninjuly.github.io/alert_accept.html
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    # 3. Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # 4. На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    x = x_element.text
    y = calc(x)

    #Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    time.sleep(1)

    #Нажать на кнопку Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
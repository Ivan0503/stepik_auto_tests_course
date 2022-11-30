from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    #1. Открыть страницу
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # 2. Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    # 3. Посчитать математическую функцию от x.
    x = x_element.text
    y = calc(x)
    # 4. Проскроллить страницу вниз.
    browser.execute_script("window.scrollBy(0, 200);")
    # 5. Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    # 6. Выбрать checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    option1.click()
    # 7. Переключить radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    option2.click()
    time.sleep(1)
    # 8. Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
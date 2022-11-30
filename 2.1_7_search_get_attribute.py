from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
try:
    #1. Открыть страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Считать значение для переменной x.'[id="treasure"]'
    # 3. Посчитать математическую функцию от x (код для этого приведён ниже).
    valuex = browser.find_element(By.CSS_SELECTOR, '[id="treasure"]')
    x = valuex.get_attribute("valuex")
    y = calc(x)

    # 4. Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)
    time.sleep(2)

    # 5. Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.CSS_SELECTOR, '[id="robotCheckbox"]')
    option1.click()

    # 6. Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.CSS_SELECTOR, '[id="robotsRule"]')
    option2.click()

    # 7. Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
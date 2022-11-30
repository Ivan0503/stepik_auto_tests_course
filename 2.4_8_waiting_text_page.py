# В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:
# 1. Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# 3. Нажать на кнопку "Book"
# 4. Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    #1. Открыть страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    #.text_to_be_present_in_element((By.ID, "здесь пишем ID"), "здесь текст")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")) #Задаем счетчик ожидания
    button = browser.find_element(By.ID, "book") #Объявляем кнопку
    button.click() #прокликиваем

    # 4. Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    # 5. Посчитать математическую функцию от x.
    x = x_element.text
    y = calc(x)

    # 6. Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys(y)

    # 7. Нажать на кнопку "Submit".
    Submit = browser.find_element(By.CSS_SELECTOR, "[id='solve']")
    Submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

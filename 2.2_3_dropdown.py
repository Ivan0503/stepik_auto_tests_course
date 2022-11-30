from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    #1. Открыть страницу
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #2. Посчитать сумму заданных чисел
    sum1 = browser.find_element(By.CSS_SELECTOR, '[id="num1"]')
    sum1 = sum1.text
    sum2 = browser.find_element(By.CSS_SELECTOR, '[id="num2"]')
    sum2 = sum2.text
    sum = int(sum1) + int(sum2)

    #3. Выбрать в выпадающем списке значение равное расчитанной сумме

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))  # ищем элемент со значением sum (переводим из int->string)
    time.sleep(2)

    #4. Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
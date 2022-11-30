from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#импортирую библиотеку math
import math

#объявляю ссылку
link = "http://suninjuly.github.io/find_link_text"

try:
    #открываю браузер
    browser = webdriver.Chrome()
    #перехожу по ссылке
    browser.get(link)
    #объявляю новую ссылку - считается число/ссылка по которой нужно перейти
    a = str(math.ceil(math.pow(math.pi, math.e)*10000))
    #ожидание 1 сек
    time.sleep(1)
    #переход по ссылке
    link = browser.find_element(By.LINK_TEXT, a)
    link.click()
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    time.sleep(1)
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    time.sleep(1)
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 3 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
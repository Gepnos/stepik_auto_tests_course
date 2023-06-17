from selenium import webdriver # открываем библиотеку webdriver
from selenium.webdriver.common.by import By #открываем библеотеку By
import time

try: # вводим условия (сделано для того чтобы код сработал в любом случае даже если действи в этом блоке не сработают
    link = "http://suninjuly.github.io/get_attribute.html" # вводим переменную с значением ссылки для удобства дальнейшего использования
    browser = webdriver.Chrome() #команда для открытия браузера(в нашем случае хрома
    browser.get(link) # открытие ссылки в нашем браузере

    import math # открываем библиотеку мат функций

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x))))) # пока не разобрался


    x_element = browser.find_element(By.ID, "treasure") # поиск элемента по ID
    x = x_element.get_attribute("valuex") # поиск значения указанного атрибута
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver # открываем библиотеку webdriver
from selenium.webdriver.common.by import By #открываем библеотеку By
import time

try: # вводим условия (сделано для того чтобы код сработал в любом случае даже если действи в этом блоке не сработают
    link = "https://suninjuly.github.io/selects2.html" # вводим переменную с значением ссылки для удобства дальнейшего использования
    browser = webdriver.Chrome() #команда для открытия браузера(в нашем случае хрома
    browser.get(link) # открытие ссылки в нашем браузере

    import math # открываем библиотеку мат функций

    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text

    p = str(int(y) + int(x))

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(p)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
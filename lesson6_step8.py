from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "third")
    input3.send_keys("test@gmail.com")
    input4 = browser.find_element(By.CLASS_NAME, "first")
    input4.send_keys("555-333-2211")
    input5 = browser.find_element(By.CLASS_NAME, "second")
    input5.send_keys("Broadway 1, New York")
    button = browser.find_element(By.XPATH, "//*[@type='submit']")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

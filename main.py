from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

'''
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
'''

link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    """
    Функция возращает результат формулы ln(abs(12*sin(x)))
    :param x:
    :return str:
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


driver = webdriver.Chrome()
# Открываем страницу
driver.get(link)

price = WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )
button = driver.find_element(By.CLASS_NAME, "btn.btn-primary")
button.click()

# Получаем строковое значение x
x = driver.find_element(By.ID,'input_value').text

# Получаем результат формулы
calculation_result = calc(x)

input1 = driver.find_element(By.ID, "answer")
input1.send_keys(str(calculation_result))
button4 = driver.find_element(By.ID, "solve")
button4.click()

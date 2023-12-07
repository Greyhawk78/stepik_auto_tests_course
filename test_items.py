from selenium.webdriver.common.by import By


def test_check_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.implicitly_wait(10)
    assert browser.find_elements(By.XPATH, '//*[@id="add_to_basket_form"]/button'), 'Button not found'


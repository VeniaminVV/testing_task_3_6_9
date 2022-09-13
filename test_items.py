from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_btn_add_to_basket_is_on_page(browser):
    browser.get(link)
    btn = len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"))
    assert btn > 0, "Кнопка не на месте...."

from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")
    PHONE = (By.XPATH, "//*[text()='+38 098 911 95 22']")
    EMAIL = (By.XPATH, "//a[@href='mailto:']/text()")
    CURRENCY = (By.XPATH, "//select[@id='currency']")
    USD = (By.XPATH, "//select[@id='currency']/option[text()='USD']")
    UAH = (By.XPATH, "//select[@id='currency']/option[text()='UAH']")
    EUR = (By.XPATH, "//select[@id='currency']/option[text()='EUR']")
    LOGO = (By.XPATH, "//img[@src='images/logo.png']")
    SEARCH_INPUT = (By.XPATH, "//input[@id='typeahead']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    WISHLIST = (By.XPATH, "//a[@href='wish/show']")
    CART = (By.XPATH, "//a[@href='cart/show']")






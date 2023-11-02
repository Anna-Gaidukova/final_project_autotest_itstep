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
    HOTHITS = (By.XPATH, '//a[@href="main/showHit" and @class="check-item check-hot"]')
    SALES = (By.XPATH, '//a[@href="main/showSale"]/span[text()="Скидки"]')
    NEW_COMINGS = (By.XPATH, '//a[@href="main/showNew"]/span[text()="Новинки"]')
    READMI_LIST = (By.XPATH, '//div[text()="Readmi"]')
    OPPO_LIST = (By.XPATH, '//div[text()="OPPO"]')
    JBL_LIST = (By.XPATH, '//div[text()="JBL"]')
    SAMSUNG_LIST = (By.XPATH, '//div[text()="Samsung"]')
    SAMSUNG_J701 = (By.XPATH, '//a[text()="Samsung J701"]')

    LENOVO_LIST = (By.XPATH, '//div[text()="Lenovo"]')
    MEIZU_LIST = (By.XPATH, '//div[text()="Meizu"]')
    HUAWEI_LIST = (By.XPATH, '//div[text()="Huawei"]')
    XIAOMI_LIST = (By.XPATH, '//div[text()="Xiaomi"]')
    APPLE_LIST = (By.XPATH, '//div[text()="Apple"]')

    SUBSCRIBE = (By.XPATH, '//div[text()="Подпишитесь на рассылку"]')
    NEWSLETTER_IMPUT = (By.XPATH, '//input[@name="submail"]')
    FOOTER_LOGO = (By.XPATH, '//img[@src="images/logo-footer.png"]')


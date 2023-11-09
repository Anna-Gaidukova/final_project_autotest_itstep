from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_SIGNUP = (By.XPATH, "//div[@class='top_bar_user']/a[@href='user/login']")
    DETAILS = (By.XPATH, '//a[text()="Детали сотрудничества"]')
    FEEDBACK = (By.XPATH, "//a[text()='Обратная связь']")
    DELIVERY = (By.XPATH, "//a[text()='Доставка']")
    WARRANTY = (By.XPATH, "//a[text()='Гарантия']")
    PHONE = (By.XPATH, "//*[text()='+38 098 911 95 22']")
    EMAIL = (By.XPATH, "//a[@href='mailto:']")

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
    NEWSLETTER_INPUT = (By.XPATH, '//input[@name="submail"]')
    SUBSCRIBE_BTN = (By.XPATH, "//button[text() = 'Подписаться!']")
    FOOTER_LOGO = (By.XPATH, '//img[@src="images/logo-footer.png"]')
    ALERT_SUCCESS = (By.XPATH, "//div[@id='alert-success']")


class MainPageLocators:
    MAIN_SLIDER = (By.XPATH, '//div[@class = "screen_slider"]')
    CATEGORY_CHARGERS = (By.XPATH, '//a[@href = "category/zaryadki"]')
    SUB_CAT_POWERBANK = (By.XPATH, "//ul[contains(@class, 'cat_menu')]//a[contains(., 'Павер банк')]")

    INFO_BLOCK_REFUND = (By.XPATH, '//div[@class = "characteristics"]//div[@class = "row"]/div[1]/div')
    INFO_BLOCK_FREE_SHIPPING = (By.XPATH, '//div[@class = "characteristics"]//div[@class = "row"]/div[2]/div')
    INFO_BLOCK_DELAY = (By.XPATH, '//div[@class = "characteristics"]//div[@class = "row"]/div[3]/div')
    INFO_BLOCK_TECH_SUPPORT = (By.XPATH, '//div[@class = "characteristics"]//div[@class = "row"]/div[4]/div')
    BUTTON_SHOW_NEW_PRODUCT = (By.XPATH, "//div[@class='new_arrivals_title clearfix']//a[@href='main/showNew' and contains(text(), 'Показать все')]")
    BUTTON_PREV_NEW_PRODUCT = (By.XPATH, '//div[@class = "new_arrivals"]//div[@class = "arrivals_nav arrivals_prev"]')
    BUTTON_NEXT_NEW_PRODUCT = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'arrivals_nav arrivals_next']")
    SECTION_NEW_PRODUCTS = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']")
    NEW_PRODUCT_8 = (By.XPATH, "//div[@class = 'new_arrivals']//div[@class = 'slick-list draggable']/div/div[3]/div[2]")
    BUTTON_SHOW_HITS = (By.XPATH, "//div[@class='best_sellers']//a[@class='view-all'][contains(text(), 'Показать все')]")
    BUTTON_PREV_HITS = (By.XPATH, "//div[@class = 'best_sellers']//div[@class = 'best_prev best_nav']/i")
    BUTTON_NEXT_HITS = (By.XPATH, "//div[@class = 'best_sellers']//div[@class = 'best_next best_nav']/i")
    SECTION_HITS = (By.XPATH, "//div[@class = 'best_sellers']//div[@class = 'bestsellers_panel panel active']")
    BUTTON_PREV_TREND = (By.XPATH, "//div[@class = 'trends']//div[@class = 'trends_prev trends_nav slick-arrow']/i")
    BUTTON_NEXT_TREND = (By.XPATH, "//div[@class = 'trends']//div[@class = 'trends_next trends_nav slick-arrow']/i")





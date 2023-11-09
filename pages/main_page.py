from ..pages import base_page, locators
import inspect


class MainPage(base_page.BasePage):
    def is_button_login(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGIN_SIGNUP), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_feedback(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "ELement 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.FEEDBACK), \
            "Button feedback is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_delivery(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.DELIVERY), \
            "Button delivery is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_warranty(self):
        assert self.hover_action(*locators.BasePageLocators.DETAILS), \
            "Element 'Детали сотрудничества' is not present"
        assert self.is_element_present(*locators.BasePageLocators.WARRANTY), \
            "Button warranty is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_phone(self):
        assert self.is_element_present(*locators.BasePageLocators.PHONE), \
            "Element phone is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_email(self):
        assert self.is_element_present(*locators.BasePageLocators.EMAIL), \
            "Element email is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_currency(self):
        assert self.is_element_present(*locators.BasePageLocators.CURRENCY), \
            "Button currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_uah(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.UAH), \
            "Element UAH is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_usd(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.USD), \
            "Element USD is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_eur(self):
        assert self.click_element(*locators.BasePageLocators.CURRENCY), \
            "The element is not present or intractable"
        assert self.is_element_present(*locators.BasePageLocators.EUR), \
            "Element EUR is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGO), \
            "The element logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_search_input(self):
        assert self.is_element_present(*locators.BasePageLocators.SEARCH_INPUT), \
            "The element search input is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_submit(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBMIT_BUTTON), \
            "The element submit button is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_wishlist(self):
        assert self.is_element_present(*locators.BasePageLocators.WISHLIST), \
            "The element wishlist button is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_cart(self):
        assert self.is_element_present(*locators.BasePageLocators.CART), \
            "The element cart is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_readme_list(self):
        assert self.is_element_present(*locators.BasePageLocators.READMI_LIST), \
            "The element readme list is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_oppo_list(self):
        assert self.is_element_present(*locators.BasePageLocators.OPPO_LIST), \
            "The element oppo list is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_jbl_list(self):
        assert self.is_element_present(*locators.BasePageLocators.JBL_LIST), \
            "The element jbl list is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_samsung_list(self):
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_LIST), \
            "The element samsung list is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_samsung_j701(self):
        assert self.hover_action(*locators.BasePageLocators.SAMSUNG_LIST), \
            "Element samsung is not present"
        assert self.is_element_present(*locators.BasePageLocators.SAMSUNG_J701), \
            "The element samsung j701 is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_lenovo_list(self):
        assert self.is_element_present(*locators.BasePageLocators.LENOVO_LIST), \
            "The element lenovo list is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_meizu_list(self):
        assert self.is_element_present(*locators.BasePageLocators.MEIZU_LIST), \
            "The element meizu list is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_huawei_list(self):
        assert self.is_element_present(*locators.BasePageLocators.HUAWEI_LIST), \
            "The element huawei list is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_xiaomi_list(self):
        assert self.is_element_present(*locators.BasePageLocators.XIAOMI_LIST), \
            "The element xiaomi list is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_apple_list(self):
        assert self.is_element_present(*locators.BasePageLocators.APPLE_LIST), \
            "The element apple list is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_main_slider(self):
        assert self.is_element_present(*locators.MainPageLocators.MAIN_SLIDER), \
            "The element main slider is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_category_chargers(self):
        assert self.is_element_present(*locators.MainPageLocators.CATEGORY_CHARGERS), \
            "The element chargers is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_sub_cat_powerbank(self):
        assert self.hover_action(*locators.MainPageLocators.CATEGORY_CHARGERS), \
            "Element chargers is not present"
        assert self.is_element_present(*locators.MainPageLocators.SUB_CAT_POWERBANK), \
            "The element chargers subcategory is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_refund(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_REFUND), \
            "The element refund is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_free_shipping(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_FREE_SHIPPING), \
            "The element free shipping is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_delay(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_DELAY), \
            "The element money delay is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_info_block_tech_support(self):
        assert self.is_element_present(*locators.MainPageLocators.INFO_BLOCK_TECH_SUPPORT), \
            "The element technical support is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_show_new_product(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_SHOW_NEW_PRODUCT), \
            "The element new product display is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_prev_new_product(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_NEW_PRODUCT), \
            "The button preview of new product is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_next_new_product(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_NEW_PRODUCT), \
            "The element next new product is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_selection_new_prod(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_NEW_PRODUCTS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_new_prod_8(self):
        assert self.hover_action(*locators.MainPageLocators.SECTION_NEW_PRODUCTS), \
            "The element is not present"
        assert self.is_element_present(*locators.MainPageLocators.NEW_PRODUCT_8), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_show_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_SHOW_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")


    def is_button_prev_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_next_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_selection_hits(self):
        assert self.is_element_present(*locators.MainPageLocators.SECTION_HITS), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_btn_prev_trend(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_PREV_TREND), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_btn_next_trend(self):
        assert self.is_element_present(*locators.MainPageLocators.BUTTON_NEXT_TREND), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_button_subscribe(self):
        assert self.is_element_present(*locators.BasePageLocators.SUBSCRIBE), \
            "The element subscribe is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_elem_footer_logo(self):
        assert self.is_element_present(*locators.BasePageLocators.FOOTER_LOGO), \
            "The element footer logo is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def subscribe_action(self, email):
        assert self.input_data(*locators.BasePageLocators.NEWSLETTER_INPUT, email), \
            "The element is not inserted"
        self.explicit_wait(5)
        assert self.click_element(*locators.BasePageLocators.SUBSCRIBE_BTN), \
            "The element is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - OK")

    def is_alert_success_after_sbscr(self):
        assert self.is_element_appeared_after_while(*locators.BasePageLocators.ALERT_SUCCESS, timeout=5), \
            "The element is not present"
        print(f"{inspect.currentframe().f_code.co_name} - OK")



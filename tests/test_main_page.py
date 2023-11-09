import pytest
from ..pages.base_page import BasePage
from ..pages.main_page import MainPage
import random
from ..settings import sets

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.main_page
class TestMainPage:

    def setup_method(self):
        hash_name = "%032x" % random.getrandbits(128)
        self.email_for_subscribe = f"{hash_name}@mail.com"

    def test_get_main_page(self, browser):
        page = BasePage(browser, sets.PROD_SERVER)
        page.open()

    def test_main_page_header(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_login()
        page.is_button_feedback()
        page.is_button_delivery()
        page.is_button_warranty()
        page.is_elem_phone()
        page.is_elem_email()
        page.is_button_currency()
        page.is_button_uah()
        page.is_button_usd()
        page.is_button_eur()
        page.is_elem_logo()
        page.is_elem_search_input()
        page.is_button_submit()
        page.is_button_wishlist()
        page.is_button_cart()
        page.is_button_readme_list()
        page.is_button_oppo_list()
        page.is_button_jbl_list()
        page.is_button_samsung_list()
        page.is_button_samsung_j701()
        page.is_button_lenovo_list()
        page.is_button_meizu_list()
        page.is_button_huawei_list()
        page.is_button_xiaomi_list()
        page.is_button_apple_list()

    def test_main_page_main_body(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_main_slider()
        page.is_category_chargers()
        page.is_sub_cat_powerbank()
        page.is_info_block_refund()
        page.is_info_block_free_shipping()
        page.is_info_block_delay()
        page.is_info_block_tech_support()
        page.is_button_show_new_product()
        page.is_button_prev_new_product()
        page.is_button_next_new_product()
        page.is_selection_new_prod()
        page.is_button_new_prod_8()
        page.is_button_show_hits()
        page.is_button_prev_hits()
        page.is_button_next_hits()
        page.is_selection_hits()
        page.is_btn_prev_trend()
        page.is_btn_next_trend()

    def test_main_page_footer(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.is_button_subscribe()
        page.is_elem_footer_logo()

    def test_main_page_subscribe_action(self, browser):
        self.link_to_cabinet = browser.current_url
        page = MainPage(browser, self.link_to_cabinet)
        page.subscribe_action(self.email_for_subscribe)
        page.is_alert_success_after_sbscr()






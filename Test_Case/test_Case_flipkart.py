import pytest
from selenium import webdriver
import time
from PageObjectModel.Flipkart_page_object import Flipkart_webpsite

class Test_Flipkart_website_001:
    driver=webdriver.Chrome(executable_path="Driver\chromedriver.exe")
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()

    def test_website(self):
        self.fw=Flipkart_webpsite(self.driver)
        time.sleep(1)
        self.fw.popup_message()
        time.sleep(1)
        self.fw.Search_bar_inbox()
        time.sleep(1)
        self.fw.Search_Button()

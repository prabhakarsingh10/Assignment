class Flipkart_webpsite:
    popup_message_xpath = "/html/body/div[2]/div/div/button"
    Search_bar_inbox_class = "_3704LK"
    Search_button_class = "L0Z3Pu"

    def __init__(self, driver):
        self.driver = driver

    def popup_message(self):
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()

    def Search_bar_inbox(self):
        self.driver.find_element_by_class_name("_3704LK").send_keys("Mobile Phone")

    def Search_Button(self):
        self.driver.find_element_by_class_name("L0Z3Pu").click()

from selenium import webdriver


class SeleniumSetup:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        self.driver.set_page_load_timeout(20)
        self.driver.maximize_window()

    def tear_down(self):
        self.driver.close()
        self.driver.quit()

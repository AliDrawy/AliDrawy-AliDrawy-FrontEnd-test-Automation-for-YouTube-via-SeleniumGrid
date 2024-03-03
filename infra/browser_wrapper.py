from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class WebNavigator:
    def __init__(self):
        self.timeout = None
        self.web_driver = None
        self.parallel = True
        self.serial = False

    def launch_browser(self, browser):
        self.web_driver = self.get_driver(browser)
        self.open_website("https://www.youtube.com/")
        return self.web_driver

    def fetch_wait(self, timeout=50):
        self.timeout = timeout
        return WebDriverWait(self.web_driver, self.timeout)

    def open_website(self, website_url):
        self.web_driver.get(website_url)

    def open_channel(self):
        self.open_website("https://www.youtube.com/@harrypotter/videos")

    def open_video(self):
        self.open_website("https://www.youtube.com/watch?v=Qgr4dcsY-60")

    def terminate_browser(self):
        if self.web_driver:
            self.web_driver.quit()

    def get_driver(self, browser):
        browser_type = browser
        if self.parallel:
            options = self.set_up_capabilities(browser_type)
            self.web_driver = webdriver.Remote(command_executor="http://192.168.217.1:4444", options=options)


        else:
            if browser.lower() == 'chrome':
                self.web_driver = webdriver.Chrome()
            elif browser.lower() == 'firefox':
                self.web_driver = webdriver.Firefox()
            elif browser.lower() == 'edge':
                self.web_driver = webdriver.Edge()
        self.open_website("https://www.youtube.com/")

        return self.web_driver

    def set_up_capabilities(self, browser_type):
        options = ''
        if browser_type.lower() == 'chrome':
            options = webdriver.ChromeOptions()
        elif browser_type.lower() == 'firefox':
            options = webdriver.FirefoxOptions()
        elif browser_type.lower() == 'edge':
            options = webdriver.EdgeOptions()

        options.add_argument(f'--platformName=windows')
        return options

    def get_browsers(self):
        return ["chrome", "chrome"]

    # def is_grid(self):
    #     return ["chrome", "edge"]

    # def get_browser(self):
    #     return "chrome"

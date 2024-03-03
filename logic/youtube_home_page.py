from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from infra.page_base import WebPageBase
from selenium.common.exceptions import TimeoutException


class YouTubeHomePage(WebPageBase):
    CONFIG_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Settings']")
    DARK_MODE = "Dark theme"
    LIGHT_MODE = "Light theme"
    SYSTEM_MODE = "Use device theme"
    THEME_MENU = (By.XPATH, "//tp-yt-paper-item[@role='menuitem']")
    LOCATION_BTN = (By.XPATH,
                    '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer[1]/div[2]/ytd-compact-link-renderer[4]/a')
    FRANCE_LOCATION = (By.XPATH,
                       '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[29]/a')
    ISRAEL_LOCATION = (By.XPATH,
                       '/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[43]/a')

    def change_location(self, location):
        if location == "France":
            location = self.FRANCE_LOCATION
            self.access_settings()
        else:
            location = self.ISRAEL_LOCATION

        self.wait_condition.until(EC.element_to_be_clickable(self.LOCATION_BTN)).click()
        self.wait_condition.until(EC.element_to_be_clickable(location)).click()
        self.access_settings()
        self.wait_condition.until(EC.visibility_of_element_located(self.LOCATION_BTN))
        result = self.browser_driver.find_element(*self.LOCATION_BTN)
        return result.text[10:]

    def access_settings(self):
        self.wait_condition.until(EC.element_to_be_clickable(self.CONFIG_BUTTON)).click()

    def select_theme_menu(self, current_theme):
        return self.wait_condition.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@id='label' and contains(text(), 'Appearance: {current_theme}')]")))

    def choose_theme_option(self, theme_choice):
        return self.wait_condition.until(EC.element_to_be_clickable(
            (By.XPATH, f"//tp-yt-paper-item[@role='link' and contains(., '{theme_choice}')]")))

    def modify_theme(self, new_theme, current_theme="Device theme"):
        theme_choice = ""
        if new_theme == "Dark":
            theme_choice = self.DARK_MODE
        elif new_theme == "Light":
            theme_choice = self.LIGHT_MODE
        elif new_theme == "Device theme":
            theme_choice = self.SYSTEM_MODE
        self.access_settings()
        theme_menu = self.select_theme_menu(current_theme)
        theme_menu.click()
        theme_option = self.choose_theme_option(theme_choice)
        theme_option.click()

    def confirm_theme(self, theme):
        self.access_settings()
        try:
            self.select_theme_menu(theme)
        except TimeoutException:
            return False
        finally:
            self.access_settings()
        return True

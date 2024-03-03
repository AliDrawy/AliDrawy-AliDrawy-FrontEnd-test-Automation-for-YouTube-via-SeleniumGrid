from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.page_base import WebPageBase


class YouTubeChannel(WebPageBase):
    CLEAR_BTN = (By.XPATH,
                 '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[2]/div[2]/div/ytd-menu-renderer/div[1]/ytd-button-renderer')
    NUM_OF_VIDEOS_IN_QUEUE = (By.XPATH,
                              '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[1]/div[1]/div/div/span')
    MINI_PLAYER_BTN = (
        By.XPATH,
        '/html/body/ytd-app/ytd-miniplayer/div[2]/div/div[1]/div[1]/div/ytd-player/div/div/div[19]/div/button[2]')
    ADD_TO_QUEUE = (By.XPATH, '//*[@id="items"]/ytd-menu-service-item-renderer[1]/tp-yt-paper-item')
    OLDEST_BTN = (By.XPATH, '//*[@id="chips"]/yt-chip-cloud-chip-renderer[3]')
    LIST_BTN = (By.XPATH, '//button[@class ="style-scope yt-icon-button"and @aria-label="Action menu"]')
    UNDO_BTN = (By.XPATH,
                '/html/body/ytd-app/ytd-popup-container/yt-notification-action-renderer[1]/tp-yt-paper-toast/yt-button-renderer/yt-button-shape/button')
    QUEUE_H = (By.XPATH,
               '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[1]/div[1]/h3[1]/yt-formatted-string')

    def add_videos_to_queue(self, number_of_videos):
        try:
            cm_to_inches = 6 / 2.54  # Calculate approximate scroll distance in pixels
            cm_to_inches2 = 0.22 / 2.54  # Calculate approximate scroll distance in pixels
            dpi = 100  # Example DPI, replace with actual DPI
            scroll_distance_inches = cm_to_inches
            scroll_distance_pixels = int(scroll_distance_inches * dpi)
            scroll_distance_pixels2 = int((cm_to_inches2 + 1) * dpi)
            # Scroll the page by the calculated amount
            self.wait_condition.until(EC.element_to_be_clickable(self.OLDEST_BTN)).click()
            button_list = self.browser_driver.find_elements(*self.LIST_BTN)
            for button in range(number_of_videos):
                WebDriverWait(self.browser_driver, 20).until(EC.element_to_be_clickable(button_list[button])).click()
                WebDriverWait(self.browser_driver, 30).until(EC.element_to_be_clickable(self.ADD_TO_QUEUE)).click()
                if button == 0:
                    self.browser_driver.execute_script(f"window.scrollBy(0, {scroll_distance_pixels2});")
                if button % 4 == 0:
                    self.browser_driver.execute_script(f"window.scrollBy(0, {scroll_distance_pixels});")
            WebDriverWait(self.browser_driver, 50).until(EC.element_to_be_clickable(self.MINI_PLAYER_BTN)).click()
            self.wait_condition.until(EC.presence_of_element_located(self.QUEUE_H))
            result = (self.browser_driver.find_element(*self.NUM_OF_VIDEOS_IN_QUEUE)).text
            self.wait_condition.until(EC.element_to_be_clickable(self.CLEAR_BTN)).click()
            return result
        except Exception as e:
            print(f"An error occurred while sharing the video: {str(e)}")


            # WebDriverWait(self.browser_driver, 30).until(EC.invisibility_of_element_located(self.UNDO_BTN))

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from infra.page_base import WebPageBase
from selenium.webdriver import ActionChains


class YouTubeVideo(WebPageBase):
    FULL_SCREEN = (By.CSS_SELECTOR, "button.ytp-fullscreen-button")
    SOUND_TOGGLE = (By.CSS_SELECTOR, "button.ytp-mute-button")
    VIDEO_PLAY = (By.CSS_SELECTOR, "button.ytp-play-button")
    MINI_PLAYER_BUTTON = (By.CSS_SELECTOR, "button.ytp-miniplayer-button")
    MINI_PLAYER_EXPAND = (By.CSS_SELECTOR, ".ytp-miniplayer-expand-watch-page-button")
    VIDEO_IN_MINI_PLAYER_ELEMENT = (By.CLASS_NAME, "ytp-miniplayer-scrim")
    VIDEO_ELEMENT = (By.XPATH, "//video[@class = 'video-stream html5-main-video']")
    SHARE_BTN = (By.XPATH,
                 '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[2]/div/div/ytd-menu-renderer/div[1]/yt-button-view-model/button-view-model/button')
    SVG_WHATSAPP = (By.XPATH,
                    "//button[@title='WhatsApp']")
    SVG_FACEBOOK = (By.XPATH,
                    "//button[@title='Facebook']")

    def start_video(self):
        play_button = self.wait_condition.until(EC.element_to_be_clickable(self.VIDEO_PLAY))
        play_button.click()
        self.wait_condition.until(EC.element_to_be_clickable(self.VIDEO_PLAY))
        return True

    def change_sound_state(self):
        self.wait_condition.until(EC.element_to_be_clickable(self.SOUND_TOGGLE)).click()
        return self.video_is_muted()

    def video_is_muted(self):
        return self.browser_driver.execute_script("return document.querySelector('video').muted;")

    def activate_full_screen(self):
        full_screen_btn = self.wait_condition.until(EC.element_to_be_clickable(self.FULL_SCREEN))
        full_screen_btn.click()
        self.wait_condition.until(
            lambda d: self.browser_driver.execute_script("return document.fullscreenElement != null;"))

    def verify_full_screen(self):
        return self.browser_driver.execute_script("return document.fullscreenElement != null;")

    def deactivate_full_screen(self):
        if self.verify_full_screen():
            self.browser_driver.execute_script("document.exitFullscreen();")
            self.wait_condition.until(
                lambda d: self.browser_driver.execute_script("return document.fullscreenElement == null;"))

    def share_video(self, path):

        try:
            path_to_share = ""
            if path == "whatsapp":
                path_to_share = self.SVG_WHATSAPP
            elif path == "facebook":
                path_to_share = self.SVG_FACEBOOK

            self.wait_condition.until(EC.element_to_be_clickable(self.SHARE_BTN)).click()
            self.wait_condition.until(EC.presence_of_element_located(path_to_share))
            self.wait_condition.until(EC.element_to_be_clickable(path_to_share)).click()
            original_window = self.browser_driver.window_handles[0]
            WebDriverWait(self.browser_driver, 20).until(EC.element_to_be_clickable(path_to_share))
            WebDriverWait(self.browser_driver, 20).until(EC.number_of_windows_to_be(2))
            new_window = [window for window in self.browser_driver.window_handles if window != original_window][0]
            self.browser_driver.switch_to.window(new_window)
            new_page_url = self.browser_driver.current_url
            return new_page_url
        except Exception as e:
            print(f"An error occurred while sharing the video: {str(e)}")

    def check_full_screen_exit(self):
        return self.browser_driver.execute_script("return document.fullscreenElement == null;")

    def hover_on(self, direction):
        if direction == "expand_button":

            to_element = self.wait_condition.until(EC.presence_of_element_located(self.VIDEO_IN_MINI_PLAYER_ELEMENT))
        elif direction == "video":
            to_element = self.wait_condition.until(EC.element_to_be_clickable(self.VIDEO_ELEMENT))
        else:
            raise Exception

        actions = ActionChains(self.browser_driver)

        actions.move_to_element(to_element).perform()

    def use_miniplayer(self):
        self.start_video()
        self.hover_on("video")
        self.wait_condition.until(EC.element_to_be_clickable(self.MINI_PLAYER_BUTTON)).click()
        self.hover_on("expand_button")
        self.wait_condition.until(EC.visibility_of_element_located(self.MINI_PLAYER_EXPAND))
        return True

    def expand_from_miniplayer(self):
        """Return to the regular video view from miniplayer mode."""
        self.hover_on("expand_button")
        self.wait_condition.until(EC.element_to_be_clickable(self.MINI_PLAYER_EXPAND)).click()
        self.hover_on("video")
        self.wait_condition.until(EC.visibility_of_element_located(self.MINI_PLAYER_BUTTON))
        return True

import unittest
from infra.browser_wrapper import WebNavigator
from logic.youtube_video import YouTubeVideo


class VideoTests(unittest.TestCase):
    def setUp(self):
        self.navigator = WebNavigator()
        self.browser_driver = self.navigator.launch_browser(self.__class__.browser)
        self.wait_tool = self.navigator.fetch_wait()
        self.YouTubeVideo = YouTubeVideo(self.browser_driver, self.wait_tool)

    def test_video_playback(self):
        self.navigator.open_video()
        result = self.YouTubeVideo.start_video()
        self.assertTrue(result)
        result = self.YouTubeVideo.start_video()
        self.assertTrue(result)

    def test_full_screen_mode(self):
        self.navigator.open_video()
        self.YouTubeVideo.start_video()
        self.YouTubeVideo.activate_full_screen()
        self.assertTrue(self.YouTubeVideo.verify_full_screen(), "Video is not in full screen mode.")
        self.YouTubeVideo.deactivate_full_screen()
        self.assertTrue(self.YouTubeVideo.check_full_screen_exit(), "Video didn't exit from full screen mode.")

    def test_sound_toggle(self):
        self.navigator.open_video()
        self.YouTubeVideo.start_video()
        is_muted = self.YouTubeVideo.change_sound_state()
        self.assertTrue(is_muted, "Video is not muted.")
        is_muted = self.YouTubeVideo.change_sound_state()
        self.assertFalse(is_muted, "Video is not unmute.")

    def test_miniplayer_mode(self):
        """Test entering and exiting miniplayer mode."""
        self.browser_driver.maximize_window()
        self.navigator.open_video()
        self.YouTubeVideo.start_video()
        result = self.YouTubeVideo.use_miniplayer()
        self.assertTrue(result, "Miniplayer mode is not activated.")
        result = self.YouTubeVideo.expand_from_miniplayer()
        self.assertTrue(result, "The video successfully toggled miniplayer mode and returned direction full size.")
        self.assertTrue(result, "Video did not exit miniplayer mode.")

    def test_share_video_to_whatsapp(self):
        self.navigator.open_video()
        result = self.YouTubeVideo.share_video("whatsapp")
        self.assertIn("whatsapp", result, "Result does not contain WhatsApp")

    def test_share_video_to_facebook(self):
        self.navigator.open_video()
        result = self.YouTubeVideo.share_video("facebook")
        self.assertIn("facebook", result, "Result does not contain facebook")

    def tearDown(self):
        self.navigator.terminate_browser()

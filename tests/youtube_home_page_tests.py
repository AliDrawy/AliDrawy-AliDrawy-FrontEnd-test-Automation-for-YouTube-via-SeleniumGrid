import unittest
from infra.browser_wrapper import WebNavigator
from logic.youtube_home_page import YouTubeHomePage


class HomePage(unittest.TestCase):
    def setUp(self):
        self.navigator = WebNavigator()
        self.browser_driver = self.navigator.launch_browser(self.__class__.browser)
        self.wait_tool = self.navigator.fetch_wait()
        self.YouTubeHomePage = YouTubeHomePage(self.browser_driver, self.wait_tool)

    def test_theme_change_to_dark(self):
        self.YouTubeHomePage.modify_theme("Dark")
        is_theme_applied = self.YouTubeHomePage.confirm_theme("Dark")
        self.assertTrue(is_theme_applied)

    def test_theme_change_to_light(self):
        self.YouTubeHomePage.modify_theme("Light")
        is_theme_applied = self.YouTubeHomePage.confirm_theme("Light")
        self.assertTrue(is_theme_applied)

    def test_change_location(self):
        self.browser_driver.maximize_window()
        result = self.YouTubeHomePage.change_location("France")
        self.assertEqual("France", result, "Result does not match")
        result = self.YouTubeHomePage.change_location("Israel")
        self.assertEqual("Israel", result, "Result does not match")

    def tearDown(self):
        self.navigator.terminate_browser()

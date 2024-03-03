import unittest
from infra.browser_wrapper import WebNavigator
from logic.youtube_channel import YouTubeChannel


class ChannelTests(unittest.TestCase):

    def setUp(self):
        self.navigator = WebNavigator()
        self.browser_driver = self.navigator.launch_browser(self.__class__.browser)
        self.wait_tool = self.navigator.fetch_wait()
        self.YouTubeChannel = YouTubeChannel(self.browser_driver, self.wait_tool)

    def test_add_videos_to_queue(self):
        self.browser_driver.maximize_window()
        self.navigator.open_channel()
        number_of_videos_to_add_in_queue = 10
        number_of_videos_to_add_in_queue_as_string = str(number_of_videos_to_add_in_queue)
        result = self.YouTubeChannel.add_videos_to_queue(number_of_videos_to_add_in_queue)
        self.assertEqual(number_of_videos_to_add_in_queue_as_string, result[4:], "Result does not match")

    def tearDown(self):
        self.navigator.terminate_browser()

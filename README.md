YouTube Automation Project

This project aims to automate various actions and functionalities on the YouTube platform using Selenium WebDriver and Python. The project includes browser automation scripts, page objects, and test cases to verify the functionality of different features on YouTube, such as video playback, theme changes, adding videos to queue, and more.

Table of Contents
1-Project Overview
2-Project Structure
3-Setup and Installation
4-Usage

1. Project Overview

The project consists of several Python scripts organized into different modules:

browser_wrapper.py: Defines a class WebNavigator responsible for browser initialization and navigation.
page_base.py: Contains the WebPageBase class, which serves as the base class for all page objects.
logic/: Contains modules representing different functionalities on YouTube.
tests/: Includes test cases for verifying the functionalities defined in the logic modules.
run_all_tests.py: Script to run all test cases.

2. Project Structure

infra/
│
├── browser_wrapper.py
├── page_base.py
│
logic/
├── youtube_channel.py
├── youtube_home_page.py
├── youtube_video.py
│
tests/
├── run_all_tests.py
├── youtube_channel_tests.py
├── youtube_home_page_tests.py
├── youtube_video_tests.py

3. Setup and Installation
To set up the project and install dependencies, follow these steps:

1.Clone the repository to your local machine:
	git clone <repository_url>

2.Navigate to the project directory:
	cd <project_directory>

3.Install the required dependencies using pip:
	pip install selenium
	java -jar selenium-server-4.17.0.jar hub
	java -jar selenium-server-4.17.0.jar node --port 5555 --selenium manager true
	
4.Ensure you have the appropriate web drivers (e.g., ChromeDriver, GeckoDriver) installed and added to your system's PATH.

4-Usage
To run the test cases, execute the run_all_tests.py script:
	python run_all_tests.py

This script will execute all the test cases defined in the tests directory.
 You can also run individual test scripts if needed.

5. Contributing
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or create a pull request.
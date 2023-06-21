from src.resources.updownload.updownload_demoga_resources import *


class UpDownLoadPage:

    def __init__(self, browser):
        self.browser = browser

    def click_download(self):
        self.browser.find_element(*UpDownLoadResources.DOWNLOAD_BTN).click()

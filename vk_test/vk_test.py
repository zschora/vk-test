
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class Ppkt(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\chromedriver.exe')
        self.driver.get('https://www.vkostume.ru/')

    def tearDown(self):
        self.driver.close()


    def clikByXpath(self, xpath):
        el = self.driver.find_element_by_xpath(xpath)
        el.send_keys(Keys.ENTER)

    def hoverOverAnElementByXpath(self, xpath):
        el = self.driver.find_element_by_xpath(xpath)
        hover = ActionChains(self.driver).move_to_element(el)
        hover.perform()


    def test_1_1(self):
        self.clikByXpath('/html/body/div[5]/div[1]/div/div[1]/a')
        assert self.driver.current_url == r'https://www.vkostume.ru/catalog/kostyumy_dlya_zhenchin/'
    
        

unittest.main()
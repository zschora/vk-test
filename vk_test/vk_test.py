
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest

class Ppkt(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r'C:\chromedriver.exe')

    def setUp(self):
        self.driver.get('https://www.vkostume.ru/')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


    def clikByXpath(self, xpath):
        el = self.driver.find_element_by_xpath(xpath)
        el.send_keys(Keys.ENTER)

    def hoverOverAnElementByXpath(self, xpath):
        el = self.driver.find_element_by_xpath(xpath)
        hover = ActionChains(self.driver).move_to_element(el)
        hover.perform()


    def test_1_1(self):
        """
        Открытие категории “ЖЕНЩИНАМ”
        """

        self.clikByXpath('/html/body/div[5]/div[1]/div/div[1]/a')

        self.assertEqual(self.driver.current_url, r'https://www.vkostume.ru/catalog/kostyumy_dlya_zhenchin/')
    
    def test_1_2(self):
        """
        Перемещение в категории “ЖЕНЩИНАМ”.
        Открытие подкатегории “Многоразовые маски и антисептики”.
        """

        self.hoverOverAnElementByXpath('/html/body/div[5]/div[1]/div/div[1]/a')
        self.clikByXpath('/html/body/div[5]/div[1]/div/div[1]/div/div/div/div/div/ul/li[1]/a')

        self.assertEqual(self.driver.current_url, \
            r'https://www.vkostume.ru/catalog/kostyumy_dlya_zhenchin/mnogorazovye_maski_i_antiseptiki/')

    def test_1_3(self):
        """
        Перемещение в категории “ЖЕНЩИНАМ”.
        Открытие подкатегории “Костюмы”.
        """

        self.hoverOverAnElementByXpath('/html/body/div[5]/div[1]/div/div[1]/a')
        self.clikByXpath('/html/body/div[5]/div[1]/div/div[1]/div/div/div/div/div/ul/li[2]/a')

        self.assertEqual(self.driver.current_url, \
            r'https://www.vkostume.ru/catalog/kostyumy_dlya_zhenchin/Kostyumy/')

    def test_1_4(self):
        """
        Перемещение в категории “ЖЕНЩИНАМ”.
        Открытие подкатегории “Эротические костюмы”.
        """

        self.hoverOverAnElementByXpath('/html/body/div[5]/div[1]/div/div[1]/a')
        self.clikByXpath('/html/body/div[5]/div[1]/div/div[1]/div/div/div/div/div/ul/li[7]/a')

        self.assertEquals(self.driver.current_url, r'https://www.vkostume.ru/catalog/Eroticheskie/')

        
if __name__ == "__main__":
    unittest.main()
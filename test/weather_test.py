import allure

from unittest import TestCase
from library.httpclient import HttpClient


@allure.feature('Test Weather api')
class Weather(TestCase):
    """Weather api test cases"""

    def setUp(self):
        """Setup of the test"""

        self.host = 'http://www.weather.com.cn'
        self.ep_path = '/data/cityinfo'
        self.client = HttpClient()

    @allure.story('Test of HangZhou')
    @allure.severity(allure.severity_level.NORMAL)
    def test_weather_hangzhou(self):
        city_code = '101210101'
        exp_city = '杭州'
        self._test(city_code, exp_city)

    @allure.story('Test of FuYang')
    @allure.severity(allure.severity_level.MINOR)
    def test_weather_fuyang(self):
        city_code = '101220801'
        exp_city = '阜阳'
        self._test(city_code, exp_city)

    @allure.story('Test of NingBo')
    def test_weather_ningbo(self):
        city_code = '101210401'
        exp_city = '宁波'
        self._test(city_code, exp_city)

    @allure.story('Test of ShangHai')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_weather_shanghai(self):
        city_code = '101020100'
        exp_city = '上海'
        self._test(city_code, exp_city)

    @allure.story('Test of GuiYang')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_weather_guiyang(self):
        city_code = '101260101'
        exp_city = '贵阳'
        self._test(city_code, exp_city)

    def _test(self, city_code, exp_city):
        url = f'{self.host}{self.ep_path}/{city_code}.html'
        response = self.client.Get(url=url)
        act_city = response.json()['weatherinfo']['city']
        print(f'Expect city = {exp_city}, while actual city = {act_city}')
        # self.assertEqual(exp_city, act_city, f'Expect city = {exp_city}, while actual city = {act_city}')
        self.assertEqual(exp_city, act_city)
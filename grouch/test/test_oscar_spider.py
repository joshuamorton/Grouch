import scrapy
from grouch.spiders.oscar_spider import OscarSpider
import unittest
import response


class TestOscarSpider(unittest.TestCase):
    def setUp(self):
        self.response = scrapy.http.TextResponse("",body=response.resp)
        self.spider = OscarSpider()

    def test_parse_detail(self):
        item = self.spider.parse_detail(self.response)
        self.assertEqual(item['fields'], ["Grade Basis", "Restrictions", "Prerequisites"])
        self.assertEqual(item['fullname'][0], "CS 1332 - Data Struct & Algorithms")
        self.assertEqual(item['name'][0], "Data Struct & Algorithms")
        self.assertEqual(item['school'][0], "CS")
        self.assertEqual(item['number'][0], "1332")
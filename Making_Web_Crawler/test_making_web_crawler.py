import unittest

import Making_Web_Crawler.making_web_crawler as mwc

class TestMakingWebCrawler(unittest.TestCase):

    def test_001_get_next_target(self):
        self.assertEqual(('http://udacity.com', 116), mwc.get_next_target('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">'))

    def test_002_add_to_index(self):
    #     from Making_Web_Crawler.making_web_crawler import index
        index = []
        self.assertEqual((index == [['udacity', ['http://udacity.com']]]), mwc.add_to_index(index,'udacity','http://udacity.com'))


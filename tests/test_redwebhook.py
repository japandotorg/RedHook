import unittest
from RedWebhook import RedWebhook

class TestLemonApi(unittest.TestCase):
    """ Tests to exercise webhooks """
    
    def test_redwebhook_constructor(self):
        webhook = RedWebhook("testurl")
        self.assertEqual(webhook.url, "testurl")
        
    def test_set_content(self):
        test_content = "Test data"
        webhook = RedWebhook("testurl")
        webhook.set_content(test_content)
        self.assertEqual(webhook.url, test_content)
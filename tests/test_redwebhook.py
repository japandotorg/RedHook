import unittest
from RedWebhook import RedHook

class TestLemonApi(unittest.TestCase):
    """ Tests to exercise webhooks """
    
    def test_redwebhook_constructor(self):
        webhook = RedHook("testurl")
        self.assertEqual(webhook.url, "testurl")
        
    def test_set_content(self):
        test_content = "Test data"
        webhook = RedHook("testurl")
        webhook.set_content(test_content)
        self.assertEqual(webhook.url, test_content)
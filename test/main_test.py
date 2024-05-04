import unittest
from utils import Utils

class MenuHandlerTest(unittest.TestCase):

    def test_empty_json(self):

        res = Utils.menu_handler(stage='1')

        self.assertEqual(res, (0, 0, 0))

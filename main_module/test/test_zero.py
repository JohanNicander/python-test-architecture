import unittest
import main_module


class TestZero(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(main_module.zero(), 0)

import unittest
import main_module.submodule1


class TestZero(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(main_module.submodule1.one(), 1)

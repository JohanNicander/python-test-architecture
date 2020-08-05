import unittest
import main_module.submodule2


class TestZero(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(main_module.submodule2.two(), 2)

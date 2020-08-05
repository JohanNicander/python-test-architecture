import sys
import os

__all__ = ['UnitTester']

class UnitTester:

    def __init__(self, module_name):
        self.module_name = module_name

    def __call__(self, *args, **kwargs):

        import unittest
        from unittest import main, defaultTestLoader
        # import warnings

        module = sys.modules[self.module_name]
        base_module = sys.modules["main_module"]
        base_module_path = os.path.abspath(base_module.__path__[0])
        module_path = os.path.relpath(module.__path__[0], base_module_path)
        test_path = os.path.join(base_module_path, "tests", module_path)

        tests = defaultTestLoader.discover(test_path)
        textTestRunner = unittest.TextTestRunner(*args, **kwargs)
        textTestResult = textTestRunner.run(tests)

        return textTestResult.wasSuccessful()
import sys
import os

__all__ = ['UnitTester']

class UnitTester:

    def __init__(self, module_name):
        self.module_name = module_name

    def __call__(self):

        from stestr.commands import run_command
        # import warnings

        module = sys.modules[self.module_name]
        base_module = sys.modules["main_module"]
        base_module_path = os.path.abspath(base_module.__path__[0])
        module_path = os.path.relpath(module.__path__[0], base_module_path)
        test_path = os.path.join(base_module_path, "tests", module_path)
        # cwd = os.getcwd()
        # os.chdir(test_path)

        stestr_args = {
            "test_path": test_path,
            "top_dir": test_path,
            "group_regex": r"([^\.]*\.)*",
        }

        try:
            code = run_command(**stestr_args)
        except SystemExit as exc:
            code = exc.code
        # finally:
        #     os.chdir(cwd)

        return code == 0
        # return 0

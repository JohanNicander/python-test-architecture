import sys
import os

__all__ = ['UnitTester']


class UnitTester:

    def __init__(self, module_name):
        self.module_name = module_name

    def __call__(self, color=False):

        from stestr.commands import run_command
        # import warnings

        module = sys.modules[self.module_name]
        module_path = os.path.abspath(module.__path__[0])
        cwd = os.getcwd()
        os.chdir(module_path)

        stestr_args = {
            "test_path": module_path,
            "top_dir": module_path,
            "group_regex": r"([^\.]*\.)*",
            "color": color,
        }

        try:
            code = run_command(**stestr_args)
        except SystemExit as exc:
            code = exc.code
        finally:
            os.chdir(cwd)

        return code == 0
        # return 0

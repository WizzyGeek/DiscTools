from os.path import abspath
from sys import argv
from sys import path as spath

try:
    import disctools
except ModuleNotFoundError:
    local = True
else:
    local = False
    del disctools

def load_tests(loader, *args):
    if ("--local" in argv) or local:
        spath.insert(0, abspath("."))
        print("Testing local disctools package")

    return loader.loadTestsFromNames(
            ["tests.test_bot",
            "tests.test_cmd",
            "tests.test_context"]
        )

import importlib
from sys import argv, exc_info, exit
from traceback import print_exception, print_tb

if __name__ == "__main__":
    args = argv[1:]
    module_name = args[0]

    try:
        module = importlib.import_module(module_name)
        module.run()

        exit()

    except Exception as ex:
        tb = exc_info()[2]
        print_tb(tb)

        exit(f"could not open module: {module_name}")

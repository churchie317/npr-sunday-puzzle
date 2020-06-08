import importlib
from sys import argv, exit

if __name__ == "__main__":
    args = argv[1:]
    module_name = args[0]

    try:
        module = importlib.import_module(module_name)
        module.run()

    except Exception as ex:
        exit(f"could not open module: {module_name}")

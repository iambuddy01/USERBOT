import os
import importlib

def load_modules(base_package: str):
    base_dir = os.path.dirname(__file__)

    for file in os.listdir(base_dir):
        if file.endswith(".py") and not file.startswith("__"):

            module_name = file[:-3]
            full_module = f"{base_package}.modules.{module_name}"

            importlib.import_module(full_module)

            print(f"✅ Loaded → {full_module}")

load_modules("Aayein")

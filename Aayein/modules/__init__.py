import os
import importlib


def load_modules(base_package: str):
    """
    Dynamically import all modules inside this directory.
    """

    base_dir = os.path.dirname(__file__)

    for root, _, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith(".py") and not filename.startswith("__"):

                rel_path = os.path.relpath(
                    os.path.join(root, filename), base_dir
                )

                module_path = rel_path.replace(os.sep, ".").replace(".py", "")

                full_module = f"{base_package}.modules.{module_path}"

                importlib.import_module(full_module)

                print(f"✅ Loaded → {full_module}")


load_modules("Aayein")

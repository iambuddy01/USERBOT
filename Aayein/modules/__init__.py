import os
import importlib

print("📦 Loading Modules from Aayein/modules")

BASE_DIR = os.path.dirname(__file__)

for file in os.listdir(BASE_DIR):
    if file.endswith(".py") and not file.startswith("__"):
        module = file[:-3]

        importlib.import_module(f"Aayein.modules.{module}")

        print(f"✅ Loaded → Aayein.modules.{module}")

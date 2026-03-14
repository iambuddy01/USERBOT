import importlib
import pkgutil

package = __name__

for _, module_name, _ in pkgutil.walk_packages(__path__, package + "."):
    importlib.import_module(module_name)
    print(f"✅ Loaded → {module_name}")

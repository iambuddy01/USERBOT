import os
import importlib

def load_modules(base_package: str):
    """
    Dynamically imports all Python modules in the current package/directory.
    
    Args:
        base_package (str): The base package name to use for imports (e.g., 'Nexa').
    """
    base_dir = os.path.dirname(file)

    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".py") and not file.startswith("__"):
                # Get the relative path from base_dir
                rel_path = os.path.relpath(os.path.join(root, file), base_dir)
                # Convert to module path
                module_path = rel_path.replace(os.sep, ".").replace(".py", "")
                full_module = f"{base_package}.{module_path}"

                # Import the module
                importlib.import_module(full_module)
                print(f"✅ Loaded → {full_module}")

# Example usage:
load_modules("Aayein")

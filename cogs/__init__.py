import os

def list_cogs():
    return [
        f"cogs.{f[:-3]}"
        for f in os.listdir(os.path.dirname(__file__))
        if f.endswith(".py") and f != "__init__.py"
    ]
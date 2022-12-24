


import glob
from pathlib import Path
from PY.utils import load_plugins
import logging
from PY import PY

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

path = "PY/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("Successfully Started Bot!")
print("Visit @tr4shcode")

if __name__ == "__main__":
    PY.run_until_disconnected()

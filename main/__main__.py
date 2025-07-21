import glob
from pathlib import Path
import logging
from main.utils import load_plugins
import threading
from health_check import start_health_check
from main import run_main

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")
print("By MaheshChauhan • DroneBots")

if __name__ == "__main__":
    threading.Thread(target=start_health_check, daemon=True).start()
    run_main()  # Start bot + userbot from __init__.py

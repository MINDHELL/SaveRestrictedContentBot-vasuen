import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from main import bot
import threading
from health_check import start_health_check

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

#Don't be a thief 
print("Successfully deployed!")
print("By MaheshChauhan • DroneBots")

if __name__ == "__main__":
    threading.Thread(target=start_health_check, daemon=True).start()
    bot.run()

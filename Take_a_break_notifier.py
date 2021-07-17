import time
from plyer import *
period  = int(input())
if __name__ == "__main__":
        while True:
                notification.notify(
                    title = "Please Take a Break...",
                    message = "By taking a break in every "+str(period)+" minute from your work keeps you healthy , and more work-efficient",
                    app_icon = "C:/Users/LENOVO/Desktop/Rest.ico",
                    timeout = 10
                )
                time.sleep(period*60)

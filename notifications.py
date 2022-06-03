import time
from plyer import notification

if __name__ == '__main__':
    while True:
        notification.notify(
            title = "notification", 
            message = "i'm sending you a notification",
            # time it stays on the screen
            timeout = 10
        )
        # time between messages
        time.sleep(15)

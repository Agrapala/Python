from player import notifications
import time

if __name__ == '__main__':
    while True:
        notifications.notify(
            title="*** Whatapp ***",
            message="You have received messages from your GF",
            app_icon = "C:/Users/samit/Desktop",
            timeout=5)
        time.sleep(20)
    
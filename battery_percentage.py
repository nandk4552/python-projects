from plyer import notification
import time

battery = psutil.sensors_battery()

while (True) :

percent = battery.percent
notification.notify(title = "Battery Percent")
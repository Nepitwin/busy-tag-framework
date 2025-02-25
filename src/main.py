from serial_operations import find_all_busy_tag_devices
from led import Led
from busy_api import BusyApi

devices = find_all_busy_tag_devices()
if not devices:
    print("No devices found.")
    exit()

print(devices)

with BusyApi(devices[0]) as busy_api:
    busy_api.set_solid_color(Led.LeftTop | Led.MiddleTop | Led.RightTop | Led.LeftMiddle | Led.RightMiddle | Led.LeftBottom | Led.RightBottom, "00FF00")
    busy_api.set_showing_picture("hello_ez.gif")
    busy_api.set_brightness(100)

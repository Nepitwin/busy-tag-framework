from busy_tag_framework import serial_operations
from busy_tag_framework.busy_api import BusyApi
from busy_tag_framework.led import Led

devices = serial_operations.find_all_busy_tag_devices()
if not devices:
    print("No devices found.")
    exit()

print(devices)

with BusyApi(devices[0]) as busy_api:
    # Get Commands
    print(busy_api.get_device_name())
    print(busy_api.get_manufacture_name())
    print(busy_api.get_device_id())
    print(busy_api.get_firmware_version())
    print(busy_api.get_picture_list())
    print(busy_api.get_file_list())
    print(busy_api.get_local_host_address())
    print(busy_api.get_free_storage_size())
    print(busy_api.get_total_storage_size())
    print(busy_api.get_used_storage())

    # Set and Get Commands
    busy_api.set_solid_color(Led.LeftTop | Led.MiddleTop | Led.RightTop | Led.LeftMiddle | Led.RightMiddle | Led.LeftBottom | Led.RightBottom, "00FF00")
    print(busy_api.get_solid_color())

    busy_api.set_display_brightness(100)
    print(busy_api.get_display_brightness())

    busy_api.set_showing_picture("hello_ez.gif")
    print(busy_api.get_showing_picture())

    print(busy_api.get_show_after_drop())

    print(busy_api.get_allowed_web_file_server())

    print(busy_api.get_wifi_config())

    print(busy_api.get_usb_mass_storage_allowed())

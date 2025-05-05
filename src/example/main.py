from busy_tag_framework import serial_operations
from busy_tag_framework.busy_api import BusyApi
from busy_tag_framework.command import Command
from busy_tag_framework.led import Led

devices = serial_operations.find_all_busy_tag_devices()
if not devices:
    print("No devices found.")
    exit()

print(devices)

with BusyApi(devices[0]) as busy_api:
    # Get Commands
    print(busy_api.get_command(Command.GetDeviceName))
    print(busy_api.get_command(Command.GetManufactureName))
    print(busy_api.get_command(Command.GetDeviceId))
    print(busy_api.get_command(Command.GetFirmwareVersion))
    print(busy_api.get_command(Command.GetPictureList))
    print(busy_api.get_command(Command.GetFileList))
    print(busy_api.get_command(Command.GetLocalHostAddress))
    print(busy_api.get_command(Command.GetFreeStorageSize))
    print(busy_api.get_command(Command.GetTotalStorageSize))
    print(busy_api.get_used_storage())

    # Set and Get Commands
    busy_api.set_solid_color(Led.LeftTop | Led.MiddleTop | Led.RightTop | Led.LeftMiddle | Led.RightMiddle | Led.LeftBottom | Led.RightBottom, "00FF00")
    print(busy_api.get_command(Command.GetSolidColor))

    busy_api.set_display_brightness(100)
    print(busy_api.get_command(Command.GetDisplayBrightness))

    busy_api.set_showing_picture("hello_ez.gif")
    print(busy_api.get_command(Command.GetShowingPicture))

    print(busy_api.get_command(Command.GetShowAfterDrop))

    print(busy_api.get_command(Command.GetAllowedWebFileServer))

    print(busy_api.get_command(Command.GetWifiConfig))

    print(busy_api.get_command(Command.GetUsbMassStorageAllowed))

import sys

from busy_tag_framework.busy import Busy
from busy_tag_framework import serial_operations
from busy_tag_framework.busy_api import BusyApi
from busy_tag_framework.busy_exception import BusyException
from busy_tag_framework.busy_command import BusyCommand
from busy_tag_framework.led import Led

devices = serial_operations.find_all_busy_tag_devices()
if not devices:
    print("No devices found.")
    sys.exit(0)

print(devices)

# Error code conversion as enum
print(Busy.get_last_error_code(-1))
print(Busy.get_last_error_code(0))
print(Busy.get_last_error_code(1))
print(Busy.get_last_error_code(2))
print(Busy.get_last_error_code(3))
print(Busy.get_last_error_code(4))
print(Busy.get_last_error_code(1337))

# Get last reset code as enum
print(Busy.get_last_reset_code(1))
print(Busy.get_last_reset_code(3))
print(Busy.get_last_reset_code(5))
print(Busy.get_last_reset_code(6))
print(Busy.get_last_reset_code(7))
print(Busy.get_last_reset_code(8))
print(Busy.get_last_reset_code(9))
print(Busy.get_last_reset_code(11))
print(Busy.get_last_reset_code(12))
print(Busy.get_last_reset_code(13))
print(Busy.get_last_reset_code(14))
print(Busy.get_last_reset_code(15))
print(Busy.get_last_reset_code(16))
print(Busy.get_last_reset_code(0))

with BusyApi(devices[0]) as busy_api:
    # Get Commands
    print(f"GetDeviceName: {busy_api.get_command(BusyCommand.GetDeviceName)}")
    print(f"GetManufactureName: {busy_api.get_command(BusyCommand.GetManufactureName)}")
    print(f"GetDeviceId: {busy_api.get_command(BusyCommand.GetDeviceId)}")
    print(f"GetFirmwareVersion: {busy_api.get_command(BusyCommand.GetFirmwareVersion)}")
    print(f"GetPictureList: {busy_api.get_command(BusyCommand.GetPictureList)}")
    print(f"GetFileList: {busy_api.get_command(BusyCommand.GetFileList)}")
    print(f"GetLocalHostAddress: {busy_api.get_command(BusyCommand.GetLocalHostAddress)}")
    print(f"GetFreeStorageSize: {busy_api.get_command(BusyCommand.GetFreeStorageSize)}")
    print(f"GetTotalStorageSize: {busy_api.get_command(BusyCommand.GetTotalStorageSize)}")
    print(f"UsedStorage: {busy_api.get_used_storage()}")

    # Set and Get Commands
    print(f"SetSolidColor: {busy_api.set_command(BusyCommand.SetSolidColor, {'led_bits': Led.LeftTop | Led.MiddleTop | Led.RightTop | Led.LeftMiddle | Led.RightMiddle | Led.LeftBottom | Led.RightBottom, 'color_hex': '00FF00'})}")
    print(f"GetSolidColor: {busy_api.get_command(BusyCommand.GetSolidColor)}")

    print(f"SetDisplayBrightness: {busy_api.set_command(BusyCommand.SetDisplayBrightness, {'brightness': 100})}")
    print(f"GetDisplayBrightness: {busy_api.get_command(BusyCommand.GetDisplayBrightness)}")

    print(f"SetShowingPicture: {busy_api.set_command(BusyCommand.SetShowingPicture, {'filename': 'hello_ez.gif'})}")
    print(f"GetShowingPicture: {busy_api.get_command(BusyCommand.GetShowingPicture)}")

    print(f"SetShowAfterDrop: {busy_api.set_command(BusyCommand.SetShowAfterDrop, {'active': 0})}")
    print(f"GetShowAfterDrop: {busy_api.get_command(BusyCommand.GetShowAfterDrop)}")
    print(f"SetShowAfterDrop: {busy_api.set_command(BusyCommand.SetShowAfterDrop, {'active': 1})}")
    print(f"GetShowAfterDrop: {busy_api.get_command(BusyCommand.GetShowAfterDrop)}")

    # This command force a reconnection to the device. Afterwards the device must be reinitialized.
    #print(f"SetAllowedWebFileServer: {busy_api.set_command(BusyCommand.SetAllowedWebFileServer, {'active': 1})}")
    #print(f"GetAllowedWebFileServer: {busy_api.get_command(BusyCommand.GetAllowedWebFileServer)}")
    #print(f"SetAllowedWebFileServer: {busy_api.set_command(BusyCommand.SetAllowedWebFileServer, {'active': 0})}")
    print(f"GetAllowedWebFileServer: {busy_api.get_command(BusyCommand.GetAllowedWebFileServer)}")

    print(f"SetWifiConfig: {busy_api.set_command(BusyCommand.SetWifiConfig, {'ssid': 'my_ssid', 'password': 'my_password'})}")
    print(f"GetWifiConfig: {busy_api.get_command(BusyCommand.GetWifiConfig)}")

    #print(f"SetUsbMassStorageAllowed: {busy_api.set_command(BusyCommand.SetUsbMassStorageAllowed, {'active': 0})}")
    #print(f"GetUsbMassStorageAllowed: {busy_api.get_command(BusyCommand.GetUsbMassStorageAllowed)}")
    # This command force a reconnection to the device. Afterwards the device must be reinitialized.
    # print(f"SetUsbMassStorageAllowed: {busy_api.set_command(BusyCommand.SetUsbMassStorageAllowed, {'active': 1})}")
    print(f"GetUsbMassStorageAllowed: {busy_api.get_command(BusyCommand.GetUsbMassStorageAllowed)}")

    # TODO Set
    print(f"GetLastErrorCode: {busy_api.get_command(BusyCommand.GetLastErrorCode)}")

    try:
        print(f"GetLastResetReasonForCoreZero: {busy_api.get_command(BusyCommand.GetLastResetReasonForCoreZero)}")
    except BusyException as e:
        print(f"Error: {e}")

    try:
        print(f"GetLastResetReasonForCoreOne: {busy_api.get_command(BusyCommand.GetLastResetReasonForCoreOne)}")
    except BusyException as e:
        print(f"Error: {e}")

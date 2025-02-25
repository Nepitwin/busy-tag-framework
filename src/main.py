from serial_operations import find_all_busy_tag_devices, open_serial_connection, send_serial_command, close_serial_connection
from commands import Commands

devices = find_all_busy_tag_devices()
print(devices)
ser = open_serial_connection(devices[0]["port"])
print(send_serial_command(ser, Commands.GetDeviceId))
print(send_serial_command(ser, Commands.GetFirmwareVersion))
print(send_serial_command(ser, Commands.GetFreeStorageSize))
print(send_serial_command(ser, Commands.GetTotalStorageSize))
print(send_serial_command(ser, Commands.WifiConfig))
print(send_serial_command(ser, Commands.SolidColor))
print(send_serial_command(ser, Commands.DisplayBrightness))
close_serial_connection(ser)

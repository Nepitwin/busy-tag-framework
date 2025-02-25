from commands import Commands
import serial
import re

class BusyApi:

    def __init__(self, busy_device:dict):
        self._port = busy_device["port"]
        self._device = busy_device["device"]
        self._busy_tag_serial = None

    def __enter__(self):
        self._busy_tag_serial = self._open_serial_connection(self._port)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._close_serial_connection(self._busy_tag_serial)

    def set_solid_color(self, led_bits:int, color_hex:str) -> bool:
        if not self._is_valid_hex_color(color_hex):
            # TODO ERROR HANDLING
            print("Invalid color format.")
            return False

        command = Commands.SetSolidColor.format(led_bits=led_bits, color_hex=color_hex)
        response = self._send_serial_command(command.encode())
        print(response)
        # TODO ERROR HANDLING
        return True

    def get_solid_color(self) -> str or None:
        # TODO : Implement
        command = Commands.GetSolidColor
        response = self._send_serial_command(command.encode())
        # TODO ERROR HANDLING
        return response

    @staticmethod
    def _is_valid_hex_color(color):
        return bool(re.fullmatch(r"#?[0-9A-Fa-f]{6}|#?[0-9A-Fa-f]{3}", color))

    def _send_serial_command(self, command: bytes) -> str or None:
        try:
            if self._busy_tag_serial and self._busy_tag_serial.is_open:
                self._busy_tag_serial.write(command)
                self._busy_tag_serial.flush()
                return self._busy_tag_serial.readline().decode().strip()
            else:
                # TODO ERROR HANDLING
                print("Serial connection is not open.")
                return None
        except serial.SerialException as e:
            # TODO ERROR HANDLING
            print(f"Failed to send command: {e}")
            return None

    @staticmethod
    def _open_serial_connection(port:str, baudrate:int=115200) -> serial or None:
        try:
            ser = serial.Serial(port, baudrate, timeout=1)
            return ser
        except serial.SerialException as e:
            # TODO ERROR HANDLING
            print(f"Failed to open serial connection: {e}")
            return None

    @staticmethod
    def _close_serial_connection(ser: serial) -> None:
        if ser and ser.is_open:
            ser.close()
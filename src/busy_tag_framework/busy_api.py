import serial
import re
import math

from busy_tag_framework.busy_command import BusyCommand
from busy_tag_framework.busy_return_type import BusyReturnType
from busy_tag_framework.command import Command
from busy_tag_framework.busy_exception import BusyException
from busy_tag_framework.error_code import ErrorCode
from packaging import version


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

    def get_command(self, command: BusyCommand) -> str or list[str] or int or tuple[str, str] or None:
        """
        Executes a GET command and returns the result.

        Args:
            command (BusyCommand): The command to execute. Must be a GET command.

        Returns:
            str: The result as a string if the return type is STRING.
            list[str]: A list of strings if the return type is LIST.
            int: The result as an integer if the return type is NUMBER.
            tuple[str, str]: A tuple of two strings if the return type is TUPLE.
            None: If the command does not return a value.

        Raises:
            BusyException: If the result could not be received or parsed.
        """

        if command.min_firmware_version is not None:
            min_firmware_version =  version.parse(command.min_firmware_version)
            firmware_version = version.parse(self.get_command(Command.GetFirmwareVersion))
            if firmware_version < min_firmware_version:
                clean_command = command.action.rstrip('\r\n')
                raise BusyException(f"Command {clean_command} requires firmware version {command.min_firmware_version} or higher, but current version is {firmware_version}.", ErrorCode.FIRMWARE_VERSION_TOO_LOW)

        if command.return_type == BusyReturnType.NUMBER:
            result = self._get_result(command.action.encode(), command.regex, command.error_msg, command.error_code)
            return int(result) if result is not None else None

        elif command.return_type == BusyReturnType.TUPLE:
            result = self._get_result(command.action.encode(), command.regex, command.error_msg, command.error_code)
            if result:
                match = re.match(r'(.*?),(.*)', result)
                if match:
                    one, two = match.groups()
                    return one.strip(), two.strip()

            return None

        elif command.return_type == BusyReturnType.LIST:
            return self._get_list(command.action.encode(), command.regex, command.error_msg, command.error_code)

        return self._get_result(command.action.encode(), command.regex, command.error_msg, command.error_code)

    def get_used_storage(self) -> int:
        """
        Get the percentage of used storage space.

        Returns:
            int: The percentage of used storage space, rounded up, clamped between 0 and 100.

        Raises:
            BusyException: If the free or total storage size could not be received from response.
        """
        total_storage = self.get_command(Command.GetTotalStorageSize)
        free_storage = self.get_command(Command.GetFreeStorageSize)
        used_storage = total_storage - free_storage
        used_percentage = (used_storage / total_storage) * 100
        return int(min(100, max(0, math.ceil(used_percentage))))

    # Set Commands
    def set_solid_color(self, led_bits:int, color_hex:str) -> bool:
        if not self._is_valid_hex_color(color_hex):
            # TODO ERROR HANDLING
            print("Invalid color format.")
            return False

        command = Command.SetSolidColor.format(led_bits=led_bits, color_hex=color_hex)
        response = self._send_serial_command(command.encode())
        print(response)
        # TODO ERROR HANDLING
        return True

    def set_showing_picture(self, filename:str) -> bool:
        # TODO : Implement
        command = Command.SetShowingPicture.format(filename=filename)
        response = self._send_serial_command(command.encode())
        print(response)
        # TODO ERROR HANDLING
        return True

    def set_display_brightness(self, brightness:int) -> bool:
        # TODO : Implement
        command = Command.SetDisplayBrightness.format(brightness=brightness)
        response = self._send_serial_command(command.encode())
        print(response)
        # TODO ERROR HANDLING
        return True

    def set_show_after_drop(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def set_allowed_web_file_server(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def set_wifi_config(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def set_usb_mass_storage_allowed(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def set_custom_pattern(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def get_custom_pattern(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def set_allowed_auto_storage_scan(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def get_allowed_auto_storage_scan(self) -> int or None:
        # TODO : Implement me
        raise NotImplementedError

    # Actions

    def get_file(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def upload_file(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def delete_file(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def restart_device(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def format_disk(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def activate_file_storage_scan(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def factory_reset_main_config_file(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def factory_reset_wifi_config_file(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def factory_reset_default_image(self) -> None:
        # TODO : Implement me
        raise NotImplementedError

    def _get_result(self, command: bytes, regex: str, error_message: str, error_code: ErrorCode) -> str:
        """
        Sends a command and parses the response using the given regular expression.

        Args:
            command (bytes): The command to send.
            regex (str): The regular expression to use for parsing the response.
            error_message (str): The error message to raise if the response is not found.
            error_code (ErrorCode): The error code to raise if the response is not found.

        Returns:
            str: The parsed response if found.

        Raises:
            BusyException: If the response could not be received or parsed.
        """
        result = self._get_response_from_regexp(command, regex)
        if result:
            return result
        raise BusyException(error_message, error_code)

    def _get_list(self, command: bytes, regex: str, error_message: str, error_code: ErrorCode) -> list[str]:
        """
        Sends a command to the device, parses the response using the given regular expression, and returns a list of matches.

        Args:
            command (str): The command to send to the device.
            regex (str): The regular expression to use for parsing the response.
            error_message (str): The error message to raise if the response is not found.
            error_code (ErrorCode): The error code to raise if the response is not found.

        Returns:
            list[str]: A list of strings that match the regular expression in the response.

        Raises:
            BusyException: If the response could not be received or parsed.
        """
        response = self._send_serial_command(command)
        if not response:
            raise BusyException(error_message, error_code)

        result_list = []
        for line in response:
            match = re.search(regex, line.decode('utf-8'))
            if match:
                result_list.append(match.group(1))

        return result_list

    def _get_response_from_regexp(self, command: bytes, regex: str) -> str or None:
        """
        Sends a command and parses the response using the given regular expression.

        Args:
            command (bytes): The command to send.
            regex (str): The regular expression to use for parsing the response.

        Returns:
            str: The parsed response if found, otherwise None.
        """
        response = self._send_serial_command(command)
        if response:
            match = re.search(regex, response[0].decode('utf-8'))
            if match:
                return match.group(1)
        return None

    def _send_serial_command(self, command: bytes) -> list[bytes] or None:
        try:
            if self._busy_tag_serial and self._busy_tag_serial.is_open:
                self._busy_tag_serial.write(command)
                self._busy_tag_serial.flush()
                return self._busy_tag_serial.readlines()
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

    @staticmethod
    def _is_valid_hex_color(color):
        return bool(re.fullmatch(r"#?[0-9A-Fa-f]{6}|#?[0-9A-Fa-f]{3}", color))

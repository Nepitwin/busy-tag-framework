import serial
import re
import math

from busy_tag_framework.commands import Commands
from busy_tag_framework.busy_exception import BusyException
from busy_tag_framework.error_code import ErrorCode


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

    # Get Commands
    def get_device_name(self) -> str:
        """
        Get the device name from busy tag device.

        Returns:
            str: The busy tag device name.

        Raises:
            BusyException: If the device name could not be received from response.
        """
        return self._get_result(Commands.GetDeviceName.encode(),
                                r'\+DN:(.*)',
                                "Device name not found",
                                ErrorCode.DEVICE_NAME_NOT_FOUND)

    def get_manufacture_name(self) -> str:
        """
        Get the manufacture name.

        Returns:
            str: The manufacture name.

        Raises:
            BusyException: If the manufacture name could not be received from response.
        """
        return self._get_result(Commands.GetManufactureName.encode(),
                                r'\+MN:(.*)',
                                "Manufacture name not found",
                                ErrorCode.MANUFACTURE_NAME_NOT_FOUND)

    def get_device_id(self) -> str:
        """
        Get the device ID.

        Returns:
            str: The device ID.

        Raises:
            BusyException: If the device ID could not be received from response.
        """
        return self._get_result(Commands.GetDeviceId.encode(),
                                r'\+ID:(.*)',
                                "Device ID not found",
                                ErrorCode.DEVICE_ID_NOT_FOUND)

    def get_firmware_version(self) -> str:
        """
        Get the firmware version.

        Returns:
            str: The firmware version.

        Raises:
            BusyException: If the firmware version could not be received from response.
        """
        return self._get_result(Commands.GetFirmwareVersion.encode(),
                                r'\+FV:(.*)',
                                "Firmware version not found",
                                ErrorCode.FIRMWARE_VERSION_NOT_FOUND)

    def get_picture_list(self) -> list[str]:
        """
        Get the list of picture names.

        Returns:
            list[str]: The list of picture names.

        Raises:
            BusyException: If the picture list could not be received from response.
        """
        return self._get_list(Commands.GetPictureList,
                              r'\+PL:(.*?),\d+',
                              "Picture list not found",
                              ErrorCode.PICTURE_LIST_NOT_FOUND)

    def get_file_list(self) -> list[str]:
        """
        Get the list of file names.

        Returns:
            list[str]: The list of file names.

        Raises:
            BusyException: If the file list could not be received from response.
        """
        return self._get_list(Commands.GetFileList,
                              r'\+FL:(.*?),file,\d+',
                              "File list not found",
                              ErrorCode.FILE_LIST_NOT_FOUND)

    def get_local_host_address(self) -> str:
        """
        Get the local host address.

        Returns:
            str: The local host address.

        Raises:
            BusyException: If the local host address could not be received from response.
        """
        return self._get_result(Commands.GetLocalHostAddress.encode(),
                                r'\+LHA:(.*)',
                                "Local host address not found",
                                ErrorCode.LOCAL_HOST_ADDRESS_NOT_FOUND)

    def get_free_storage_size(self) -> int:
        """
        Get the free storage size.

        Returns:
            int: The free storage size in bytes.

        Raises:
            BusyException: If the free storage size could not be received from response.
        """
        result = self._get_result(Commands.GetFreeStorageSize.encode(),
                                  r'\+FSS:(\d+)',
                                  "Free storage size not found",
                                  ErrorCode.FREE_STORAGE_SIZE_NOT_FOUND)
        return int(result)

    def get_total_storage_size(self) -> int:
        """
        Get the total storage size.

        Returns:
            int: The total storage size in bytes.

        Raises:
            BusyException: If the total storage size could not be received from response.
        """
        result = self._get_result(Commands.GetTotalStorageSize.encode(),
                                  r'\+TSS:(\d+)',
                                  "Total storage size not found",
                                  ErrorCode.TOTAL_STORAGE_SIZE_NOT_FOUND)
        return int(result)

    def get_used_storage(self) -> int:
        """
        Get the percentage of used storage space.

        Returns:
            int: The percentage of used storage space, rounded up, clamped between 0 and 100.

        Raises:
            BusyException: If the free or total storage size could not be received from response.
        """
        total_storage = self.get_total_storage_size()
        free_storage = self.get_free_storage_size()
        used_storage = total_storage - free_storage
        used_percentage = (used_storage / total_storage) * 100
        return int(min(100, max(0, math.ceil(used_percentage))))

    # Set and Get Commands

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

    def set_showing_picture(self, filename:str) -> bool:
        # TODO : Implement
        command = Commands.SetShowingPicture.format(filename=filename)
        response = self._send_serial_command(command.encode())
        print(response)
        # TODO ERROR HANDLING
        return True

    def set_brightness(self, brightness:int) -> bool:
        # TODO : Implement
        command = Commands.SetDisplayBrightness.format(brightness=brightness)
        response = self._send_serial_command(command.encode())
        print(response)
        # TODO ERROR HANDLING
        return True

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

    def _get_list(self, command: str, regex: str, error_message: str, error_code: ErrorCode) -> list[str]:
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
        response = self._send_serial_command(command.encode())
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

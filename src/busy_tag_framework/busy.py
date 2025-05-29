"""
This module provides the `Busy` class, which contains helper methods for
evaluating error and reset codes for Busy Tag devices.
It allows mapping numeric error and reset codes to their corresponding enum
members to support easier error diagnosis and handling.

Functions:
- get_last_error_code: Returns the matching enum member for an error code.
- get_last_reset_code: Returns the matching enum member for a reset code.

Dependencies:
- busy_get_last_error_code
- busy_get_last_reset_code
"""

from busy_tag_framework.busy_get_last_error_code import BusyGetLastErrorCode
from busy_tag_framework.busy_get_last_reset_code import BusyGetLastResetCode

class Busy:
    """
    The `Busy` class provides static helper methods for evaluating error and reset codes
    for Busy Tag devices. It maps numeric error and reset codes to their corresponding
    enum members to facilitate error diagnosis and handling.

    Methods:
        get_last_error_code(error_code: int) -> BusyGetLastErrorCode:
            Returns the matching enum member for a given error code.

        get_last_reset_code(reset_code: int) -> BusyGetLastResetCode:
            Returns the matching enum member for a given reset code.
    """

    @staticmethod
    def get_last_error_code(error_code: int) -> BusyGetLastErrorCode:
        """
        Returns the corresponding BusyGetLastErrorCode enum member for the given error code.

        Args:
            error_code (int): The numeric error code to evaluate.

        Returns:
            BusyGetLastErrorCode: The matching enum member, or UNDEFINED if not found.
        """
        for member in BusyGetLastErrorCode:
            if member.value == error_code:
                return member
        return BusyGetLastErrorCode.UNDEFINED

    @staticmethod
    def get_last_reset_code(reset_code: int) -> BusyGetLastResetCode:
        """
        Returns the corresponding BusyGetLastResetCode enum member for the given reset code.

        Args:
            reset_code (int): The numeric reset code to evaluate.

        Returns:
            BusyGetLastResetCode: The matching enum member, or UNDEFINED if not found.
        """
        for member in BusyGetLastResetCode:
            if member.value == reset_code:
                return member
        return BusyGetLastResetCode.UNDEFINED

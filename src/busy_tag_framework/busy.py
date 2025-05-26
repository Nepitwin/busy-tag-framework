from busy_tag_framework.busy_get_last_error_code import BusyGetLastErrorCode
from busy_tag_framework.busy_get_last_reset_code import BusyGetLastResetCode

class Busy:

    @staticmethod
    def get_last_error_code(error_code: int) -> BusyGetLastErrorCode:
        for member in BusyGetLastErrorCode:
            if member.value == error_code:
                return member
        return BusyGetLastErrorCode.UNDEFINED

    @staticmethod
    def get_last_reset_code(reset_code: int) -> BusyGetLastResetCode:
        for member in BusyGetLastResetCode:
            if member.value == reset_code:
                return member
        return BusyGetLastResetCode.UNDEFINED
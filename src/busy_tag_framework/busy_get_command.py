from busy_tag_framework.busy_return_type import BusyReturnType
from busy_tag_framework.error_code import ErrorCode


class BusyGetCommand:

    def __init__(self,
                 action: str,
                 regex: str,
                 error_msg: str,
                 error_code: ErrorCode,
                 return_type: BusyReturnType,
                 min_firmware_version: str = None):
        self.action = action
        self.regex = regex
        self.error_msg = error_msg
        self.error_code = error_code
        self.return_type = return_type
        self.min_firmware_version = min_firmware_version

from busy_tag_framework.busy_return_type import BusyReturnType
from busy_tag_framework.error_code import ErrorCode


class BusyCommand:

    def __init__(self, action: str, regex: str, error_msg: str, error_code: ErrorCode, return_type: BusyReturnType):
        self.action = action
        self.regex = regex
        self.error_msg = error_msg
        self.error_code = error_code
        self.return_type = return_type

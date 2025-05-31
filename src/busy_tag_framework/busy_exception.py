from busy_tag_framework.busy_error_code import BusyErrorCode

class BusyException(Exception):
    def __init__(self, message, error_code: BusyErrorCode):
        super().__init__(message)
        self.error_code = error_code

from busy_tag_framework.error_code import ErrorCode

class BusyException(Exception):
    def __init__(self, message, error_code: ErrorCode):
        super().__init__(message)
        self.error_code = error_code
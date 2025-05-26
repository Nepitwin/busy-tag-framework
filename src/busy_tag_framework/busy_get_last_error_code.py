from enum import Enum

class BusyGetLastErrorCode(Enum):
    NONE = -1
    UNKNOWN_ERROR = 0
    UNKNOWN_COMMAND = 1
    INVALID_ARGUMENT = 2
    FILE_NOT_FOUND = 3
    INVALID_SIZE = 4
    UNDEFINED = 5

from busy_tag_framework.busy_return_type import BusyReturnType


class BusySetCommand:

    def __init__(self,
                 action: str,
                 params: list[str],
                 return_type: BusyReturnType,
                 min_firmware_version: str = None):
        self.action = action
        self.params = params
        self.return_type = return_type
        self.min_firmware_version = min_firmware_version

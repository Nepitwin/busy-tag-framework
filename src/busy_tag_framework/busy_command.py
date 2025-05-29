from busy_tag_framework.busy_get_command import BusyGetCommand
from busy_tag_framework.busy_set_command import BusySetCommand
from busy_tag_framework.busy_return_type import BusyReturnType
from busy_tag_framework.error_code import ErrorCode


class BusyCommand:

    # https://luxafor.helpscoutdocs.com/article/47-busy-tag-usb-cdc-command-reference-guide

    # Get Commands
    GetDeviceName = BusyGetCommand("AT+GDN\r\n", r"\+DN:(.*)", "Device name not found", ErrorCode.DEVICE_NAME_NOT_FOUND, BusyReturnType.STRING)
    GetManufactureName = BusyGetCommand("AT+GMN\r\n", r"\+MN:(.*)", "Manufacture name not found", ErrorCode.MANUFACTURE_NAME_NOT_FOUND, BusyReturnType.STRING)
    GetDeviceId = BusyGetCommand("AT+GID\r\n", r"\+ID:(.*)", "Device ID not found", ErrorCode.DEVICE_ID_NOT_FOUND, BusyReturnType.STRING)
    GetFirmwareVersion = BusyGetCommand("AT+GFV\r\n", r"\+FV:(.*)", "Firmware version not found", ErrorCode.FIRMWARE_VERSION_NOT_FOUND, BusyReturnType.STRING)
    GetPictureList = BusyGetCommand("AT+GPL\r\n", r"\+PL:(.*),\d+", "Picture list not found", ErrorCode.PICTURE_LIST_NOT_FOUND, BusyReturnType.LIST)
    GetFileList = BusyGetCommand("AT+GFL\r\n", r"\+FL:(.*?),file,\d+", "File list not found", ErrorCode.FILE_LIST_NOT_FOUND, BusyReturnType.LIST)
    GetLocalHostAddress = BusyGetCommand("AT+GLHA\r\n", r"\+LHA:(.*)", "Local host address not found", ErrorCode.LOCAL_HOST_ADDRESS_NOT_FOUND, BusyReturnType.STRING)
    GetFreeStorageSize = BusyGetCommand("AT+GFSS\r\n", r"\+FSS:(.*)", "Free storage size not found", ErrorCode.FREE_STORAGE_SIZE_NOT_FOUND, BusyReturnType.NUMBER)
    GetTotalStorageSize = BusyGetCommand("AT+GTSS\r\n", r"\+TSS:(.*)", "Total storage size not found", ErrorCode.TOTAL_STORAGE_SIZE_NOT_FOUND, BusyReturnType.NUMBER)
    GetSolidColor = BusyGetCommand("AT+SC?\r\n", r"\+SC:\d+,(#?[0-9A-Fa-f]{6}|#?[0-9A-Fa-f]{3})", "Solid color not found", ErrorCode.SOLID_COLOR_NOT_FOUND, BusyReturnType.STRING)
    GetDisplayBrightness = BusyGetCommand("AT+DB?\r\n", r"\+DB:(\d+)", "Display brightness not found", ErrorCode.DISPLAY_BRIGHTNESS_NOT_FOUND, BusyReturnType.NUMBER)
    GetShowAfterDrop = BusyGetCommand("AT+SAD?\r\n", r"\+SAD:(\d+)", "Show after drop not found", ErrorCode.SHOW_AFTER_DROP_NOT_FOUND, BusyReturnType.NUMBER)
    GetAllowedWebFileServer = BusyGetCommand("AT+AWFS?\r\n", r"\+AWFS:(\d+)", "Allowed web file server not found", ErrorCode.ALLOWED_WEB_FILE_SERVER_NOT_FOUND, BusyReturnType.NUMBER)
    GetWifiConfig = BusyGetCommand("AT+WC?\r\n", r"\+WC:(.*)", "Wifi config not found", ErrorCode.WIFI_CONFIG_NOT_FOUND, BusyReturnType.TUPLE)
    GetUsbMassStorageAllowed = BusyGetCommand("AT+UMSA?\r\n", r"\+UMSA:(\d+)", "USB mass storage allowed not found", ErrorCode.USB_MASS_STORAGE_ALLOWED_NOT_FOUND, BusyReturnType.NUMBER)
    GetShowingPicture = BusyGetCommand("AT+SP?\r\n", r"\+SP:(.*)", "Showing picture not found", ErrorCode.SHOWING_PICTURE_NOT_FOUND, BusyReturnType.STRING, "0.8")
    GetLastErrorCode = BusyGetCommand("AT+GLEC\r\n", r"\+LEC:(-?\d+)", "Get last error code not found", ErrorCode.GET_LAST_ERROR_CODE, BusyReturnType.NUMBER, "0.8")
    GetLastResetReasonForCoreZero = BusyGetCommand("AT+GLRR0\r\n", r"\+LRR0:(-?\d+)", "Get last reset code for core 0 not found", ErrorCode.GET_LAST_RESET_CODE_CORE_ZERO, BusyReturnType.NUMBER, "1.1")
    GetLastResetReasonForCoreOne = BusyGetCommand("AT+GLRR1\r\n", r"\+LRR1:(-?\d+)", "Get last reset code for core 1 not found", ErrorCode.GET_LAST_RESET_CODE_CORE_ONE, BusyReturnType.NUMBER, "1.1")

    # Set Commands
    # TODO Validation into params as class member
    SetSolidColor = BusySetCommand("AT+SC={led_bits},{color_hex}\r\n", ["led_bits", "color_hex"], BusyReturnType.BOOLEAN)
    SetDisplayBrightness = BusySetCommand("AT+DB={brightness}\r\n", ["brightness"], BusyReturnType.BOOLEAN)
    SetUsbMassStorageAllowed = BusySetCommand("AT+UMSA={active}\r\n", ["active"], BusyReturnType.BOOLEAN)
    SetWifiConfig = BusySetCommand("AT+WC={ssid},{password}\r\n", ["ssid", "password"], BusyReturnType.BOOLEAN)
    SetShowAfterDrop = BusySetCommand("AT+SAD={active}\r\n", ["active"], BusyReturnType.BOOLEAN)
    SetAllowedWebFileServer = BusySetCommand("AT+AWFS={active}\r\n", ["active"], BusyReturnType.BOOLEAN)
    SetShowingPicture = BusySetCommand("AT+SP={filename}\r\n", ["filename"], BusyReturnType.BOOLEAN, "0.8")

    # TODO Get and Set Commands to implement
    GetCustomPattern = "AT+CP?\r\n"
    SetCustomPattern = "AT+CP={pattern}\r\n"
    GetAllowedAutoStorageScan = "AT+AASS?\r\n"  # Since Firmware Version 0.8
    SetAllowedAutoStorageScan = "AT+AASS\r\n" # Since Firmware Version 0.8

    # Action Commands
    # TODO Actions to implement
    GetFile = "AT+GF\r\n"
    UploadFile = "AT+UF\r\n"
    DeleteFile = "AT+DF\r\n"
    RestartDevice = "AT+RST\r\n"
    FormatDisk = "AT+FD\r\n"
    ActivateFileStorageScan = "AT+AFSS\r\n"

    # Factory Reset Commands
    # TODO Factory reset commands to implement
    FactoryResetMainConfigFile = "AT+FRMCF\r\n" # Since Firmware Version 1.1
    FactoryResetWifiConfigFile = "AT+FRWCF\r\n" # Since Firmware Version 1.1
    FactoryResetDefaultImage = "AT+FRDI\r\n" # Since Firmware Version 1.1

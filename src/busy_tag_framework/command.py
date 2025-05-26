from busy_tag_framework.busy_command import BusyCommand
from busy_tag_framework.busy_return_type import BusyReturnType
from busy_tag_framework.error_code import ErrorCode


class Command:

    # https://luxafor.helpscoutdocs.com/article/47-busy-tag-usb-cdc-command-reference-guide

    # Get Commands
    GetDeviceName = BusyCommand("AT+GDN\r\n",r"\+DN:(.*)", "Device name not found", ErrorCode.DEVICE_NAME_NOT_FOUND, BusyReturnType.STRING)
    GetManufactureName = BusyCommand("AT+GMN\r\n",r"\+MN:(.*)", "Manufacture name not found", ErrorCode.MANUFACTURE_NAME_NOT_FOUND, BusyReturnType.STRING)
    GetDeviceId = BusyCommand("AT+GID\r\n",r"\+ID:(.*)", "Device ID not found", ErrorCode.DEVICE_ID_NOT_FOUND, BusyReturnType.STRING)
    GetFirmwareVersion = BusyCommand("AT+GFV\r\n",r"\+FV:(.*)", "Firmware version not found", ErrorCode.FIRMWARE_VERSION_NOT_FOUND, BusyReturnType.STRING)
    GetPictureList = BusyCommand("AT+GPL\r\n",r"\+PL:(.*),\d+", "Picture list not found", ErrorCode.PICTURE_LIST_NOT_FOUND, BusyReturnType.LIST)
    GetFileList = BusyCommand("AT+GFL\r\n",r"\+FL:(.*?),file,\d+", "File list not found", ErrorCode.FILE_LIST_NOT_FOUND, BusyReturnType.LIST)
    GetLocalHostAddress = BusyCommand("AT+GLHA\r\n",r"\+LHA:(.*)", "Local host address not found", ErrorCode.LOCAL_HOST_ADDRESS_NOT_FOUND, BusyReturnType.STRING)
    GetFreeStorageSize = BusyCommand("AT+GFSS\r\n",r"\+FSS:(.*)", "Free storage size not found", ErrorCode.FREE_STORAGE_SIZE_NOT_FOUND, BusyReturnType.NUMBER)
    GetTotalStorageSize = BusyCommand("AT+GTSS\r\n",r"\+TSS:(.*)", "Total storage size not found", ErrorCode.TOTAL_STORAGE_SIZE_NOT_FOUND, BusyReturnType.NUMBER)
    GetSolidColor = BusyCommand("AT+SC?\r\n",r"\+SC:\d+,(#?[0-9A-Fa-f]{6}|#?[0-9A-Fa-f]{3})", "Solid color not found", ErrorCode.SOLID_COLOR_NOT_FOUND, BusyReturnType.STRING)
    GetShowingPicture = BusyCommand("AT+SP?\r\n",r"\+SP:(.*)", "Showing picture not found", ErrorCode.SHOWING_PICTURE_NOT_FOUND, BusyReturnType.STRING)
    GetDisplayBrightness = BusyCommand("AT+DB?\r\n",r"\+DB:(\d+)", "Display brightness not found", ErrorCode.DISPLAY_BRIGHTNESS_NOT_FOUND, BusyReturnType.NUMBER)
    GetShowAfterDrop = BusyCommand("AT+SAD?\r\n",r"\+SAD:(\d+)", "Show after drop not found", ErrorCode.SHOW_AFTER_DROP_NOT_FOUND, BusyReturnType.NUMBER)
    GetAllowedWebFileServer = BusyCommand("AT+AWFS?\r\n",r"\+AWFS:(\d+)", "Allowed web file server not found", ErrorCode.ALLOWED_WEB_FILE_SERVER_NOT_FOUND, BusyReturnType.NUMBER)
    GetWifiConfig = BusyCommand("AT+WC?\r\n",r"\+WC:(.*)", "Wifi config not found", ErrorCode.WIFI_CONFIG_NOT_FOUND, BusyReturnType.TUPLE)
    GetUsbMassStorageAllowed = BusyCommand("AT+UMSA?\r\n",r"\+UMSA:(\d+)", "USB mass storage allowed not found", ErrorCode.USB_MASS_STORAGE_ALLOWED_NOT_FOUND, BusyReturnType.NUMBER)
    GetLastErrorCode = BusyCommand("AT+GLEC\r\n", r"\+LEC:(-?\d+)", "Get last error code not found", ErrorCode.GET_LAST_ERROR_CODE, BusyReturnType.NUMBER, "0.8")
    GetLastResetReasonForCoreZero = BusyCommand("AT+GLRR0\r\n", r"\+LRR0:(-?\d+)", "Get last reset code for core 0 not found", ErrorCode.GET_LAST_RESET_CODE_CORE_ZERO, BusyReturnType.NUMBER, "1.1")
    GetLastResetReasonForCoreOne = BusyCommand("AT+GLRR1\r\n", r"\+LRR1:(-?\d+)", "Get last reset code for core 1 not found", ErrorCode.GET_LAST_RESET_CODE_CORE_ONE, BusyReturnType.NUMBER, "1.1")

    # TODO Get Commands to implement
    GetCustomPattern = "AT+CP?\r\n"
    GetAllowedAutoStorageScan = "AT+AASS?\r\n"  # Since Firmware Version 1.1

    # Set Commands
    # TODO Set Commands to implement
    SetSolidColor = "AT+SC={led_bits},{color_hex}\r\n"
    SetCustomPattern = "AT+CP={pattern}\r\n"
    SetDisplayBrightness = "AT+DB={brightness}\r\n"
    SetShowAfterDrop = "AT+SAD={brightness}\r\n"
    SetAllowedWebFileServer = "AT+AWFS?\r\n"
    SetWifiConfig = "AT+WC={ssid},{password}\r\n"
    SetUsbMassStorageAllowed = "AT+UMSA={allowed}\r\n"
    SetShowingPicture = "AT+SP={filename}\r\n"
    SetAllowedAutoStorageScan = "AT+AASS\r\n" # Since Firmware Version 1.1

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

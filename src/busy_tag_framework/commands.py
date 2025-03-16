
class Commands:

    # https://luxafor.helpscoutdocs.com/article/47-busy-tag-usb-cdc-command-reference-guide

    # Get Commands
    GetDeviceName = "AT+GDN\r\n"
    GetManufactureName = "AT+GMN\r\n"
    GetDeviceId = "AT+GID\r\n"
    GetFirmwareVersion = "AT+GFV\r\n"
    GetPictureList = "AT+GPL\r\n"
    GetFileList = "AT+GFL\r\n"
    GetLocalHostAddress = "AT+GLHA\r\n"
    GetFreeStorageSize = "AT+GFSS\r\n"
    GetTotalStorageSize = "AT+GTSS\r\n"

    # TODO : FIRMWARE CHECKUP + IMPLEMENT ME
    GetLastErrorCode = "AT+GLEC\r\n" # Since Firmware Version 0.8

    # TODO : FIRMWARE CHECKUP + IMPLEMENT ME
    GetLastResetReasonForCoreZero = "AT+GLRR0\r\n"  # Since Firmware Version 1.1
    GetLastResetReasonForCoreOne = "AT+GLRR1\r\n"   # Since Firmware Version 1.1

    # Set and Get Commands
    # TODO : SET USAGE HERE AS Template
    SetSolidColor = "AT+SC={led_bits},{color_hex}\r\n"
    SetShowingPicture = "AT+SP={filename}\r\n"
    SetDisplayBrightness = "AT+DB={brightness}\r\n"

    GetSolidColor = "AT+SC?\r\n"
    GetShowingPicture = "AT+SP?\r\n"
    GetDisplayBrightness = "AT+DB?\r\n"
    GetShowAfterDrop = "AT+SAD?\r\n"
    GetAllowedWebFileServer = "AT+AWFS?\r\n"
    GetWifiConfig = "AT+WC?\r\n"
    GetUsbMassStorageAllowed = "AT+UMSA?\r\n"

    # TODO : IMPLEMENT ME
    GetCustomPattern = "AT+CP?\r\n"

    # TODO : FIRMWARE CHECKUP + IMPLEMENT ME
    SetAllowedAutoStorageScan = "AT+AASS\r\n" # Since Firmware Version 1.1
    GetAllowedAutoStorageScan = "AT+AASS?\r\n"  # Since Firmware Version 1.1

    # Actions
    # TODO : IMPLEMENT ME
    GetFile = "AT+GF\r\n"
    UploadFile = "AT+UF\r\n"
    DeleteFile = "AT+DF\r\n"
    RestartDevice = "AT+RST\r\n"
    FormatDisk = "AT+FD\r\n"
    ActivateFileStorageScan = "AT+AFSS\r\n"

    # TODO : FIRMWARE CHECKUP + IMPLEMENT ME
    FactoryResetMainConfigFile = "AT+FRMCF\r\n" # Since Firmware Version 1.1
    FactoryResetWifiConfigFile = "AT+FRWCF\r\n" # Since Firmware Version 1.1
    FactoryResetDefaultImage = "AT+FRDI\r\n" # Since Firmware Version 1.1



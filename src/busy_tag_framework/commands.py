
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

    # TODO : FIRMWARE CHECKUP
    GetLastErrorCode = "AT+GLEC\r\n" # Since Firmware Version 0.8

    # TODO : FIRMWARE CHECKUP
    GetLastResetReasonForCoreZero = "AT+GLRR0\r\n"  # Since Firmware Version 1.1
    GetLastResetReasonForCoreOne = "AT+GLRR1\r\n"   # Since Firmware Version 1.1

    # Set and Get Commands
    # TODO : SET USAGE HERE AS Template
    SetSolidColor = "AT+SC={led_bits},{color_hex}\r\n"
    SetShowingPicture = "AT+SP={filename}\r\n"
    SetDisplayBrightness = "AT+DB={brightness}\r\n"

    # TODO : Get Solid Color
    GetSolidColor = "AT+SC\r\n"
    CustomPattern = b"AT+CP\r\n"
    DisplayBrightness = b"AT+DB\r\n"
    ShowAfterDrop = b"AT+SAD\r\n"
    AllowedWebFileServer = b"AT+AWFS\r\n"
    WifiConfig = b"AT+WC\r\n"
    UsbMassStorageAllowed = b"AT+UMSA\r\n"
    ShowingPicture = b"AT+SP\r\n"
    # TODO : FIRMWARE CHECKUP
    AllowedAutoStorageScan = b"AT+AASS\r\n" # Since Firmware Version 1.1

    # Actions
    GetFile = b"AT+GF\r\n"
    UploadFile = b"AT+UF\r\n"
    DeleteFile = b"AT+DF\r\n"
    RestartDevice = b"AT+RST\r\n"
    FormatDisk = b"AT+FD\r\n"
    ActivateFileStorageScan = b"AT+AFSS\r\n"

    # TODO : FIRMWARE CHECKUP
    FactoryResetMainConfigFile = b"AT+FRMCF\r\n" # Since Firmware Version 1.1
    FactoryResetWifiConfigFile = b"AT+FRWCF\r\n" # Since Firmware Version 1.1
    FactoryResetDefaultImage = b"AT+FRDI\r\n" # Since Firmware Version 1.1



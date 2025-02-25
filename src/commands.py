
class Commands:

    # https://luxafor.helpscoutdocs.com/article/47-busy-tag-usb-cdc-command-reference-guide

    # Get Commands
    GetDeviceName = b"AT+GDN\r\n"
    GetManufactureName = b"AT+GMN\r\n"
    GetDeviceId = b"AT+GID\r\n"
    GetFirmwareVersion = b"AT+GFV\r\n"
    GetPictureList = b"AT+GPL\r\n"
    GetFileList = b"AT+GFL\r\n"
    GetLocalHostAddress = b"AT+GLHA\r\n"
    GetFreeStorageSize = b"AT+GFSS\r\n"
    GetTotalStorageSize = b"AT+GTSS\r\n"

    # TODO : FIRMWARE CHECKUP
    GetLastErrorCode = b"AT+GLEC\r\n" # Since Firmware Version 0.8

    # TODO : FIRMWARE CHECKUP
    GetLastResetReasonForCoreZero = b"AT+GLRR0\r\n"  # Since Firmware Version 1.1
    GetLastResetReasonForCoreOne = b"AT+GLRR1\r\n"   # Since Firmware Version 1.1

    # Set and Get Commands
    # TODO : SET USAGE HERE
    SolidColor = b"AT+SC\r\n"
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



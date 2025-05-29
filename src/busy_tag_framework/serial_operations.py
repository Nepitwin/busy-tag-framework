import serial
import serial.tools.list_ports

from busy_tag_framework.busy_command import BusyCommand

def find_all_busy_tag_devices() -> list or None:
    devices = []

    ports = serial.tools.list_ports.comports()
    for port_info in ports:
        port = port_info.device
        try:
            ser = serial.Serial(port, baudrate=115200, timeout=1, write_timeout=1)
            ser.flushInput()
            ser.flushOutput()
            ser.write(BusyCommand.GetDeviceName.action.encode())
            response = ser.readline().decode('utf-8').strip()

            if response.startswith("+DN:busytag-"):
                ser.close()
                devices.append({"port": port, "device": response})

            ser.close()

        except serial.SerialTimeoutException:
            print(f"Timeout on port {port}, moving to the next port.")
            continue

        except (serial.SerialException, UnicodeDecodeError, OSError) as e:
            print(f"Error on port {port}: {e}")
            continue

        except Exception as e:
            print(f"Unexpected error on port {port}: {e}")
            continue

        finally:
            try:
                if ser.is_open:
                    ser.close()
            except:
                pass

    if len(devices) > 0:
        return devices

    print("No Busy Tag device found.")
    return None
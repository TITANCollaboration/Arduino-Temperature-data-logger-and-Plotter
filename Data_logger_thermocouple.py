import time
import serial
import serial.tools.list_ports
from datetime import datetime
import csv 
import os
header = ["Timestamp", "PB5 Temperature"]
baud_rate = 115200
DATA_FOLDER = "PB5_Temp_Data"

def find_port(): # This function finds the correct port that the Arduino is attached to on your device, as this is important for telling the main logging function what port to read from incase you have multiple devices attached 
    ports = serial.tools.list_ports.comports()

    for port in ports: # This for loop searches through the ports on your device based on the keywords for the Arduino
        description = port.description.lower()
        manufacturer = (port.manufacturer or "").lower()

        if any(keyword in description or keyword in manufacturer for keyword in ["arduino"]):
            return port.device


def get_date(): #Helper funcion to get the date and time for time stamp purposes
    return datetime.now().strftime("%Y-%m-%d")
    

def Main_Logger(): # The main logging function
    os.makedirs(DATA_FOLDER, exist_ok=True)

    ser = None

    port = find_port()
    if not port:
        print("No serial or USB port found, check connections")
        return 
    try: # Finds and sets the correct Baud rate so you are able to communicate with the Arduino, mainly incase your device runs at a different one than the standard I had set in the Arduino code
        ser = serial.Serial(port, baud_rate, timeout=2)
        print(f"Connected to{port} at {baud_rate} baud.")
    except serial.SerialException as e:
        print(f"Failed to connect to the serial port{e}")
        return

    time.sleep(2)

    date = None
    file_handle = None
    csv_writer = None

    try:# This is the main csv writing file which both creates and then writes the data 
        while True:

            today = get_date()
            if today!= date:
                if file_handle:
                    file_handle.close()
                date = today
                filename = os.path.join(DATA_FOLDER, f"PB5_Temp_Data_{date}.csv")
 

                file_exists = os.path.isfile(filename)

                file_handle = open(filename, mode="a", newline="")
                csv_writer = csv.writer(file_handle)

                if not file_exists:
                    csv_writer.writerow(header)
                    file_handle.flush()
                print(f"Logging data to:{filename}")

            if ser.in_waiting > 0:
                try:
                    line = ser.readline().decode("utf-8").strip()

                    if line:
                        data = line
                        

                        timestamp = datetime.now().strftime("%H:%M:%S")

                        row = [timestamp, data]
                        print(row)

                        csv_writer.writerow(row)
                        file_handle.flush()

                except UnicodeDecodeError:

                    pass
            time.sleep(0.01)
    except KeyboardInterrupt:
        print("\nStopping data logger")  

    finally:
        if file_handle:
            file_handle.close()
        if ser.is_open:
            ser.close()
if __name__ == "__main__":
    Main_Logger()



        


    


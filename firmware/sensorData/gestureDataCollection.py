import serial
import csv
import time
from normalizeFunction import normalize

# Ask for gesture name
gesture_label = input("What gesture are you recording (e.g., 'Thank_You', 'ILoveYou')? ")

# Set up serial connection (make sure COM port is correct guys! You can check this in your arduino IDE)
ser = serial.Serial('/dev/cu.usbmodem21101', 9600)

time.sleep(2)

# Save to Downloads folder (rename for your file structure!)
filename = f"/Users/srodr679/Downloads/{gesture_label}_data.csv"


# Open CSV file and start logging
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['F1', 'F2', 'F3', 'F4', 'F5', 'X', 'Y', 'Z', 'Gesture'])

    print(f"\n Recording data for: {gesture_label}")
    print(f" Saving to: {filename}")
    print(" Press Ctrl+C to stop...\n")

    try:
       while True:
        user_input = input("Type 'cont' to record a new value or 'stop' to end: ").strip().lower()

        if user_input == 'stop':
            print("Stopping.")
            break
        elif user_input == 'cont':
            for i in range(6):
                line = ser.readline().decode().strip()

                # split returns strings, below will convert to floats instead
                values = [float(x) for x in (line.split(','))]

                # Normalizing values, adjust as needed!
                # Since we know the order the serial data will arrive, we can use
                # ranges to normalize specific parts of the list of values

                # :5 means up to and excluding 5, as index 0-4 are our flex sensors
                values[:5] = normalize(values[:5], 100, 700)

                # 5: means from 5 to end, as index 5-7 are (supposed to be?) positional values
                values[5:] = normalize(values[5:], -1, 2)

                if len(values) == 8:
                    writer.writerow(values + [gesture_label])
                    print(values + [gesture_label])
            print()
        else:
            print("Invalid input. Please type 'cont' or 'stop'.")
           
    except KeyboardInterrupt:
        print(f"\n🛑 Recording stopped. File saved to: {filename}")

ser.close()
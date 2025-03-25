import serial
import csv
import time

# Ask for gesture name
gesture_label = input("What gesture are you recording (e.g., 'Thank_You', 'ILoveYou')? ")

# Set up serial connection (make sure COM port is correct guys! You can check this in your arduino IDE)
ser = serial.Serial('/dev/cu.usbmodem21101', 9600)

time.sleep(2)

# Save to Downloads folder
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
                values = line.split(',')

                if len(values) == 8:
                    writer.writerow(values + [gesture_label])
                    print(values + [gesture_label])
            print()
        else:
            print("Invalid input. Please type 'cont' or 'stop'.")
           
    except KeyboardInterrupt:
        print(f"\n🛑 Recording stopped. File saved to: {filename}")

ser.close()
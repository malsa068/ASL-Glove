import os
import serial
import csv
import time
from normalizeFunction import normalize

gesture_label = input("What gesture are you recording (e.g., 'Thank_You', 'ILoveYou')? ")

# Set up serial connection (make sure COM port is correct guys! You can check this in your arduino IDE)
ser = serial.Serial('/dev/cu.usbmodem21101', 9600)
time.sleep(2)

# Save to local Downloads folder
filename = f"/Users/srodr679/Downloads/{gesture_label}_data.csv"
file_exists = os.path.exists(filename)


with open(filename, 'a', newline='') as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(['F1', 'F2', 'F3', 'F4', 'F5', 'X', 'Y', 'Z', 'Gesture'])

    print(f"\nRecording 20 samples for: {gesture_label}")
    print(f"Saving to: {filename}")
    print("waiting for valid sensor data...\n")

    sample_count = 0

    try:
        while sample_count < 20:
            # Always read and show raw line
            raw_line = ser.readline().decode(errors='ignore').strip()
            print(f"[RAW] {raw_line}")

            values = raw_line.split(',')

            if len(values) == 8:
                try:
                    values = [float(v) for v in values]
                    writer.writerow(values + [gesture_label])
                    print(f"Sample {sample_count + 1} saved: {values + [gesture_label]}")
                    sample_count += 1
                except ValueError:
                    print("Invalid float conversion. Skipping line.")
            else:
                print(f"Expected 8 values, got {len(values)}. Skipping.")

    except KeyboardInterrupt:
        print("\n Recording interrupted.")

ser.close() 
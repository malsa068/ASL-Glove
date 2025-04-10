#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>




Adafruit_MPU6050 mpu;




const int thumbPin = A1;
const int indexPin = A2;
const int middlePin = A3;
const int ringPin = A4;
const int pinkyPin = A5;




void setup() {
  Serial.begin(9600);
  while (!Serial);




  pinMode(thumbPin, INPUT);
  pinMode(indexPin, INPUT);
  pinMode(middlePin, INPUT);
  pinMode(ringPin, INPUT);
  pinMode(pinkyPin, INPUT);






  Wire.begin();
  Wire.setClock(100000); // slow I2C = less interference




  Serial.println("Initializing MPU6050...");
  if (!mpu.begin(0x68, &Wire)) {
    Serial.println("MPU6050 not found. Check wiring.");
    while (1);
  }




  Serial.println("MPU6050 connected!");
  mpu.setAccelerometerRange(MPU6050_RANGE_4_G);
  mpu.setFilterBandwidth(MPU6050_BAND_5_HZ);
  delay(100);
}




void loop() {
  sensors_event_t accel, gyro, temp;
  mpu.getEvent(&accel, &gyro, &temp);
  delay(5);




  int thumbValue = analogRead(thumbPin); delay(2);
  int indexValue = analogRead(indexPin); delay(2);
  int middleValue = analogRead(middlePin); delay(2);
  int ringValue = analogRead(ringPin); delay(2);
  int pinkyValue = analogRead(pinkyPin); delay(2);




  Serial.print(" "); Serial.print(thumbValue);
  Serial.print(", "); Serial.print(indexValue);
  Serial.print(", "); Serial.print(middleValue);
  Serial.print(", "); Serial.print(ringValue);
  Serial.print(", "); Serial.print(pinkyValue);
  Serial.print(", "); Serial.print(accel.acceleration.x);
  Serial.print(", "); Serial.print(accel.acceleration.y);
  Serial.print(", "); Serial.println(accel.acceleration.z);

//  // Print labeled values to Serial Monitor
//   Serial.print("Thumb: "); Serial.print(thumbValue);
//   Serial.print(" | Index: "); Serial.print(indexValue);
//   Serial.print(" | Middle: "); Serial.print(middleValue);
//   Serial.print(" | Ring: "); Serial.print(ringValue);
//   Serial.print(" | Pinky: "); Serial.println(pinkyValue);
//   // Sample Output: Thumb: 100 | Index: 234 | Middle: 561 | Ring: 451  | Pinky:

//   // Print accelerometer values
//   Serial.print("aX = "); Serial.print(accelerometer_x);
//   Serial.print(" | aY = "); Serial.print(accelerometer_y);
//   Serial.print(" | aZ = "); Serial.println(accelerometer_z);


  delay(500);
}


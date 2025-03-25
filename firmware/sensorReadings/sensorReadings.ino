// Define flex sensor pins with corresponding finger names
const int thumbPin = A1;
const int indexPin = A2;
const int middlePin = A3;
const int ringPin = A4;
const int pinkyPin = A5;

void setup() {
    Serial.begin(9600); // Start Serial Monitor at 9600 baud
    
    // Set pins as input
    pinMode(thumbPin, INPUT);
    pinMode(indexPin, INPUT);
    pinMode(middlePin, INPUT);
    pinMode(ringPin, INPUT);
    pinMode(pinkyPin, INPUT);
}

void loop() {
    // Read sensor values
    int thumbValue = analogRead(thumbPin);
    int indexValue = analogRead(indexPin);
    int middleValue = analogRead(middlePin);
    int ringValue = analogRead(ringPin);
    int pinkyValue = analogRead(pinkyPin);

    // Print labeled values to Serial Monitor
    Serial.print("Thumb: "); Serial.print(thumbValue);
    Serial.print(" | Index: "); Serial.print(indexValue);
    Serial.print(" | Middle: "); Serial.print(middleValue);
    Serial.print(" | Ring: "); Serial.print(ringValue);
    Serial.print(" | Pinky: "); Serial.println(pinkyValue);

    // Print unlabeled values to Serial Monitor for Data Collection
    Serial.print(thumbValue);
    Serial.print(" ,"); Serial.print(indexValue);
    Serial.print(" ,"); Serial.print(middleValue);
    Serial.print(" ,"); Serial.print(ringValue);
    Serial.print(" ,"); Serial.println(pinkyValue);

    // Sample Output: Thumb: 100 | Index: 234 | Middle: 561 | Ring: 451  | Pinky:

    delay(900); // Adjust delay for smoother readings
}

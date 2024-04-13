#include <IRremote.h>

// Define IR sensor pins
const int IR_PIN = 2;
const int IR_PIN2 = 3;
const int IR_PIN3 = 14;
const int IR_PIN4 = 4;

// Define RGB LED pins
const int RED_LED_PIN = 11;
const int GREEN_LED_PIN = 10;
const int BLUE_LED_PIN = 9;

// Variables to keep track of the count
int count1 = 0;
int count2 = 0;
int count3 = 0;
int count4 = 0;

// Dummy data array
int dummyData[] = {1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0};
int dataLength = sizeof(dummyData) / sizeof(dummyData[0]);
int dataIndex = 0;

void setup() {
  // Start the serial communication
  Serial.begin(9600);

  // Set IR sensor pins as input
  pinMode(IR_PIN, INPUT);
  pinMode(IR_PIN2, INPUT);
  pinMode(IR_PIN3, INPUT);
  pinMode(IR_PIN4, INPUT);

  // Set RGB LED pins as output
  pinMode(RED_LED_PIN, OUTPUT);
  pinMode(GREEN_LED_PIN, OUTPUT);
  pinMode(BLUE_LED_PIN, OUTPUT);
}

void loop() {
  // Simulate reading the state of the IR sensors from dummy data
  int something = dummyData[dataIndex % dataLength];
  int something1 = dummyData[(dataIndex + 1) % dataLength];
  int something2 = dummyData[(dataIndex + 2) % dataLength];
  int something3 = dummyData[(dataIndex + 3) % dataLength];
  dataIndex++;

  // Check each sensor and update the count accordingly
  if (something == LOW) {
    count1++;
    handleTraffic("signal1", count1, RED_LED_PIN);
    count1 = 0; // Reset the count after handling
  }
  if (something1 == LOW) {
    count2++;
    handleTraffic("signal2", count2, GREEN_LED_PIN);
    count2 = 0; // Reset the count after handling
  }
  if (something2 == LOW) {
    count3++;
    handleTraffic("signal4", count3, BLUE_LED_PIN);
    count3 = 0; // Reset the count after handling
  }
  if (something3 == LOW) {
    count4++;
    handleTraffic("signal3", count4, RED_LED_PIN);
    count4 = 0; // Reset the count after handling
  }

  // Delay to prevent bouncing
  delay(100);
}

void handleTraffic(String signalPath, int count, int ledPin) {
  String trafficDensity;
  if (count < 1) {
    trafficDensity = "loose";
    digitalWrite(ledPin, LOW); // Turn off the LED
  } else if (count = 1 && count < 2) {
    trafficDensity = "moderate";
    digitalWrite(ledPin, HIGH); // Turn on the LED
  } else if (count >= 3 && count < 5) {
    trafficDensity = "congested";
    digitalWrite(ledPin, LOW); // Turn off the LED
  }

  // Log to serial monitor
  Serial.print(signalPath + " traffic density: ");
  Serial.println(trafficDensity);
}

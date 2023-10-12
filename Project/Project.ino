
#include <VarSpeedServo.h> 

// include the library code:
#include <LiquidCrystal.h>

// initialize the library by associating any needed LCD interface pin
// with the arduino pin number it is connected to
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
String incomingByte ;    

int blue_led = 7;

int buzzer = 8;

VarSpeedServo myservo1;

void setup() {

  Serial.begin(9600);
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  pinMode(blue_led, OUTPUT);
  pinMode(buzzer, OUTPUT);
  myservo1.attach(9);

}

void loop() {
  if (Serial.available() > 0) {

    incomingByte = Serial.readStringUntil('\n');

    if (incomingByte == "on") {

      digitalWrite(blue_led, HIGH);

      digitalWrite(buzzer, HIGH);

      Serial.write("Led on");

      myservo1.write(90);

      lcd.println("Welcome");

      delay(3000);

      lcd.clear();

    }

    else if (incomingByte == "off") {

      digitalWrite(blue_led, LOW);

      Serial.write("Led off");

      digitalWrite(buzzer, LOW);

      myservo1.write(0);

      lcd.println("Adham Osama Mohamed");

      delay(3000);
    }

    else{

    Serial.write("invald input");

    }

  }}


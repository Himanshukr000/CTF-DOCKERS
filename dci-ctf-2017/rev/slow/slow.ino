
#include "check.h"

void setup() {
  Serial.begin(115200);  
}

void loop() {
  Serial.println("Welcome");
  Serial.println("I will send you each char of the flag");
  Serial.println("But only one per day...");
  Serial.println("I hope you are not in a rush :)");

  send_flag();

  delay(1000);
}


int finger_count;
const byte ledPins[] = {3,4,5,6,7};

void setup() {
  Serial.begin(9600);
  for (byte i = 0; i < sizeof(ledPins); i++) { 
    pinMode(ledPins[i], OUTPUT);
  }
}

void off() {

  for(int i=0; i<sizeof(ledPins); i++) {

    digitalWrite(ledPins[i], LOW);
    delay(25);
    
  }
}

void fire_leds() {
  if(finger_count == 0) {
        off();
      }
  if(finger_count > 0 || finger_count <= 5) {
     for(int i=0; i<finger_count; i++) {
       digitalWrite(ledPins[i], HIGH);
     }
  }
  else {
    off();
  }
}

void loop() {
  
if(Serial.available()>0) {

  finger_count = Serial.read()- '0'; 
  Serial.println(finger_count);
  fire_leds();
}
}

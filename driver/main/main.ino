#include "TestBed.h"

/* Testing bet instance with default values */
TestBed testBed;


/* Program variables */
uint8_t selector;
float setPoint,lowPoint, highPoint;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(20);
}


void loop() {
  while(!Serial.available()){;}
  selector = Serial.read();
  Serial.print(selector);

  switch(selector){
    /* Calibrate: 'a' */
    case 'a':
      testBed.calibrateHome();
      break;
    
    /* Home: 'b' */
    case 'b':
      testBed.moveCar(0.0);
      break;

    /* Move car: 'c' + set-point in mm (float) */
    case 'c':
      while(!Serial.available()){;}
      setPoint = -1*(Serial.readString().toFloat());  // Covert to negative: GUI is sending positive position values
      setPoint = constrain(setPoint, MIN_LIM, MAX_LIM);
      testBed.moveCar(setPoint);
      break;

    /* Oscillate: 'd' +  lowPoint in mm(float) +  highPoint in mm(float) */
    case 'd':
      while(!Serial.available()){;}
      lowPoint = -1*(Serial.readString().toFloat());
      lowPoint = constrain(lowPoint, MIN_LIM, MAX_LIM);
      while(!Serial.available()){;}
      highPoint = -1*(Serial.readString().toFloat());
      highPoint = constrain(highPoint, MIN_LIM, MAX_LIM);


      do{
        testBed.moveCar(highPoint);
        testBed.moveCar(lowPoint);
      }while(!Serial.available());

      while(Serial.available())
        Serial.read();
            
      break;
    
    /*IN PROGRESS - Send status*/
    case 'e':
      
      break;

    /*IN PROGRESS - Set parameters*/
    case 'f':
      
      break;

    default:
      break;
  }

  delay(50);
}

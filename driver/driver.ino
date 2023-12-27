#include "TestBed.h"

TestBed testBed;

uint8_t selector;
float setPoint;

void setup() {
  Serial.begin(115200);
}


void loop() {
  while(!Serial.available()){;}
  selector = Serial.read();
  Serial.println(selector);

  switch(selector){
    /* Calibrate */
    case 'a':
      testBed.calibrateHome();
      break;
    
    /* Home */
    case 'b':
      testBed.moveCar(0.0);
      break;

    /* Move car */
    case 'c':
      while(!Serial.available()){;}
      setPoint = Serial.parseFloat();
      Serial.println(setPoint);
      if(setPoint > 0.0) setPoint = 0.0;    
      testBed.moveCar(setPoint);
      break;
    
    /*IN PROGRESS - Get status*/
    case 'd':
      
      break;

    /*IN PROGRESS - Set parameters*/
    case 'e':
      
      break;

    default:
      break;
  }

  delay(50);
}

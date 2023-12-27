#include "TestBed.h"

/* Testing bet instance with default values */
TestBed testBed;


/* Program variables */
uint8_t selector;
float setPoint,lowPoint, highPoint;

void setup() {
  Serial.begin(115200);
}


void loop() {
  while(!Serial.available()){;}
  selector = Serial.read();
  Serial.println(selector);

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
      setPoint = Serial.parseFloat();
      Serial.println(setPoint);
      if(setPoint > 0.0) setPoint = 0.0;    
      testBed.moveCar(setPoint);
      break;

    /* Oscillate: 'd' +  lowPoint in mm(float) +  highPoint in mm(float) */
    case 'd':
      while(!Serial.available()){;}
      lowPoint = Serial.parseFloat();
      Serial.println(lowPoint);
      if(lowPoint > 0.0) lowPoint = 0.0; 

      while(!Serial.available()){;}
      highPoint = Serial.parseFloat();
      Serial.println(highPoint);
      if(highPoint > 0.0) highPoint = 0.0; 

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

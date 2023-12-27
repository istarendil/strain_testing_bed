#include "TestBed.h"

/* Interrupts for the limit switch
* Based on: https://www.onetransistor.eu/2019/05/arduino-class-interrupts-and-callbacks.html
*/
TestBed *ptrSwInt;
static void outsideInterruptHandler(void) { // define global handler
  ptrSwInt->classInterruptHandler(); // calls class member handler
}

void TestBed::classInterruptHandler(void) {
  (digitalRead(LIM_SW_FRONT)==0) ? frontLock = true : frontLock = false;
}

/* Class methods */
TestBed::TestBed(uint8_t inter, uint8_t step, uint8_t dir, uint8_t limSwFr):AccelStepper(inter, step, dir){
  pinMode(limSwFr, INPUT_PULLUP);
  
  ptrSwInt = this;
  attachInterrupt(digitalPinToInterrupt(limSwFr), outsideInterruptHandler, CHANGE);

  setParams();
  
  return;
}

void TestBed::setParams(uint16_t ppr, uint16_t maxSpeed, uint16_t accel){
  this->ppr = ppr;
  this->maxSpeed = maxSpeed;
  this->accel = accel;


  setMaxSpeed(maxSpeed);
  setAcceleration(accel);

  return;
}

uint32_t TestBed::dist2Pul(float length){
  return uint32_t(length*PPR/GRAD);   
}

void TestBed::calibrateHome(){
  moveCar(150.0);
  setCurrentPosition(0);
  delay(1000);
  return;
}


void TestBed::moveCar(float disp){
  uint32_t rev = dist2Pul(disp);
  moveTo(rev);
  while(currentPosition() != rev){
    if(frontLock==1){
      stop();
      return;
    }
    run();
  }
  return;
}


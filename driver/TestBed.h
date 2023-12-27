/* Alberto Sanchez-Delgado
* alberto.casd@proton.me
* 21.12.23
*/

#ifndef TESTBED_H
#define TESTBED_H

#include "Arduino.h"
#include "AccelStepper.h"

/* Driver default definitions */
#define PPR         1000          // Pulse-Per-Revolution (Driver defined)
#define MAX_SPD     1000          // PPR/seg
#define ACCEL       500           // PPR/seg²
#define GRAD        4             // Gradient in mm: Linear distance traveled per revolution - Depends on the bed's screw 

/* Arduino-Driver default pins definition */
#define ITF_TYPE    1
#define STEP        5
#define DIR         4

/* Arduino-Limit Switch default pins definition */
#define LIM_SW_FRONT  3          // Fontal limit switch: Low active

/* Calibration definitions */
#define BIAS_POS    2.0           // Home distance from limit switch in mm (float)


class TestBed: public AccelStepper{
  private:
    uint32_t dist2Pul(float);     // Convert a distance in mm to pulses
    bool frontLock = false;       // Flag: On when the car reached the front limit switch
    void libInterruptHandler(void);
    
  public:
    uint16_t mmPos;               // Instantaneous position in mm
    uint16_t pulsePos;            // Instantaneous position in pulses
    uint16_t ppr;                 // Instantaneous position in pulses
    uint16_t maxSpeed;            // Maximum speed in pulses
    uint16_t accel;               // Acceleration in pulses
    uint8_t grad;                 // Gradient

    TestBed(uint8_t = ITF_TYPE, uint8_t = STEP, uint8_t = DIR, uint8_t = LIM_SW_FRONT);
    void setParams(uint16_t = PPR, uint16_t = MAX_SPD, uint16_t = ACCEL, uint8_t = GRAD);  // (max speed, acceleration, pin of front switch )
    void calibrateHome();
    void moveCar(float);          // Linear displacement in mm: Returns until the position is reached

    void classInterruptHandler(void);
    
};

#endif
# Stain testing bed
This test bed is intended for experimentation with sensors and stretchable materials such as strain gauges. Its structure is based on a linear actuator coupled to a stepper motor and a 3D printed clamp to hold the test material.

Its operation is based on an Arduino card and a DM542EU stepper motor driver. In addition, a GUI has been written in Python to facilitate its configuration.

## Mechanical structure
![PXL_20240119_141446644](https://github.com/istarendil/strain_testing_bed/assets/107052856/1b7dce17-6c8b-4a7c-80db-80d1c3f93f1f)
![PXL_20240119_141431085](https://github.com/istarendil/strain_testing_bed/assets/107052856/21f132d0-c755-4e8c-87e2-a98b80c315bc)


## Graphical User Interface 
![strain_gui](https://github.com/istarendil/strain_testing_bed/assets/107052856/5d1170fb-6d34-41d0-be57-ea26e71cb1ff)


## BOM
- [DOLD Mechatronics](https://www.dold-mechatronik.de/Home)
  - 1 x Linear axis configurator / Easy-Mechatronics System 1216A nominal length 150mm (SKU: EMS1216A-L150) 
  - 1x Plate set incl. Bearings and small parts / Easy-Mechatronics System 1216A (SKU: 90395)
  - 1x Aluminum Profile 30x120L I-Type Groove 6 / Länge: 150mm (SKU: 63047-STLS-0150)
  - 1x SET: ball screw SFU1204-DM 185mm with screw block for Easy-Mechatronics System 1216A - L150 (SKU: 97844)
  - 1x SET: 4x linear bearing SCE16SUU / 2x precision shafts 16mm h6 sanded and hardened, 150mm, with threaded holes M8x25 
  - 1x Stepper motor / 103-H5210-4240 / NEMA17 / flange 42mm / 1A / 51 Ncm (SKU: 76511)
  - 1x Cable with JST (80cm) for stepper motor 103-H5210 / 05-4240 (SKU: 76771)
  - 4x DIN 912 screws with hexagon socket, 8.8, galvanized M3x12 (SKU: DIN912-3x12)
  - 1x Backlash-free coupling JM16C D16L22 5.00 / 6.00mm (SKU: 43049)
  - 1x Machining aluminum profile | cut 8x M6
  - 1x Stepper motor power stage Leadshine DM542EU / Digital / 20-50V (DC) / 1.0-4.2A (DM542EU)
  - 1x Screw Shield for Arduino (SKU:  EX028)
  - 6x DIN 7984 cylinder head screw with hexagon socket and low head, 8.8, galvanized M5x12(SKU: DIN7984-5x12)
  - 6x DIN 7991 countersunk allen, 8.8, galvanized M5x10 (DIN7991-5x10)
  - 6x DIN 7984 cylinder head screw with hexagon socket and low head, 8.8, galvanized M4x20 (SKU: DIN7984-4x20):
  - 6x DIN 934 Hexagon nut, .8, galvanized M4x0.7 (SKU: DIN934-M4)
- [Conrad](https://www.conrad.de/)
  - 2x Delock Adapter für Power Connector - 2-polige Klemmleiste zu Gleichstromstecker 3,5 x 1,35 mm (W)
  - 1x Eaxus 4260183015956 Steckernetzteil, einstellbar 12 V, 15 V, 16 V, 18 V, 19 V, 20 V, 24 V 4500 mA 100 W 

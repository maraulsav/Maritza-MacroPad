## Maritza-MacroPad
Maritza's MacroPad
This is my first ever PCB project. Currently I am making a MacroPad that capable of braille keys and adjusting the volume
It consist of 9 keys MacroPad with a rotary encoder and 2 WS2812B Leds

## Features : 
- Dual layer acrylic case.
- EC11 Rotary encoder
- 2 WS2812B RGB LEDs.
- 9 keys

## CAD Model:
Made in Fusion360
I think it need to used 4 M3 Bolts, 2 M2.5 Bolts (For the mounting hole in the rotary encoder-PCB, I am actually not sure in this part)
and heatset insert. 

<img width="1440" height="900" alt="Screenshot 2025-12-24 at 20 10 17" src="https://github.com/user-attachments/assets/8b19bc2e-013c-4809-80f1-0867bba357b4" />


## PCB
Here's my PCB! It was made in KiCad
I used matrix method for the keys, I followed the guide from GitHub repos dumbpad
These are the Foot Print I used 
- Rotary_Encoder: Rotary Encoder_Alps_EC11E-Switch_Vertical_H20mm_CircularMounting Holes
- Diode: Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal
- XIAO RP2040: Seeed Studio XIAO Series Library: XIAO-RP2040-DIP
- Push Button: Button_Switch_Keyboard: SW_Cherry_MX_1.00u_PCB
- SK6812MINI: LED SMD: LED_SK6812MINI_PLCC4_3.5x3.5mm_P1.75mm

Schematic 
<img width="937" height="503" alt="Screenshot 2025-12-24 at 19 51 22" src="https://github.com/user-attachments/assets/2ed857bc-5fe9-4061-bfa0-ee3ebd87e903" />

PCB

<img width="379" height="454" alt="Screenshot 2025-12-24 at 19 53 05" src="https://github.com/user-attachments/assets/e3d83da8-e88c-44d8-99a4-d70a6cb4118a" />

## Firmware Overview
This MacroPad uses the KMK Firmware -- python in VS Code
- The rotary encoder changes volume. press to mute
- The center column keys is function as delete, enter, space (concurrently from top to bottom)
- The right and left column key is the one that function like braille

## BOM:
Here should be everything you need to make this HackPad
- 4x Cherry MX Switches
- 4x DSA Keycaps
- 9x 1N4148 DO-35 Diodes.
- 2x WS2812B LEDs
- 1x EC11 Rotary Encoder
- 1x XIAO RP2040
- 1x Case (2 Printed Parts)
- 4x Heatsocket
- 4x M3x16mm SHCS Bolts
- 2x M2.5 Bolts

# Extra stuff
I hope this can works out hwhwhw and later perhaps I can donate it to people that have difficulties in hearing or seeing. 
I think it will be more easy to them to just like having keyboard that capable of braille

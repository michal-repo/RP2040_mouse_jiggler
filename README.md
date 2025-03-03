# RP2040_mouse_jiggler

## If you liked it you can support my work
[!["Buy Me A Coffee"](https://raw.githubusercontent.com/michal-repo/random_stuff/refs/heads/main/bmac_small.png)](https://buymeacoffee.com/michaldev)



Raspberry Pi Pico RP2040 board based mouse jiggler.<br><br>
Board is detected as mouse, program is configured to move mouse every 30 seconds.

## Requirements

 - Raspberry Pi Pico
 - *USB-A* **<->** *micro USB* **cable**

## Additional information

CircuitPython enables mass storage device for user to save code on board. This repository includes `boot.py` file that disables this functionality. However there is implemented override to skip disabling mass storage device (allowing you to modify code on board).<br>
By default this version requires you to ground GPIO 14 pin (you need to short pin 14 and ground), on Raspberry Pi Pico GPIO 14 and ground are next to each other. Before connecting USB cable you need to short pin 14 and ground, you can use tweezers, pliers or even paper clip if your board do not have soldered pins.<br>
**If your board do not have GPIO 14 you need to modify `boot.py` file to use different pin.**

## How to

 - Download and install [CircuitPython binary](https://circuitpython.org/downloads) for your board version
 - Clone this repo

### Installing CircuitPython

 - Hold BOOTSEL/BOOT button on your board
 - Connect USB cable while holding button
 - New storage device will be mounted on your system
 - Copy CircuitPython binary file (*.uf2) directly on storage device **DO NOT UNPLUG DEVICE**
 - After few seconds your board will reboot and you'll see new storage device named *CIRCUITPY*

### Installing Mouse Jiggler

 - Copy content of `files` directory directly on your board's storage device
 - Program starts working immediately after copy is successful
 - **If you do not want to disable Mass Storage functionality of CircuitPython remove `boot.py` file before unplugging your board**

## Additional patterns

In directory `additional patterns` you can find different pattern.
 - `windows enhance pointer precision` works with mouse setting in Windows: "Enhance pointer precision"
 - `complex pattern` a bit more complicated pattern


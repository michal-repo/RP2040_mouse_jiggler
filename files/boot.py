import storage
import board, digitalio

# Grounding GPIO 14 enables mass storage
button = digitalio.DigitalInOut(board.GP14)
button.pull = digitalio.Pull.UP

if button.value:
   storage.disable_usb_drive()
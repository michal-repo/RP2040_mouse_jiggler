import time
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

time.sleep(5)

while True:
	mouse.move(x=20)
	time.sleep(0.2)
	mouse.move(x=-20)
	time.sleep(30)

import time
import usb_hid
from adafruit_hid.mouse import Mouse

mouse = Mouse(usb_hid.devices)

time.sleep(5)

while True:
	for sleeptime in [0.1,0.13,0.15]:
		for jump in [2,4,3,5,2,3]:
			if (jump % 2) == 0:
				mouse.move(x=jump, y=jump)
				time.sleep(sleeptime)
				mouse.move(x=-jump)
				time.sleep(sleeptime)
				mouse.move(x=-jump, y=-jump)
				time.sleep(sleeptime)
				mouse.move(x=jump)
			else:
				mouse.move(x=jump)
				time.sleep(sleeptime)
				mouse.move(y=-jump)
				time.sleep(sleeptime)
				mouse.move(x=-jump, y=jump)
			time.sleep(sleeptime*200)

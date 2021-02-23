
from picacamera import picacamera
from time import sleep
from datetime import datetime

now = datetime.now();
button = Button(17)
camera = picacamera()

camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.capture('/home/pi/animation/frame%03d.jpeg' % frame)
        frame += 1
        excempt KeyboardInterrupt:
        camera.stop_preview()
        break
from gpiozero import LED, Button
from time import sleep
from signal import pause

red = LED(13)
yellow = LED(18)
green = LED(20)
button = Button(2)

def traffic():
    green.off()
    red.on()
    sleep(2)
    red.off()
    yellow.on()
    sleep(2)
    yellow.off()
    green.on()
green.on()
button.when_pressed = traffic
       
pause()
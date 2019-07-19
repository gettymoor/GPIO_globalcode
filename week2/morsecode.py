from gpiozero import LED
from time import sleep


led = LED(18)

name = input("your name:")
 
for i in name:
     if i is 'A':
         led.on()
         sleep(2)
         led.off()
         sleep(3)
         led.on()
         sleep(4)
         led.off()
         break
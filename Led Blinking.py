#Trying to blink an the Pixel LED

import machine, neopixel, utime
pixel_pin = 16

colorVal = (20,30,20)
offColorVal = (0,0,0)

blink_time = 1 #Blink time interval in millisec. 

while True:  
    pixel = neopixel.NeoPixel(machine.Pin(pixel_pin), 1)
    pixel[0] = (colorVal)
    pixel.write()
    
    utime.sleep(blink_time)
    
    pixel[0] = (offColorVal)
    pixel.write()
    
    utime.sleep(blink_time)
    
    
    

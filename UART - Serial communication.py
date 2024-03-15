from machine import UART, Pin
import utime


while True:
    uart1 = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))
    uart1.write('hello')  # write 5 bytes
    uart1.read(5)
    utime.sleep(2)

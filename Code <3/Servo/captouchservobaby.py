import board
import time
import pulseio
import touchio
from adafruit_motor import servo

touch_prim = board.A3 #connecting analog pin to wire
touch_prime = board.A4

touch_prim = touchio.TouchIn(board.A3) #setting wire as input
touch_prime = touchio.TouchIn(board.A4)

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50) #setting pulse to output


servobaby = servo.Servo(pwm)

while True:
    
    if touch_prim.value: #wire connected to pin A3 is touched
        for angle in range(0, 180, 2):
            servobaby.angle = angle #servo moves
            print("don't touch me!")
            
    elif touch_prime.value:
        for angle in range(180, 0, -2):
            servobaby.angle = angle
            print("Please hold me!")
            
    else: # no connection
        servobaby.angle= 0
        time.sleep(0.05)
    
   
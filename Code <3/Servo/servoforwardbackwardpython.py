import board
import time
import pulseio
import digitalio
from adafruit_motor import servo

pwm = pulseio.PWMOut(board.A2,duty_cycle=2 ** 15, frequency=50)

servobaby = servo.Servo(pwm)

while True:
    for angle in range (0, 180, 5):
        servobaby.angle = angle
        time.sleep(0.05)
    for angle in range (180, 0, -5):
        servobaby.anglev = angle
        time.sleep(0.05)
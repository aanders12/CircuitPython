import board
import time
import touchio


touch_prim = board.A2
touch_prime = board.A4


touch_prim = touchio.TouchIn(board.A2)
touch_prime = touchio.TouchIn(board.A4)


while True:
    if touch_prim.value:
        print ("don't touch me!")
    if touch_prime.value:
        print ("please! don't touch me!")
    time.sleep (0.05)
    
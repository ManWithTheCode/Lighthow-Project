# Lighthow-Project
'''
Create a lightshow for the Jack-o-lantern.  
It must use multiple colors that are associated with the holiday. 
It must demonstrate multiple lighting effects (at least 5 different ones).  
'''
import board
import neopixel
import time
import random
BRIGHTNESS = 1.0
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=BRIGHTNESS, auto_write=False)
num_pixels = 10
# Changes the opacity for selected colors/elements from visible to hidden.
def fade_out(color, sec=0.001):
    mx = max(color[0], max(color[1], color[2]))
    r_inc = color[0]/mx
    g_inc = color[1]/mx
    b_inc = color[2]/mx
    while color[0] >= 0 and color[1] >= 0 and color[2] >= 0:
        color[0] -= r_inc
        color[1] -= g_inc
        color[2] -= b_inc
        rgb.fill((int(color[0]), int(color[1]), int(color[2])))
        rgb.show()
        time.sleep(sec)
# Changes Opacity and makes the color visible again after the fadeout 
def fade_in(color, sec=0.001):
    r, g, b = color
    r1 = r
    g1 = g
    b1 = b
    mx = max(color[0], max(color[1], color[2]))
    r_inc = color[0]/mx
    g_inc = color[1]/mx
    b_inc = color[2]/mx
    r = 0
    b = 0
    g = 0
    while r < r1 and g < g1 and b < b1:
        r += r_inc
        g += g_inc
        b += b_inc
        rgb.fill((int(r), int(g), int(b)))
        rgb.show()
        time.sleep(sec)
# Sparkle puts some colors into view on one side and puts other colors on the other side.
def sparkle(color1, color2, delay):
    np.fill(color1)
    for i in range(4):
        np[random.randint(0, 9)] = color2
    np.show()
    time.sleep(delay)
# Creates a flame effect on a strip of neopixels
def fire(background, foreground, delay=0.1):
    for j in range(20):
        intensity = random.random() * 0.1 + 0.3
        i_background = [int(i * intensity) for i in background]
        np.fill(i_background)
        for i in range(random.randint(2, int(num_pixels/5))):
            intensity = random.random() * 0.1 + 0.3
            i_foreground = [int(i * intensity) for i in foreground]
            np[random.randint(0, num_pixels-1)] = i_foreground
        np.show()
        time.sleep(delay)
# Chase makes one color follow another color on a linear path.
def chase(color1, color2, loop=20, count=3, delay=0.1):
    result = 0
    for outer in range(count * loop):
        np.fill(color1)
        for i in range(num_pixels):
            if i % count == result:
                np[i] = color2
        np.show
        time.sleep(delay)
        result += 1
        result %= count
        np.show()
while True:
    for i in range(10):
        fire(
    
  



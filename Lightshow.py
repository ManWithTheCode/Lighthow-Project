# Lighthow-Project
'''
Create a lightshow for the Jack-o-lantern.  
It must use multiple colors that are associated with the holiday. 
It must demonstrate multiple lighting effects (at least 5 different ones).  
'''
# Lighthow-Project
'''
Create a lightshow for the Jack-o-lantern.
It must use multiple colors that are associated with the holiday.
It must demonstrate multiple lighting effects (at least 5 different ones).
'''
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
BRIGHTNESS = 0.5
np = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=BRIGHTNESS, auto_write=False)
num_pixels = 10
# Changes the opacity for selected colors/elements from visible to hidden.
def fade_out(color, increment):
    rgb = color
    maximum = max (rgb[0], max(rgb[1], rgb[2]))
    r_inc = rgb[0] / maximum
    g_inc = rgb[1] / maximum
    b_inc = rgb[2] / maximum
    r, g, b = rgb
    while r >= 0 and g >= 0 and b >= 0:
        r -= r_inc
        g -= g_inc
        b -= b_inc
        np.fill((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)

# Changes Opacity and makes the color visible again after the fadeout
def fade_in(color, increment):
    rgb = color
    r, g, b = rgb
    r_final = r
    g_final = g
    b_final = b
    print(r_final, g_final, b_final)
    maximum = max(rgb[0], max(rgb[1], rgb[2]))
    r_inc = rgb[0] / maximum
    g_inc = rgb[1] / maximum
    b_inc = rgb[2] / maximum
    r, g, b = 0, 0, 0
    while r <= r_final and g <= g_final and b <= b_final:
        r += r_inc
        g += g_inc
        b += b_inc
        np.fill((int(r), int(g), int(b)))
        np.show()
        time.sleep(increment)

# Sparkle puts some colors into view on one side and puts other colors on the other side
def sparkle(color1, color2, delay):
    np.fill(color1)
    for i in range(4):
        np[random.randint(0, 9)] = color2
    np.show()
    time.sleep(delay)

def constrain(low, high, value):
    if value < low:
        return low
    if value > high:
        return high
    return value

np.fill((255, 127, 0))
np.show()

def light(back, fore):
    ran = random.random()/20
    for j in range(10):
        intense = random.random() * 0.7 + 0.3
        i_back = [int(i * intense) for i in back]
        np.fill(i_back)
        for i in range(random.randint(2, int(num_pixels/5))):
            intense = random.random() * 0.7 + 0.3
            i_fore = [int(i * intense) for i in fore]
            np[random.randint(0, num_pixels-1)] = i_fore
        np.show()
        time.sleep(ran)
# Creates a flame effect on a strip of neopixels
def fire(background, foreground):
    for j in range(45):
        intensity = random.random() * 0.7 + 0.3
        i_background = [int(i * intensity) for i in background]
        np.fill(i_background)
        for i in range(random.randint(2, int(num_pixels/5))):
            intensity = random.random() * 0.7 + 0.3
            i_foreground = [int(i * intensity) for i in foreground]
            np[random.randint(0, num_pixels-1)] = i_foreground
        np.show()
        time.sleep(0.06)

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
    for i in range(2):
        fire((30, 1, 46), (214, 104, 11))
        light((255, 129, 0), (255, 129, 0))
        fire((101, 83, 0), (214, 104, 11))
    fade_out([36, 2, 120], 0.01)
    fade_in([0, 75, 0], 0.01)
    fade_out([0, 75, 0], 0.01)
    chase((58, 0, 0), (30, 1, 46))
    for i in range(5):
        sparkle((44, 135, 50) , (44, 135 , 40) , 5)











    
  



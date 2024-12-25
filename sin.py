"""
	Just a code to calculate the sin and cos from 0 to 90 at an increment of 0.25
"""
import math
x=0.0
lim=90.0
inc=0.25

while x<=lim:
    rad=math.radians(x)
    y=math.sin(rad)
    z=math.cos(rad)

    print("%s:%s"%(y,z))
    x+=inc

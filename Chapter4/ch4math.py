# ch4math.py
# Q: what does 'import' do?
# A: cretes a "module object"
# the module object contains the functions
# and variables defined in the module
# these functions and variables can be accessed 
# using dot.notation    

import math

print(math)

signal_power = 10
noise_power = 2

ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
print 'decibels = ', decibels

# this example prints the sine of radians
radians = .7
height = math.sin(radians)

print(height)

#convert from degrees to radians
# divide by 360 and multiply 2 * pi
degrees = 45
radians = degrees / 360.0 * 2 * math.pi
print 'sine after convert degrees =', math.sin(radians)

# print square root 4 / 2
print math.sqrt(4) / 2.0

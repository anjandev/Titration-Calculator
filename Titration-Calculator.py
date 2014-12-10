# Titration calculator. By Anjan Momi. 
# Use http://www.codeskulptor.org/

import math

vol_OH = float(input("Enter the Volume of OH-"))

# Change this to your needs
vol_H3O = 25.0
concentration_OH = 0.1
concentration_H3O = 0.1

concentration_OH = concentration_OH * vol_OH / (vol_H3O + vol_OH)

concentration_H = concentration_H3O * vol_H3O / (vol_H3O + vol_OH)

# This could happen behind the scenes but I feel more
# certain about the numbers this program outputs if 
# I can see the input.
print "concentration of OH- is", concentration_OH
print "concentration of H3O+ is",concentration_H

if concentration_OH == concentration_H:
    print "Neutral. pH = 7"
elif concentration_OH > concentration_H:
    excess_OH = concentration_OH - concentration_H
    print math.log(excess_OH, 10) + 14
else:
    excess_H3O = concentration_H - concentration_OH
    print - math.log(excess_H3O, 10)

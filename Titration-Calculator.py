# Titration calculator. By Anjan Momi. 
#{Calculates the pH at various stages of the titration of a strong acid against a strong base.}
# Copyright (C) {2014}  {Anjandev Momi}
# Contact me at anjan@momi.ca
# Use http://www.codeskulptor.org/ to run this program.

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

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

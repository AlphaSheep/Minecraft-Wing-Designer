'''
Minecraft Wing Designer
Version 1.02

Outputs text files containing layers of blocks which make up a user-specified aircraft wing.
Copyright (C) 2012 Brendan James Gray

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
'''

#=========================================================================
#           INPUT PARAMETERS
#=========================================================================

rootchord = 20 # length from front to back of wing root in blocks
halfSpan = 23 # length from root to tip in blocks
tpc = 0.10 # thickness to chord ratio
taper = 0.28 # taper ratio
leSweep = 42.5 #deg (leading edge sweep)
dihedral = 8.2 #deg (positive for upward pointing, negative for downward pointing)
y0 = 5 # the y coord at the chordline of the root
# The program fits a symmetrical NACA 4-series.

#=========================================================================

blockchar = '[_]'
spacechar = ' . '

#=========================================================================



# Coordinate definitions:
#   x : chordwise
#   y : vertical
#   z : spanwise


import math



def airfoilCoords(xpc,tpc):
    ''' returns the top y coord for a given x coord, thickness ratio and chord'''
    yt = tpc/0.2*(0.2969*(xpc**0.5) - 0.1260*xpc - 0.3516*(xpc**2) + 0.2843*(xpc**3) - 0.1015*(xpc**4))
    # source: http://en.wikipedia.org/wiki/NACA_airfoil#Equation_for_a_symmetrical_4-digit_NACA_airfoil
    return yt


def getBoundingBox(tpc,chord,halfSpan,taper,y0,leSweep,dihedral):
    ycroot = y0 
    yctip = y0 + halfSpan * math.tan(dihedral/180*math.pi)
    ytroot = ycroot + tpc*chord 
    yttip = yctip + tpc*chord*taper
    ybroot = ycroot - tpc*chord
    ybtip = yctip - tpc*chord*taper
    minz = math.floor(0)
    maxz = math.ceil(halfSpan)
    minx = math.floor(0)
    maxx = math.ceil(halfSpan*(math.tan(leSweep*math.pi/180))+(taper)*rootchord)
    miny = math.floor(min([1,ybtip,ybroot]))-1
    maxy = math.ceil(max([ytroot,yttip]))+1
    return [[minx,miny,minz],[maxx,maxy,maxz]]

BB = getBoundingBox(tpc,rootchord,halfSpan,taper,y0,leSweep,dihedral)
minx,miny,minz = BB[0][0],BB[0][1],BB[0][2] 
maxx,maxy,maxz = BB[1][0],BB[1][1],BB[1][2]
print(BB)

layer = []

for z in range(minz,maxz,1):
    chord = rootchord*(1-(1-taper)*z/halfSpan)
   # tpc = roottpc * chord/rootchord
    xle = z*math.tan(leSweep*math.pi/180)
    xte = xle + chord
    thickness = tpc*chord
    
    singleLayer = []
    for x in range(minx,maxx,1):
        line = []
        yc = y0 + z*math.tan(dihedral/180*math.pi)
        if (x > xle) and (x < xte):
            xpc = (x-xle)/(xte-xle)
            
            
            yFree = airfoilCoords(xpc,tpc) * (xte-xle)
            yt = yc + yFree
            yb = yc - yFree
            
            for y in range(miny,maxy,1):
                if (y < yt + 0.5) and (y > yb-0.5):
                    line.append(True)
                else:
                    if (thickness<1) and (y == math.floor(yc)):
                        line.append(True)
                    else:
                        line.append(False)
        else:
            for y in range(miny,maxy,1):
                line.append(False)
        singleLayer.append(line)
    layer.append(singleLayer)            

# -- Display Output - By vertical cross sections

outfile = open('wingcrosssections.txt','w')
outputstring = ''
                     
for z in range(minz,maxz,1):
    outputstring = outputstring + '\n\n    z = '+str(z)+'\n#'
    
    for y in range(maxy-1,miny-1,-1):
        for x in range(minx,maxx,1):
            if layer[z][x][y]:
                outputstring = outputstring + blockchar
            else:
                outputstring = outputstring + spacechar
        outputstring = outputstring + '#'+str(y)+'\n#'
    for x in range(minx,maxx,1):
        outputstring = outputstring + str(x % 10)
        for i in range(len(blockchar)-1):
            outputstring = outputstring + ' '

outfile.write(outputstring)
outfile.close()

# -- Display Output - By horizontal layers

outfile = open('winglayers.txt','w')
outputstring = ''
                     
for y in range(miny,maxy,1):
    outputstring = outputstring + '\n\n    z = '+str(y)+'\n#'
    
    for x in range(minx,maxx,1):
        for z in range(minz,maxz,1):
            if layer[z][x][y]:
                outputstring = outputstring + blockchar
            else:
                outputstring = outputstring + spacechar
        outputstring = outputstring + '#'+str(x)+'\n#'
    for z in range(minz,maxz,1):
        outputstring = outputstring + str(z % 10)
        for i in range(len(blockchar)-1):
            outputstring = outputstring + ' '

outfile.write(outputstring)
outfile.close()

print('Done...')

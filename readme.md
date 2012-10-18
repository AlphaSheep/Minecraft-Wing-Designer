# Minecraft Wing Designer

### version 1.02

Outputs text files containing layers of blocks which make up a user-specified aircraft wing.

## 1. Introduction

`MCWingDesign.py` is a python script that aids in the construction of aircraft in Minecraft. In order to run it, you will need a working installation of the Python programming language.

The program takes a small number of parameters and calculates the dimensions of the wing. It then calculates the layout of discrete blocks that could be used to mount 

## 2. Installation

Unzip the contents into a directory of your choice. The script is ready to run.

## 3. Usage

Open `MCWingDesign.py` in your prefered text editor. Edit the input parameters to match those of your desired wing.

If you are not sure of the parameters of the wing, then you can measure them off a scale drawing. You can easily find 
such a drawing by entering the name of your aircraft along with "3 view" into your prefered search engine. Once you have the 
drawing, scale it if necessary (larger is better), and open it in an image editor that allows you to read off coordinates 
of points. You can then measure or calculate the relevant lengths and angles.

The following parameters that are required.

  * *[Root Chord](http://en.wikipedia.org/wiki/Chord_(aircraft))* - Distance from the front to the back of the wing at the point where it meets the fuselage.
  * *[Half Span](http://en.wikipedia.org/wiki/Wing_span)* - Shortest horizontal distance from the tip of the wing to the fuselage.
  * *[Thickness to Chord Ratio](http://en.wikipedia.org/wiki/Airfoil#Airfoil_terminology)* - The ratio of the thickness of the wing to the chord. Most easily measured at the root.
  * *[Taper ratio](http://en.wikipedia.org/wiki/Chord_(aircraft)#Tapered_wing)* - The chord at the wing tip divided by the chord at the root.
  * *[Leading Edge Sweep](http://en.wikipedia.org/wiki/Swept_wing)* - The sweep angle measured in the top view along leading edge of the wing.
  * *[Dihedral Angle](http://en.wikipedia.org/wiki/Dihedral_(aircraft))* - The angle of the wing from the horizontal in the front view.
  * *y0* - The y coordinate of the centreline of the wing root.

There are also two optional parameters: the character combinations used to represent blocks and empty spaces in the output text files.

The script assumes that the airfoil is a symmetrical NACA 4-series airfoil. This is accurate enough for all but very large builds (that is, chords of more than 50 m). Should you need a different airfoil shape, you may edit the `airfoilCoords` function. If you need an airfoil that is not symmetrical, you will need to add an additional function for the bottom surface.

To run the program, simply call `MCWingDesign.py` in python. The script will output two text files in the same directory (WARNING: existing files will be overwritten). `wingcrosssections.txt` consists of vertical cross sections moving from the root outward, which is suited to building in Creative mode). `winglayers.txt` consists of horizontal layers moving from the ground up, and is more suited to building in Survival mode or without flying.

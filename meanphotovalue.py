# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 05:24:15 2019
REQUIREMENTS:
    1) PNG/TIF images
    2) named as {integer}.png or {integer}.tif. The integer should correspond to which frame of motion is looked at. 
Made for black and white photography of gaussian beam cross sections.  
Frame by frame analysis of the beams motion/position.
Program uses the pixel coordinates weighted by their respective intensity value to estimate the center of the beam.
@author: Bennett
"""
import os
import matplotlib.pyplot as plt
from PIL import Image
xcenters=[]
ycenters=[]
files=[]
for filename in os.listdir(r'C:\Users\Bennett\Desktop\pics'):
    name=str(filename)
    if name.endswith(.png)==True:
        files.append(int(name.rstrip('.png')))
    if name.endswith(.tif)==True:
        files.append(int(name.rstrip('.tif')))
    print("Finding value for: ", str(filename))
    im=Image.open(r'C:\Users\Bennett\Desktop\pics\{}'.format(filename))
    xmin,ytop,xmax,ybot=im.getbbox()
    xweight=0
    yweight=0
    totweight=0
    for i in range(xmin,xmax):
        for j in range(ytop,ybot):
            weight=im.getpixel((i,j))
            if weight<20:
                pass
            else:
               xweight+=i*weight
               yweight+=j*weight
               totweight+=weight
    xcenter=xweight/totweight
    ycenter=yweight/totweight
    xcenters.append(xcenter)
    ycenters.append(ycenter)

plt.figure(1)
plt.scatter(files,xcenters)
plt.xlabel("Frame")
plt.ylabel("Pixel Position")
plt.title("Central x-Position")
plt.figure(2)
plt.scatter(files,ycenters)
plt.xlabel("Frame")
plt.ylabel("Pixel Position")
plt.title("Central y-Position")

plt.show()

            

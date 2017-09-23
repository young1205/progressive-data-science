"""
###############################################################################

 Import libraries

###############################################################################
"""
from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math 
from random import randint


def islineintersect(line1, line2):
    i1 = [min(line1[0][0], line1[1][0]), max(line1[0][0], line1[1][0])]
    i2 = [min(line2[0][0], line2[1][0]), max(line2[0][0], line2[1][0])]
    ia = [max(i1[0], i2[0]), min(i1[1], i2[1])]
    if max(line1[0][0], line1[1][0]) < min(line2[0][0], line2[1][0]):
        return False
    m1 = (line1[1][1] - line1[0][1]) * 1. / (line1[1][0] - line1[0][0]) * 1.
    m2 = (line2[1][1] - line2[0][1]) * 1. / (line2[1][0] - line2[0][0]) * 1.
    if m1 == m2:
        return False
    b1 = line1[0][1] - m1 * line1[0][0]
    b2 = line2[0][1] - m2 * line2[0][0]
    x1 = (b2 - b1) / (m1 - m2)
    if (x1 < max(i1[0], i2[0])) or (x1 > min(i1[1], i2[1])):
        return False
    return True
    
print(2*math.pi/20.0)

a = np.arange(0,2*math.pi, .0001)
x = 10 + 10 * np.cos(a)
y = 10 + 10 * np.sin(a)

campers = np.arange(0,2*math.pi, 2*math.pi/20.0)
xc = 10 + 10 * np.cos(campers)
yc = 10 + 10 * np.sin(campers)


x_list = xc.tolist()
y_list = yc.tolist()

#print(len(x_list))

EOW = 0
monte = 100
for six in range(0,monte):
    Abe = randint(0, 19)
    Betty = randint(0, 19)
    while Abe == Betty:
        Betty = randint(0, 19)
    Candace = randint(0, 19)
    while ((Candace == Betty) or (Candace == Abe)):
        Candace = randint(0, 19)
    Dan = randint(0, 19)
    while ((Dan == Betty) or (Dan == Abe) or (Dan == Candace)):
       Dan = randint(0, 19)
            
    #print(Abe, Betty, Candace, Dan)
    
        
    plt.plot(x,y)
    plt.plot(xc,yc, '*', color='red')
    plt.plot([x_list[Abe],x_list[Candace]],[y_list[Abe],y_list[Candace]], color = 'purple')
    plt.plot([x_list[Betty],x_list[Dan]],[y_list[Betty],y_list[Dan]], color = 'green')
    plt.show()
    
    line1 = np.zeros((2,2))
    line2 = np.zeros((2,2))
    
    line1[0][0] = x_list[Abe]
    line1[1][0] = x_list[Candace]
    line1[0][1] = y_list[Abe]
    line1[1][1] = y_list[Candace]
    
    line2[0][0] = x_list[Betty]
    line2[1][0] = x_list[Dan]
    line2[0][1] = y_list[Betty]
    line2[1][1] = y_list[Dan]
    
    isinter = islineintersect(line1, line2)
    if isinter :
        print("End of World!")
        EOW = EOW + 1
        
print(EOW/monte)
    

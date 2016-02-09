####
#
# Night Falls. A Storm Rolls In. Can You Cross The River?
#
#
# This code was written to solve the following problem
# http://fivethirtyeight.com/features/night-falls-a-storm-rolls-in-can-you-cross-the-river/
#
#

import numpy as np
import matplotlib.pyplot as plt
import random

# This is where we calculate structure
Wide = 3
Long = 2
Num_Bridge = 2*Wide*Long+Wide-Long
Num_Islands = Wide*Long

print Num_Bridge 
#print Num_Islands

#### Fill Islands Coordinates
id_I = np.arange(Num_Islands)
x_I = np.zeros(Num_Islands)
y_I = np.zeros(Num_Islands)

count = 0
for xix in range(0,Wide):
    for yix in range(0,Long):
        print yix, xix
        x_I[count] = xix
        y_I[count] = yix
        count +=1

### Fill Bridge Coordinates
Bridges = np.zeros((Num_Bridge, 4))

count = 0
for ix in range(0,Num_Bridge):
    Bridges[ix,3] = random.randrange(0, 2)

for xix in range(0,Wide-1):
    for yix in range(0,Long):
        print yix, xix
        Bridges[count,1] = xix + 0.5
        Bridges[count,2] = yix
        Bridges[count,0] = count
        count +=1

for xix in range(0,Wide):
    for yix in range(0,Long+1):
        print yix, xix
        Bridges[count,1] = xix 
        Bridges[count,2] = yix -0.5
        Bridges[count,0] = count
        count +=1
        
print Bridges
##### Did Bridge Fail?

B_fail = Bridges[:,3] < 0.5
No_Bridges = Bridges[B_fail,:]

        
#### Make Plots             
xbig = max(x_I) +1
ybig = max(y_I) +1
xsm = min(x_I) -1
ysm = min(y_I) -1

fig, ax = plt.subplots()
ax.plot(x_I, y_I, 'o')
ax.plot(Bridges[:,1], Bridges[:,2], 'x')
ax.plot(No_Bridges[:,1], No_Bridges[:,2], '*')
ax.set_ylim((ysm, ybig))
ax.set_xlim((xsm, xbig))

plt.show()
#plt.savefig("plt"+var+".png")

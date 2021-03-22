#!/usr/bin/python
import numpy as np

#Create a cube centered around the origin
cube = np.matrix(((-1,1,-1,-1,1,-1,1,1),(-1,-1,1,-1,-1,1,1,1),(-1,-1,-1,1,1,1,-1,1)))

#####################################################################################
"""
Defining the matrices initially used to find all rotations.
"""

#The Identity matrix
identity = np.matrix(((1,0,0),(0,1,0),(0,0,1)))

#90 degree rotation about z axis
zrot = np.matrix(((0,-1,0),(1,0,0),(0,0,1)))

#180 degree rotation
rot180 = np.matrix(np.array([(0,0,1),(0,-1,0),(1,0,0)]))

#120 degree rotation
rot120 = np.matrix(np.array([((0,1,0),(0,0,1),(1,0,0))]))

#####################################################################################
"""
Compiling more matrices.
"""

rotations = [identity,zrot,rot180,rot120]

"""
Stole from Hollis :)
"""

for i in range(10000):
    count = 0
    random1 = np.random.randint(len(rotations))
    random2 = np.random.randint(len(rotations))
    newrot = rotations[random1]*rotations[random2]
    for j in range(len(rotations)):
        if np.all(newrot == rotations[j]):
            continue
        else:
            count += 1 
    if count == len(rotations):
        print("New matrix added!")
        rotations.append(newrot)

#print("There are " + str(len(rotations)) + " matrices to rotate the cube.")

#####################################################################################
"""
Making sure all matrices are SO(3).
"""

SO3check = 0

for i in rotations:
    if np.linalg.det(i) == -1:
        SO3check += 1

if SO3check == 0:
    print("All matrices are SO(3)!")

else:
    print("Some matrices are not SO(3)!")

#####################################################################################

"""
Prints each matrix.
"""

for rot in rotations:
    print(rot)
    print('-----------------')

#####################################################################################

"""
Bonus with new angle rotation!
"""

rotationplus = []
for rot in rotations:
    rotationplus.append(rot)

angle = np.radians(175)
cos = np.cos(angle)
sin = np.sin(angle)

rot175 = np.matrix(((cos,-sin,0),(sin,cos,0),(0,0,1)))
rotationplus.append(rot175)
for rot in rotationplus:
    print(rot)
    print('--------------')

for i in range(1000000):
    count = 0
    random3 = np.random.randint(len(rotationplus))
    random4 = np.random.randint(len(rotationplus))
    newrot = rotationplus[random3]*rotationplus[random4]
    for j in range(len(rotationplus)):
        if np.all(newrot == rotationplus[j]):
            continue
        else:
            count += 1 
    if count == len(rotationplus):
        print("New matrix added!")
        rotationplus.append(newrot)

print("There are " + str(len(rotationplus)) + " matrices to rotate the cubeplus.")
#####################################################################################

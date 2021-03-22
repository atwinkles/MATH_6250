import numpy, math
# To find these rotations, I simply drew a two dimensional
# square and noticed to get a ccl rotation which would be about
# the z-axis I would need:
# 0 -1 
# 1  0
#
# From here using the right hand rule (zrotation x -> y)
# I was able to determine the correct placement of the
# -1. (x_rotation: y -> z)
#     (y_rotation: z -> x)
#
# Thus, the final rotations are:
#
# rotation about the x-axis: 1  0  0
#                            0  0 -1
#                            0  1  0
#
# rotation about the y-axis: 0  0  1
#                            0  1  0
#                           -1  0  0
#
# rotation about the z-axis: 0 -1  0
#                            1  0  0
#                            0  0  1
# Oh! and we can't forget about the identity.

identity_rotation = numpy.matrix(( (1,0,0), (0,1,0), (0,0,1)))

x_rotation = numpy.matrix(( (1,0,0), (0,0,-1), (0,1,0)))
y_rotation = numpy.matrix(( (0,0,1), (0,1,0),  (-1,0,0)))
z_rotation = numpy.matrix(( (0,-1,0),(1,0,0),  (0,0,1)))
# Since you can rotate a face three times before returning
# to the original position, there are a total of 9 face rotations.

# Now, we have that loaded into python to be toyed with later.
#
# Next, let's look at the 120 deg rotations about the coners.
# Because there are eight corners of a cube, it follows that
# there are 4 axis of symmetry and that makes 4 rotational 
# matrices. To find this I pick a point (-1,1,1) and observe 
# that the rotation about the point (1,1,1)
# would take it to (1,-1,1) and then (1,1,-1).
# Since this just shifts the elements to the next position, the
# matrix for this will be: 
# 
#     0 1 0
#     0 0 1
#     1 0 0
# 
# Next let's look at the rotation about the point (-1,1,1)
# The path of points looks like: (1,1,1) -> (-1,1,-1) -> (-1,-1,1)
# Using the previous matrix as a template I thought of the matrix:
#
#     0 -1  0
#     0  0  1
#    -1  0  0
# 
# A simple check verifies that this is indeed that rotation.
# 
# Follwing next rotation about the point (-1,-1,1). The path is
# (-1,1,1) -> (-1,-1,-1) -> (1,-1,1)
# Similarly, the matrix for this is:
#
#   0  0 -1
#   1  0  0
#   0 -1  0    
# 
# Finally, the last rotation of this kind is about the point (1,-1,1).
# The path is: (-1,-1,1) -> (1,-1,-1) -> (1,1,1)
# 
#   0 -1  0
#   0  0 -1
#   1  0  0
#
# So, here are all of the "Corner Rotations":
#
#   z = x+y    z = y-x   z=-(x+y)    z = x-y
#   0  1  0    0 -1  0    0  0 -1    0 -1  0
#   0  0  1    0  0  1    1  0  0    0  0 -1
#   1  0  0   -1  0  0    0 -1  0    1  0  0
#
# Now, I will insert this into the program. notice there are a 
# total of two rotations for each before returning to the original
# position. So, there are a total of eight possible corner rotations.
# I also checked to make sure that these were all det(A) = 1
corner1_rotation = numpy.matrix(( (0, 1, 0),(0,0, 1),( 1, 0,0)))
corner2_rotation = numpy.matrix(( (0,-1, 0),(0,0, 1),(-1, 0,0)))
corner3_rotation = numpy.matrix(( (0, 0,-1),(1,0, 0),( 0,-1,0)))
corner4_rotation = numpy.matrix(( (0,-1, 0),(0,0,-1),( 1, 0,0)))

# Finally, the last type of rotation is the rotation about an edges
# midpoint. This will be a rotation by 180 deg about the edge midpt.
# To find these, I similarly just drew a cube and then drew axis 
# through the mid points. Since there are twelve edges, it follows 
# that there are six axis of rotational symmety.
# The six axis are:  
# Here I labelled the points of the cube:
A = numpy.matrix(( (1),(1),(1)))
B = numpy.matrix(( (1),(1),(-1)))
C = numpy.matrix(( (1),(-1),(-1)))
D = numpy.matrix(( (1),(-1),(1)))
E = numpy.matrix(( (-1),(1),(1)))
F = numpy.matrix(( (-1),(1),(-1)))
G = numpy.matrix(( (-1),(-1),(-1)))
H = numpy.matrix(( (-1),(-1),(1)))

# So to define the axis, it is the line through two midpoints.
# a : line(mid(A,B),mid(H,G))
# b : line(mid(B,C),mid(E,H))
# c : line(mid(C,D),mid(F,E))
# d : line(mid(D,A),mid(G,F))
# e : line(mid(A,E),mid(C,G))
# f : line(mid(B,F),mid(D,H))
#
# The corresponding matrices are:
#
# a: 0  1  0
#    1  0  0
#    0  0 -1
#
# b: 0  0 -1
#    0 -1  0
#   -1  0  0
#
# c: 0 -1  0
#   -1  0  0
#    0  0 -1
#
# d: 0  0  1
#    0 -1  0
#    1  0  0
#
# e:-1  0  0
#    0  0  1
#    0  1  0
#
# f:-1  0  0
#    0  0 -1
#    0 -1  0
# Now, we will input these!
a_rotation = numpy.matrix(( (0,1,0),(1,0,0),(0,0,-1)))
b_rotation = numpy.matrix(( (0,0,-1),(0,-1,0),(-1,0,0)))
c_rotation = numpy.matrix(( (0,-1,0),(-1,0,0),(0,0,-1)))
d_rotation = numpy.matrix(( (0,0,1),(0,-1,0),(1,0,0)))
e_rotation = numpy.matrix(( (-1,0,0),(0,0,1),(0,1,0)))
f_rotation = numpy.matrix(( (-1,0,0),(0,0,-1),(0,-1,0)))

# I think this is all of the basic ones.. I'm imagining when I multipy
# these together I will obtain a total of 24 unique cube configurations

cube_rotations = [identity_rotation,x_rotation,y_rotation,z_rotation,corner1_rotation,corner2_rotation,corner3_rotation,corner4_rotation,a_rotation,b_rotation,c_rotation,d_rotation,e_rotation,f_rotation]

#Check to ensure they are all an element of SO(3) by checking the det
check =0

for z in range(len(cube_rotations)):
    if  numpy.linalg.det(cube_rotations[z]) == -1.0:
	check += 1

for z in range(len(cube_rotations)):
    for x in range(len(cube_rotations)):
        if x != z and numpy.all(cube_rotations[x] == cube_rotations[z]):
            print x, z
 	    check += 1
if check== 0:
    print "All matrices so far unique and det(Matrices) = 1.0!!"

# Now that we have verified they are all indeed unique!!
# I think next I will do the random matrix multiplication
# to ensure that there are only 24 different rotations.
random_int = 0
random_int2 = 0
count = 0
# I want to run 100,000 random checks of the set of cube rotations
for x in range(100000):
    count = 0
    random_int = numpy.random.randint(len(cube_rotations)) 
    random_int2 = numpy.random.randint(len(cube_rotations))
    new_matrix = cube_rotations[random_int].dot(cube_rotations[random_int2])
    for y in range(len(cube_rotations)):
	if numpy.all(new_matrix == cube_rotations[y]):
	    continue
        else:
            count += 1
    if count == len(cube_rotations):
        print "New matrix added!"
        cube_rotations.append(new_matrix)

print "The number of cube rotations are "+ str(len(cube_rotations))

for x in cube_rotations:
    print x
    print ""

for z in range(len(cube_rotations)):
    if  numpy.linalg.det(cube_rotations[z]) == -1.0:
        check += 1


for z in range(len(cube_rotations)):
    for x in range(len(cube_rotations)):
        if x != z and numpy.all(cube_rotations[x] == cube_rotations[z]):
            print x, z
            check += 1
if check== 0:
    print "All matrices are still unique and det(Matrices) = 1.0!!"


# So in conclusion, there are only 24 unique rotations as anticipated.
# Further tests showed that they are all unique and have a positive
# 1.0 determinant!



# The Final Matrices are shown if you run this script. You need
# only numpy, math and python to run it. Enjoy!

# Now, I want to be able to create random arbitrary rotations.
# Recalling from Linear Algebra, we found that we can have a 
# general rotation using the R = R_z (a) R_y (b) R_x (c) for 
# the representation of the rotation about each axis..
a = 0
b = 0
c = 0
R_x =  numpy.matrix(( (1,0,0),(0,math.cos(c),-1*math.sin(c)),(0,math.sin(c),math.cos(c))))

R_y = numpy.matrix(( (math.cos(b),0,math.sin(b)),(0,1,0),(-1*math.sin(b),0,math.cos(b))))

R_z = numpy.matrix(( (math.cos(a), -1*math.sin(a),0),(math.sin(a),math.cos(a),0),(0,
0,1)))

random_rotations_about_origin = []

for v in range(100000):
    a = 2.0*math.pi*numpy.random.rand
    b = 2.0*math.pi*numpy.random.rand
    c = 2.0*math.pi*numpy.random.rand
    random_rotation_matrix = R_z.dot(R_y.dot(R_x))
    random_rotations_about_origin.append(random_rotation_matrix)

# So here we just created many arbitrary rotations of the cube.. I 
# wasn't too sure of what was wanted to be done here, but this is 
# what I thought it would be asking..

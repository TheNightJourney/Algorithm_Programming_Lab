# Find a point on a graph.
# Input the X and Y points of two points, and output the third point.
# When p = (0, 0) and q = (1, 1), r= (2, 2)
# When p = (1, 1) and q = (2, 2), r = (3, 3)

px = float(input("Enter the point px: "))
py = float(input("Enter the point py: "))
qx = float(input("Enter the point qx: "))
qy = float(input("Enter the point qy: "))

x = qx - px
y = qy - py

rx = float(qx + x)
ry = float(qy + y)

print("R would be:", "(", rx , ",", ry, ")")
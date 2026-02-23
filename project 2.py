from math import sin, cos, acos, pi
print("Enter circle calculation")
radius=float(input("Enter radius of circle: "))
y1 = float(input("starting point-Enter latitude: "))
x1 = float(input("starting point-Enter longitude: "))
y2 = float(input("ending point-Enter latitude: "))
x2 = float(input("ending point-Enter longitude: "))
y1 = y1 * pi / 180
y2 = y2 * pi / 180
x1 = x1 * pi / 180
x2 = x2 * pi / 180
distance = acos(sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1)) * radius
print("Distance between two points is:", distance)
round_distance = round(distance, 2)
print("Distance between two points rounded to 2 decimal places is:", round_distance)

def area():
    length = float(input("What is the length of your house?: "))
    width = float(input("What is the width of your house?: "))
    t_area = length * width
    return t_area

def circumference():
    pi = 3.14
    radius = float(input("What is the radius of the circle?: "))
    c_circ = 2*pi*radius
    return c_circ
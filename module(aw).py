#shapes.py
import math 
def area_circle(radius) : 
    return math.pi*radius*radius

def area_rectangle(length,width) : 
    return length*width

def area_triangle(base,height):
    return 0.5*base*height

#main.py
import shapes 
print("choose shape : ")
print("1.circle")
print("2.rectangle")
print("3.triangle")

choice = int(input("enter the choice(1-3):"))

if choice == 1 :
    r=float(input("enter radius : "))
    print("area of circle =",shapes.area_circle(r))

elif choice == 2 : 
    L=float(input("enter length:"))
    w=float(input("enter width: "))
    print("area of rectangle=",shapes.area_rectangle(L,w))

elif choice == 3 :
    b=float(input("enter base : "))
    h=float(input("enter height :"))
    print("area of triangle =",shapes.area_triangle(b,h))

else:
    print("invalid choice")
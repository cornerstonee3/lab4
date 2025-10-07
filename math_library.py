# import math
# #task 1
# x=int(input("Input degree: "))
# print(f"Output radian: {math.radians(x)}")
# #task 2
# def trap(h, a, b):
#     s=(a+b)/2*h
#     return s
# h=int(input("Enter height: "))
# a=int(input("Enter base 1: "))
# b=int(input("Enter base 2: "))
# print(f"Expected Output: {trap(h, a, b)}")
# #task 3
# def polygon(n, a):
#     s=(n*pow(a, 2))/(4*math.tan(math.pi/n))
#     return s
# n=int(input("Enter number of sides: "))
# a=int(input("Enter length of a side: "))
# res=int(polygon(n,a))
# print(f"The area of the polygon is: {res}")
# #task 4
def paral(b, h):
    s=b*h
    return s
b=int(input("Enter base: "))
h=int(input("Enter height: "))
print(f"Expected Output: {paral(b,h)}")

    
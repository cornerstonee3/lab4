# #task 1
# def sqr(N):
#     for i in range(1, N+1):
#         yield i**2
# N=int(input("Enter up to what number will we square numbers: "))
# for y in sqr(N):
#     print(y)
# #task 2
# def even(n):
#     for i in range(0, n+1):
#         if i==0:
#             continue
#         elif i%2==0:
#             yield i    
#         else:
#             continue
# n=int(input("Enter up to what number i show even numbers: "))
# for x in even(n):
#     print(x)
# #task 3
# def div(n):
#     for i in range(0, n+1):
#         if i==0:
#             continue
#         elif i%3==0 and i%4==0:
#             yield i   
#         else:
#             continue
# n=int(input("Enter up to what number i show what numbers are divisible by 3 and 4: "))
# for x in div(n):
#     print(x)  
# #task 4
# def squares(a, b):
#     for i in range(a, b+1):
#         yield i**2
# a=int(input("Enter from what number will we square numbers: "))
# b=int(input("Enter up to what number will we square numbers: "))
# for y in squares(a, b):
#     print(y)
def count(n):
    for i in range(n, -1, -1):
        yield i
n=int(input("Enter from what number will countdown: "))
for y in count(n):
    print(y)        



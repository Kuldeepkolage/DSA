n = int(input("Enter the number of rows: "))
for i in range(0,n):
    for j in range(n-i-1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    for l in range(n-i):
        print(" ",end="")    
    print()

    for i in range(0,n):
        for j in range(i):
            print(" ",end="")
        for k in range(2*n-(2*i+1)):
            print("*",end="")
        for l in range(i+1):
            print(" ",end="")    
        print()




# n = int(input("Enter the number of rows: "))
# for i in range(0,n):
#     for j in range(n-i-1):
#         print(" ",end="")
#     for k in range(2*i+1):
#         print("*",end="")   
#     for l in range(n-i-1):
#             print(" ",end="")   
#     print()

# for i in range(0,n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(2*n-(2*i+1)):
#         print("*",end="")
#     for l in range(i+1):
#         print(" ",end="")    
#     print()
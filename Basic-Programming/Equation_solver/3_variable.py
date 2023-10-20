print("Enter the respective values");

print("(a1) X + (b1) Y {c1}Z= d1")
print("(a2)X + (b2) Y {c2}Z = d2")
print("(a3)X + (b3) Y {c3}Z = d3")

a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))
d1 = int(input("Enter d1: "))

print(f"\n{a1}X + {b1}Y + {c1}Z  = {d1}\n")

a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: " ))
c2 = int(input("Enter c2: "))
d2 = int(input("Enter d2: "))

print(f"\n{a2}X + {b2}Y + {c2}Z  = {d2}\n")

a3 = int(input("Enter a3: "))
b3 = int(input("Enter b3: " ))
c3 = int(input("Enter c3: "))
d3 = int(input("Enter d3: "))

print(f"\n{a3}X + {b3}Y + {c3}Z  = {d3}\n")

det = (a1*b2*c3 + b1*c2*a3 + c1*a2*b3) - ( a3*b2*c1 + b3*c2*a1 + c3*a2*b1)

detX = (d1*b2*c3 + b1*c2*d3 + c1*d2*b3) - (d3*b2*c1 + b3*c2*d1 + c3*d2*b1)

detY = (a1*d2*c3 + d1*c2*a3 + c1*a2*d3) - (a3*d2*c1 + d3*c2*a1 + c3*a2*d1)

detZ = (a1*b2*d3 + b1*d2*a3 + d1*a2*b3) - ( a3*b2*d1 + b3*d2*a1 + d3*a2*b1)



print("---------------------")
try:
    X = detX/det
    Y = detY/det
    Z = detZ/det
    X = 0 if X == -0 else X #handling -0 situation for 0/-ve = -0
    Y = 0 if Y == -0 else Y
    Z = 0 if Z == -0 else Z
    # print(f"detX={detX} & detY = {detY} det={det}");
    print(f"X = {X}") 
    print(f"Y = {Y}") 
    print(f"Z = {Z}") 
   
except ZeroDivisionError:
   print("System does not have unique solution")



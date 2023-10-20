print("Enter the respective values");

print("(a1) X + (b1) Y = c1")
print("(a2)X + (b2) Y = c2")

a1 = int(input("Enter a1: "))
b1 = int(input("Enter b1: "))
c1 = int(input("Enter c1: "))

print(f"\n{a1}X + {b1}Y = {c1}\n")

a2 = int(input("Enter a2: "))
b2 = int(input("Enter b2: " ))
c2 = int(input("Enter c2: "))
print(f"\n{a2}X + {b2}Y = {c2}\n")

det = (a1*b2) - (a2*b1)

detX = (b2*c1) - (b1*c2)

detY = (b1*c2) - (b2*c1)

print("---------------------")
try:
    X = detX/det
    X = 0 if X == -0 else X #handling -0 situation for 0/-ve = -0
    # print(f"detX={detX} & detY = {detY} det={det}");
    Y = detY/det
    Y = 0 if Y == -0 else Y
    print(f"X = {X}") 
    print(f"Y = {Y}") 
    
except ZeroDivisionError:
   print("System does not have unique solution")

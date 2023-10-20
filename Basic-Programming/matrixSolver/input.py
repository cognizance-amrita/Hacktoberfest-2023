
x = input("Enter the order of matrix(e.g 2x3 3X4)")
x.lower();
row = int(x.split("x")[0])
column = int(x.split("x")[1])

print(row,column)
mat = list()
mrow = []
mcol = []
for i in range(column):
    for j in range(row):
        mrow.append(int(input(f"Enter mat[{i}][{j}]: ")))
    mat.append(mrow)
    mrow = []
print(mat);

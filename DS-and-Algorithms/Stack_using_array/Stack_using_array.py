# Implementing a stack using array
MAXSIZE = int(input("Maximum stack size : "))
stack = []

def push(num):
    """This function pushes given element num into stack"""
    if not isFull(): # Adds the element only if the stack does not exceed the size
        stack.append(num)
    else: 
        print("Stack overflow")
        
def peek():
    """This function prints the top most element of the stack"""
    if not isEmpty(): # If stack is not empty, it returns the top element
        print(stack[-1])
    else:
        print("Stack underflow")

def isEmpty():
    """This function returns boolean if stack is empty or not"""
    return True if len(stack) == 0 else False
    
def isFull():
    """This function returns a boolean if stack is full or has space"""
    return True if len(stack) == MAXSIZE else False

while True:
    try:
        # Asking the user what task he wants to perform
        opt = int(input("\n1. Push\n2. Peek\n3. isEmpty\n4. isFull\n5. Quit\n>>>"))
        if opt == 1:
            num = int(input("Enter number to push : "))
            push(num)
        elif opt == 2:
            peek()
        elif opt == 3:
            print(isEmpty())
        elif opt == 4:
            print(isFull())
        elif opt == 5:
            print("Thank you for using this program!")
            break
        else:
            print("Invalid option!")
    except ValueError:
        print("Invalid input!")        


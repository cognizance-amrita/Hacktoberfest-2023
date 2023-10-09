#INSERTION SORT
def insertion_sort(array_):
    for i in range(1, len(array_)):
        key=array_[i]
        j=i-1
        while j>=0 and key<array_[j]:
            array_[j+1]=array_[j]
            j-=1
        array_[j+1]=key

#input a list of numbers in the form as a list [a1,a2,a3,...,an]
#example input: [2,3,1,7,5,9,4]
list_of_numbers=eval(input("Input a list of numbers in the form of a list (eg: [4,2,1,5,6,3,8]) : "))
insertion_sort(list_of_numbers)
print("Sorted list after insertion sort:")
print(list_of_numbers)

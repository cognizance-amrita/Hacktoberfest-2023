#BUCKET SORT USING PYTHON
def bucket_sort (arr, bucket_size) :
    if len(arr) == 0:
        return arr
    minimum_ , maximum_ = min(arr) , max(arr)
    bucket_count = (maximum_ - minimum_) // bucket_size + 1
    buckets = [[] for _ in range (bucket_count)]

    for i in range (len(arr)) :
        index = (arr[i] - minimum_) // bucket_size
        buckets[index].append(arr[i])
    result = []

    for bucket in buckets:
        bucket.sort()
        result += bucket

    return result

#Give input in the form of an array
arr = eval(input("Input the array to be sorted in the form of a list"))
bucket_size = 10
sorted_arr = bucket_sort(arr, bucket_size)
print("Sorted array : ", sorted_arr)
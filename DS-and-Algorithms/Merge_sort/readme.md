Write Program for Merge sort in Python, C++, Java, and JavaScript

## Logic

```
MergeSort(array, left, right):
  if left < right
    middle = (left + right) / 2
    MergeSort(array, left, middle)
    MergeSort(array, middle + 1, right)
    Merge(array, left, middle, right)
end MergeSort

```

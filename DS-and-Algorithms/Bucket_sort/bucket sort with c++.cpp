#include <iostream>


void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}


void bucketSort(int arr[], int n, int bucketCount) {
    int maxVal = arr[0];
    int minVal = arr[0];


    for (int i = 1; i < n; i++) {
        if (arr[i] > maxVal) {
            maxVal = arr[i];
        }
        if (arr[i] < minVal) {
            minVal = arr[i];
        }
    }


    double range = (double)(maxVal - minVal + 1) / bucketCount;


    int* buckets = new int[bucketCount];
    int** bucketElements = new int*[bucketCount];


    for (int i = 0; i < bucketCount; i++) {
        buckets[i] = 0;
        bucketElements[i] = new int[n];
    }

 
    for (int i = 0; i < n; i++) {
        int index = (int)((arr[i] - minVal) / range);
        bucketElements[index][buckets[index]++] = arr[i];
    }

    // Sort each bucket using insertion sort
    int index = 0;
    for (int i = 0; i < bucketCount; i++) {
        insertionSort(bucketElements[i], buckets[i]);
        for (int j = 0; j < buckets[i]; j++) {
            arr[index++] = bucketElements[i][j];
        }
    }


    for (int i = 0; i < bucketCount; i++) {
        delete[] bucketElements[i];
    }
    delete[] bucketElements;
    delete[] buckets;
}

int main() {
    int n, bucketCount;

    std::cout << "Enter the number of elements: ";
    std::cin >> n;

    std::cout << "Enter the number of buckets: ";
    std::cin >> bucketCount;

    int* arr = new int[n];

    std::cout << "Enter the elements: ";
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    bucketSort(arr, n, bucketCount);

    std::cout << "Sorted array: ";
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;

    delete[] arr;

    return 0;
}
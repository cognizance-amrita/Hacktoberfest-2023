#include <iostream>
using namespace std;
void insertion_sort(int arr[], int n){
    for (int i=1;i<n;++i){
        int key=arr[i];
        int j=i-1;
        while (j>=0 && key<arr[j]){
            arr[j+1]=arr[j];
            j-=1;
        }
        arr[j+1]=key;
    }
}

int main() {
    int array_length;
    cout<<"Enter the number of elements in array: ";
    cin>>array_length;
    int arr[array_length];
    cout<<"Enter the elements:\n";
    for (int i=0;i<array_length;++i) {
        cout<<"Enter element "<<i+1<<": ";
        cin>>arr[i];
    }
    
    insertion_sort(arr,array_length);
    
    cout<<"Sorted array:\n";
    for (int i=0;i<array_length;++i)
        cout<<arr[i]<<" ";
    return 0;
}
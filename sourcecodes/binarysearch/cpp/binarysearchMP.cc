#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
using namespace std;

class ParameterError {
};

class searched {
    public:
        int greater;
        int smaller;
        int index;
        int num;
        
};

searched binarysearch(int array[], int size, int target) 
{
    searched rv;  // return value
    sort(array, array+size);
    int l = 0;
    int mid = 0;
    int l2 = 0;
    int mid2 = 0;
    int h = size-1; 
    int h2 = size-1;
    int HI = size-1;
    while (l+1 != h) {
        mid = (l + h)/2;
        mid2 = (l2 + h2)/2;
        if (array[mid] < target) {
            l = mid;
        } else {
            h = mid;
        }
        if (array[mid2] <= target) {
            l2 = mid2;
        } else {
            h2 = mid2;
        }
    }
    if (array[h] != target) {
        rv.index = false;
    } else {
        rv.index = h;   
    }
    rv.num = (l2 - h) + 1; //calculate instances of same number
    rv.greater = HI - l2; //amount of numbers greater than target
    
    rv.smaller = h;
    return rv;
}
int main()
{
    ios_base::sync_with_stdio(false);
    int size;
    cout << "Enter the size of the array" << "\n";
    cin >> size;
    int arr[size];
    int target;
    int number;
    for (int i = 0; i < size; i++) {
        cout << "Enter the number in index " << i << "\n";
        cin >> number;
    }
    cout << "Enter the number you want to find:" << "\n";
    cin >> target;
    searched rv = binarysearch(arr, size, target);
}

#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int binarysearch(int array[], int size, int target) 
{
    searched rv;  // return value
    sort(array, array+size);
    int l = 0;
    int mid = 0;
    int h = size-1; 
    while (l+1 != h) {
        mid = (l + h)/2;
        if (array[mid] < target) {
            l = mid;
        } else {
            h = mid;
        }
    }
    if (array[h] != target) {
        return -1;
    } else {
        return h; 
    }
}

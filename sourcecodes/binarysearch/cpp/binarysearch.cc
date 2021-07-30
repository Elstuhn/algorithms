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

searched binarysearch(int array[], int target) 
{
    int n = sizeof(array) / sizeof(array[0]);
    cout << "the size of n is " << n << "\n";
    if (n == 0) {
        throw ParameterError();
    } 
    searched rv;  // return value
    sort(array, array+n);
    for (int i = 0;i<n;i++) {
        cout << array[i] << "\n";
    }
    int l = 0;
    int mid = 0;
    int l2 = 0;
    int mid2 = 0;
    int h = n-1; 
    int h2 = n-1;
    int HI = n-1;
    while (l+1 != h) {
        mid = (l+h)/2;
        mid2 = (l2+h2)/2;
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
    rv.num = (l2-h)+1; //calculate instances of same number
    rv.greater = HI-l2; //amount of numbers greater than target
    
    rv.smaller = h;
    return rv;
}
int main()
{
    ios_base::sync_with_stdio(false);
    int test[7] = {1, 5, 2, 3, 7, 7, 2};
    searched rv = binarysearch(test, 5);
    cout << "ended" << "\n";
    cout << rv.index << "\n";
    cout << "outted index" << "\n";
    cout << rv.num;
}

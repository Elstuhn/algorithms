# Python Program for Trapping Rain Water Problem

* Introduction To Problem :-<br>
	Here, in this problem we will discuss one of the famous problem of DSA i.e., Trapping Rain Water in Python .
	We are given with n non-negative integers representing an elevation map where the width of each bar is 1,
	we need to compute how much water it is able to trap after raining.
	
* Example :
	* Input : arr = [2,0,3,0,2,0,4]
	* Output : 9
	*	Explanation : We can trap “2 units” of water between 2 and 3, “7 units” between 3 and 4 (“3 units” between 3 and 2 , 
	*	“1 unit” on top of bar 2 and “3 units” between 2 and 4.

* Algorithm :
	* Start
	* Initialize three variables with value zero named as ans, temp, prev
	* Iterate entire array using variable i
	* if arr[i] is greater then prev and temp is zero then assign the value or arr[i] to prev
	* else if arr[i] is greater then or equals to prev then add temp to ans, assign arr[i] to prev and temp to zero
	* else check if arr[i] is not the last element of arr and arr[i] is less then maximum of arr[i+1 : ] then assign difference of prev and arr[i] to temp else add arr[i to ans, assign temp to zero and prev to arr[i]
	* Print value of answer.

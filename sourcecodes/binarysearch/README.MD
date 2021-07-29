# What is BinarySearch?
###### Binary search, also known as half-interval search, logarithmic search, or binary chop is an algorithm that finds the position of a target value within a sorted array. 

# How does it work?
###### Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found. If the search ends with the remaining half being empty, the target is not in the array.

# What is the time complexity of it?
###### The average time complexity is O(log n) with the best being O(1) and the worst being O(n) where n is the number of elements in the array.

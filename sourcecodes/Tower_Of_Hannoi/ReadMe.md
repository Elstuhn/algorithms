# Problem Approach
* Create a tower_of_hanoi recursive function and pass two arguments: the number of disks n and the name of the rods such as source, aux, and target.
* We can define the base case when the number of disks is 1. In this case, simply move the one disk from the source to target and return.
* Now, move remaining n-1 disks from source to auxiliary using the target as the auxiliary.
* Then, the remaining 1 disk move on the source to target.
* Move the n-1 disks on the auxiliary to the target using the source as the auxiliary.

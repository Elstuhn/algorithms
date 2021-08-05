# Tortoise And Hare Algorithm

## Background
###### Also known as Cycle Detection or Cycle Finding, this algorithm was made by Robert W. Floyd for finding a cycle/loop in a sequence of iterated function values.

## How It Works
###### Two pointers, the tortoisee and the hare is placed at the start of the sequence, the tortoise travels x nodes and the hare travels 2x nodes every iteration until they both land on the same node. Then, the hare is placed back at the start of the sequence and both pointers keep moving one node until they meet again. The node that they are on at the end is the start of the cycle. 

## Time and Space Complexity
###### This algorithm takes O(1) space and has a time complexity of O(n)

import random
import typing as t

class search:
    def __init__(self, array, target):
        self.array = array
        self.target = target
        self.index = 0 #the index of first instance of target
        self.l = 0 #amount of targets in array
    
    def __len__(self):
        return self.l

Number = t.Union[int, float]
def binarysearch(array : list[Number], target : Number):
    array.sort()
    rv = search(array, target) #return value
    if not array:
        raise ValueError("List cannot be empty")
    elif not isinstance(target, (int, float)):
        raise ValueError("Target has to be either of type int or float")
    elif array[0] == target:
        rv.index = 0
        rv.l = 0
        for i in array:
            if i != target: break
            else: rv.l += 1
        rv.lesser = 0
        rv.greater = len(array) - rv.l
        return rv
        
    h = h2 = HI = len(array) - 1 #the highest index of the array 
    l = mid = l2 = mid2 = 0 #l = lowest (index)
    while l+1 != h:
        mid = (h+l) // 2
        mid2 = (h2+l2) // 2
        if array[mid] < target:
            l = mid
        else:
            h = mid
        if array[mid2] <= target:
            l2 = mid2
        else:
            h2 = mid2
            
    if array[h] != target:
        rv.index = False 
    else:
        rv.index = h #index of first instance of target
    rv.l = (l2-h)+1 #calculate instances of same number
    if (rv.l == 0 and rv.index):
        rv.l = 1
        
    rv.greater = HI - l2 #amount of numbers greater than target
    
    rv.lesser = h  #amount of numbers lesser than target
    
    return rv
         
     

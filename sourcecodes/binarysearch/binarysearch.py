import random
import typing

class ParameterError(Exception):
    pass

def binarysearch(array : list, target): #target int or float
    if not array:
        raise ParameterError("List cannot be empty")
    elif not (type(target) == int or type(target) == float):
        raise ParameterError("Target has to be either of type int or float")
    elif array[0] == target:
        rv.index = 0
        rv.l = 0
        for i in array:
            if i != target: break
            else: rv.l += 1
        
    rv = search(array, target) #return value
    array.sort()
    h = h2 = HI = len(array)-1 #the highest index of the array 
    l = mid = l2 = mid2 =0 #l = lowest (index)
    while l+1 != h:
        mid = (h+l)//2
        mid2 = (h2+l2)//2
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
    rv.greater = HI-l2 #amount of numbers greater than target
    
    rv.lesser = h  #amount of numbers lesser than target
    
            

class search:
    def __init__(self, array, target):
        self.array = array
        self.target = target
        self.index = 0 #the index of first instance of target
        self.l = 0 #amount of targets in array
    
    def __len__(self):
        return self.l
    
     

import typing as t

Number = t.Union[int, float]
def binarysearch(array : list[Number], target : Number):
    array.sort()
    if not array:
        raise ValueError("List cannot be empty")
    elif not isinstance(target, (int, float)):
        raise ValueError("Target has to be either of type int or float")
        
    h = len(array) - 1 #the highest index of the array 
    l = mid = 0 #l = lowest (index)
    while l+1 != h:
        mid = (h+l) // 2
        if array[mid] < target:
            l = mid
        else:
            h = mid
            
    if array[h] != target:
        return False 
    else:
        return h #index of first instance of target

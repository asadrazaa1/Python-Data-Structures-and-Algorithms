
def binary_search(data, target, low, high):
    """Return True if target is found is indicated portion of a python list
    
    The search only considers the portion from data[low] to data[high] inclusive
    """
    if low > high:
        return False                                # interval is empty, no match found
    else:                       
        mid = (low + high) // 2                 
        if target == data[mid]:
            return True                             # found a match
        elif target < data[mid]:
            # recur on the portion left of the middle
            return binary_search(data, target, low, mid-1)
        else:
            # recur on the portion right of the middle
            return binary_search(data, target, mid+1, high)

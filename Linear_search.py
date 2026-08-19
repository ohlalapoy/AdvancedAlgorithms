def linear_search(list,target):
    """
    Big O : O(log n)
    Notes : Return in Python in the failue case can be different in
    the implementations so we can use return -1 (No value) or return None can be used.

    Returns the index position of the target if found, else returns None
    """

    for i in range(0,len(list)): # for the number between 0 to length of list
        if list[i] == target: # to check that number in the range above match the target that we are looking for
            return i    # if number match to target return this number to me and terminiate the function
    return None # In case if you cannot meet the number which meet the target, return None and terminate


def verify(index):
    if index is not None:
        print("Target found at the Index: ",index)
    else:
        print("Target not found in the list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 6)
verify(result)

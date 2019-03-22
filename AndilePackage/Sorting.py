def merge_sort(x):
    """
    Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or 
    has one item, it is sorted by definition (the base case). If the list has more than one item, 
    we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, 
    the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller 
    sorted lists and combining them together into a single, sorted, new list.  
    """

    
    #function should return what was input if the list is only one number long
    if len(x) == 1:
        return x
    
    #function should take the list and split it in half and begin sorting according to index
    else:
        mid = int(len(x) / 2)
        left = merge_sort(x[:mid])
        right = merge_sort(x[mid:])
    
        """
        The result of the merge will give us a list that is sorted in the below result = 0
        This is though a holding or staging area which is empty because we are sorting still
        """
    result = []
    
    """
    The split is indexed using i&j and we will sort through this list where i is the first 
    index on the left half where j is the first index on the right half and we start at 0
    """
    i = j = 0
        
    #the sorting that runs in the background with a while loop based on the above split
    while i < len(left) and j < len(right):
        #if the left side index element(i) is smaller than the right (j) then we add the i index
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        #or else the right side index element(i) is smaller than the right (j) then we add the i index
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result



def bubble_sort(items):
    """
    This is bubble sort algorithm. The bubble sort makes multiple passes through a list. 
    It compares adjacent items and exchanges those that are out of order. Each pass 
    through the list places the next largest value in its proper place. 
    """

    for i in range (0, len(items) - 1):
        for j in range(0, len(items) -1 -i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                
                #Return array of items, sorted in ascending order

    return items



def quick_sort(items):
    """
This is a quick sort function which first selects a value, which is called the pivot value.
This quicksort algorithm makes use of recurssion and has the Hoare partition scheme
which helps in the way of selecting the pivot. This is beneficial for performance and 
can be researched further using this url: https://en.wikipedia.org/wiki/Quicksort
"""

    #So we split this list by using a fuction within a function
    def _quicksort(items, low, high):
        # must run partition on sections with 2 elements or more
        if low < high: 
            p = partition(items, low, high)
            _quicksort(items, low, p)
            _quicksort(items, p+1, high)
            
    def partition(items, low, high):
        pivot = items[low]
        while True:
            while items[low] < pivot:
                low += 1
            while items[high] > pivot:
                high -= 1
            if low >= high:
                return high
            items[low], items[high] = items[high], items[low]
            low += 1
            high -= 1
    _quicksort(items, 0, len(items)-1)
    return items






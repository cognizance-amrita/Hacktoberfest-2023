# Merge sort

def merge_sort(array):
    """This function takes an array as an argument and sorts using merge sort in place"""
    if len(array) > 1: # Merge sort step 1 : It divides the array until its size is 1
        mid = len(array) // 2
        left_array = array[:mid]
        right_array = array[mid:]
        
        merge_sort(left_array)
        merge_sort(right_array)
        
        # Merge sort step 2 : Merging the elements into the sorted array in sorted order
        l_ind = r_ind = s_ind = 0 # left index, right index and sort index initialized to 0
        
        while l_ind < len(left_array) and r_ind < len(right_array): # It checks the left most element of both halves
            # If leftmost of left array smaller than leftmost of right, adding leftmost to the array in place
            if left_array[l_ind] < right_array[r_ind]: 
                array[s_ind] = left_array[l_ind]
                l_ind += 1
            # Else, adding leftmost of right array
            else:
                array[s_ind] = right_array[r_ind]
                r_ind += 1
            s_ind += 1
            
        while l_ind < len(left_array): # If there remains more elements without merging in left array adding them
            array[s_ind] = left_array[l_ind]
            l_ind += 1
            s_ind += 1
            
        while r_ind < len(right_array): # If there remains more elements withoug merging in right array adding them
            array[s_ind] = right_array[r_ind]
            r_ind += 1
            s_ind += 1
    
def maxandmin(list1):
    # Handle empty input
    if len(list1)==0:
       return None
    # Initialize both values with the first element
    largest =list1[0]
    smallest=list1[0]

     # Traverse every element in the array
    for i in list1:
        
        # Update largest if current element is greater
        if i>largest:
            largest=i

        # Update smallest if current element is smaller
        if i<smallest:
            smallest=i

    return f"the largest is {largest} and the smallest is {smallest}"

# Example execution
print(maxandmin([10, 5, 30, 2, 50]))
"""
    Problem:
        Find the maximum and minimum elements in an array.

    Approach:
        Use a single traversal to find both values.

    Algorithm:
        1. Check whether the input array is empty.
        2. Initialize largest and smallest with the first element.
        3. Traverse the array using a for loop.
        4. If the current element is greater than largest,
           update largest.
        5. If the current element is smaller than smallest,
           update smallest.
        6. Return both values.

    Time Complexity:
        O(n) - Every element is visited exactly once.

    Space Complexity:
        O(1) - Only two variables are used for tracking.
        No additional data structure is created.

    Example:
        Input:  [10, 5, 30, 2, 50]
        Output: Largest = 50, Smallest = 2
        """

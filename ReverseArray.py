def reverse_array(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    start=0
    print(len(nums))
    end = len(nums)-1
    while start < end:

        #swap elements
        nums[start], nums[end]= nums[end], nums[start]
        start +=1
        end -=1

    return nums

a={1,2,3,4}
print(reverse_array(a))
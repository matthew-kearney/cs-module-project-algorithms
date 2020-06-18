'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # Understand the problem:
    # An array of numbers where every each of one appears twice except of one that it appears only once.
    # Input = array =[3 2 5 2 5 3 1]
    # Output = 1
    
    # An array of numbers where every each of one appears twice except of one that it appears only once.
    not_duplicate_list = []
    nums = arr
     # for every number in numbers:
    for number in nums:# loop through numbers array
        if number in not_duplicate_list:# remove any duplicate number
            not_duplicate_list.remove(number)
        else:
            not_duplicate_list.append(number)# otherwise add the number to the list
    return not_duplicate_list.pop()
    
    
    # notes from lecture
    s = set()
    # use either a dic or a set
    # sets hold onto unique elements
    # loop thru array
    for x in arr:
        # for ech element 
        # check if its already in our set
        # if it is then that not our out element out
        if x in s:
            # remove the element from our set
            s.remove(x)
        else:
            s.add(x)
    # the odd element out will be the only element in the set
    return list (s)[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
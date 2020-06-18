'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # we need to move all the zeroes to the end of our list
    # loop through the list, if a the number is 0 
    # put the zero at the end of the list 
    # do this until all zeroes goes to the end of the list
    
    
    # if count = 0 non zero numbers
    count = arr.count(0)
    # for every i in range of count
    for i in range(count):
        # add the 0 to the arr
        arr.append(0)
        # or remove 0 from the array
        arr.remove(0)
    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
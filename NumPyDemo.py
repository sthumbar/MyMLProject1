import numpy as np
# create 1 d array
arr_1d = np.array([109,204,504,45])
print(arr_1d)
print(type(arr_1d))
print(arr_1d.ndim)
print("size of 1d array == ",arr_1d.size)
# shape attribute return for each dimension how many elements in that dimensions
print("shape is " ,arr_1d.shape)  # how many elements are alone dimension

# create a 2 d array
arr_2d = np.array([[109,204,504,90],[9,5,7,70],[98,51,72,56]])
print(arr_2d)
print(type(arr_2d))
print(arr_2d.ndim)
print("size of 2d array == ",arr_2d.size)
# shape attribute return for each dimension how many elements in that dimensions
print(arr_2d.shape)  # how many elements are alone dimension

# reshape can be of same matrix size row*columns
arr_2d_reshape1 = arr_2d.reshape(2,6)
print(arr_2d_reshape1)

arr_2d_reshape2 = arr_2d.reshape(4,3)
print(arr_2d_reshape2)

arr_2d_reshape3 = arr_2d.reshape(1,12)
print(arr_2d_reshape3)


# magic number -1 , if we dont know what reshape values we can keep , numpy automatically reshapes to

arr_2d_reshape4 = arr_2d.reshape(4,-1)
print("reshape with -1", arr_2d_reshape4)


# indexing retirive single element, slicing retrives range of elements

# create a 1 d arry

account_length = np.array([1,2,3,4])
print(account_length)
print(account_length[0])
print(account_length[3])
# last element is retrived by -1
print(" last element is retrived   by -1 ",account_length[-1])
print(account_length[::])

print(account_length[1:2])

print("get even index numbers == " ,account_length[:: 2])

# reverse element is retrived by -1

print("reverse numbers == " ,account_length[:: -1])

# get element based on the condition
filter = (account_length >1) & (account_length <4)
print(account_length[filter])

arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

'''
[[1,2,3,4],
[5,6,7,8],
[9,10,11,12]]
'''
print(arr_2d[0,0])
print(arr_2d[2,3])
# last row and last column
print(arr_2d[-1,-1])

# get 2 nd row
print(arr_2d[1,:]) # this is preferrred
print(arr_2d[1,0:4])

# get 2 column
print(arr_2d[:,1])

# get sub matrix

print(arr_2d[1:,2:])

B = arr_2d[1:,2:]
B[0,0] = 77
print(B)
print(arr_2d) # original array changes, bcoz B is view of array 2d

# if we dont want to change the original 2d array


arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# get 2 column
print(arr_2d[:,1])

# get sub matrix

print(arr_2d[1:,2:])

B = arr_2d[1:,2:].copy()
B[0,0] = 99
print(B)
print(arr_2d) # original array changes, bcoz B is view of array 2d

# return odd number of arr_2d
filter = (arr_2d %2 !=0)
print(arr_2d[filter])

# return even number of arr_2d
filter = (arr_2d %2 ==0)
print(arr_2d[filter])




# add ten function

arr_2d = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
def add_ten(input_arr):
    # create a new array same shape a s input_arr and uninitialized values
    output_arr = np.empty_like(input_arr)
    # its shape is tuple with number rows and number of columns so we get the length by that
    for row_idx in range(input_arr.shape[0]):
        for col_ind in range(input_arr.shape[1]):
            output_arr[row_idx][col_ind] = input_arr[row_idx][col_ind] +10

    print("\n  after chaning the values to 10 o 2d output_arr is ==  ")
    print(output_arr)

print("\noriginal 2d array")
add_ten(arr_2d)

#-------------------
# broadcasting
print("after broadcasting")
print(arr_2d+100)
print("orginal array after  broadcasting")
print(arr_2d)


# multipley 1d array with 2d arry
arr1d = np.array([1,10,100,1000])
print(arr_2d*arr1d)


# divide 2d array by 2d arry
print("after division")
arr_2d_2 = np.array([[1],[2],[3]])
print(arr_2d/arr_2d_2)


# add 2d array by 2d arry
print("after addition")
arr_2d_3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(arr_2d+arr_2d_3)


print(np.diagonal(arr_2d))
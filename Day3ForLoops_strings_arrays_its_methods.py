for i in range(5):
    print(i)

# increment by 2
print("increment by  2")
for i in range(1, 10, 2):
    print(i)

# decrement 
print("decrement 5 till 1 by 2")
for i in range(5, 1, -2):
    print(i)    
    
print(5/2)
print(5// 2)


arr = [1, 2, 3, 4]
print(arr)

# arrays in py are dynamic by defautl... so it van be used as stack
arr.append(5)

arr.append(7)
print(arr)
arr.pop()
print(arr)


arr.insert(1, 6) # O(n) operation for inserting....
print(arr)

arr[1] = 3
arr[0] = 2

print(arr)


# initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

# last element
arr = [1, 2, 3]
print(arr[-1])

#similar to for-loop ranges, last index is
# non - inclusidve
# sublist (aka slicing)
print(arr[1:10])  # excluding the element at 10 index and also it doesn't throw out of bound exception.


#unpacking
# carefull the left variables should be equal to elements of the array.
a, b, c = [1, 3, 4]
print (a, b, c)

nums = [1, 2, 3, 4]

# using index
for i in range(len(nums)):
    print(nums[i])

# withou index
for i in nums:
    print(i)  # no need of range.. just i/n/x anything in nums...

# need both index and value in same loop... use first range for loop or enumerate..

# first is index and seciond is value
for i, n in enumerate(nums):
    print(i, n)

# loop thrugh multiple arrays simultaneously..
# # with unpacking

num1 = [1, 3, 5, 7]
num2 = [2, 4, 6, 8]

for n1, n2 in zip(num1, num2):
    print(n1, n2)

# reversing an array...
num1.reverse()
print(num1)

# sorting...
num1.sort()
print(num1)
num1.sort(reverse=True)
print(num1)
arr = ["bob", "alic","zam", "sam", "pam"]
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)

arr.sort()
print(arr)



# sort based on length .. lambda ... its also alphabetical sort.
arr.sort(key=lambda x:len(x))
print(arr)

# List comprehension...
arr = [i for i in range(5)]
print(arr)

arr = [i+i for i in range(5)]
print(arr)

# 2 D list
nums = [[0] * 4 for i in range(4)]
print(nums)

# but this is not same as creting 2D array like this... as they all are copy of each other and modifying any sub arr will modify the others.
nums2 = [[0]*4] * 4
print(nums2)


# String are similar to arrays
s = "abc"
print(s[0:2])

#but they are immutable.
# cannot be modified at any index 
# but can update the string by appeding toher string to it.. which will create a new string
s += "def"
print(s)

# string can be converted to integers and integers can also be converted to string.. ex

print(int("123") + int("123")) # addition integers 

print(str("1243")+str("1234")) # append

# ASCII value of a char ord()
print(ord("a"))
print(ord("A"))
print(ord("b"))

# combine a list of strings (with an emptystring #delimitor)
str = ["ab", "cd", "ef"]
print("".join(str))
print(" ".join(str))
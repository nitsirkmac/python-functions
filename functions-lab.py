# Challenge 1
def sum_to(n):
    return (n * (n+1) // 2)

"""print(sum_to(6))
print(sum_to(10))"""




# Challenge 2
# Write a function named largestthat takes a list of numbers as an argument and returns the largest number in that list.
"""
def largest(nums):
    lg_num = nums[0]
    for n in nums:
        if n > lg_num:
            lg_num = n
    return("The largest number is:", lg_num)

print(largest([1,2,3,4,0]))
print(largest([10, 90, 55, 32]))
"""


# Challenge 3
# Write a function named occurancesthat takes two string arguments as input and counts the number of occurances of the second string inside the first string.
"""
def occurances(string, ocs):
    count = string.count(ocs)
    return(count)


print(occurances('fleep floop', 'e'))   # returns 2
print(occurances('fleep floop', 'p'))  # returns 2
print(occurances('fleep floop', 'ee'))  # returns 1
print(occurances('fleep floop', 'fe'))  # returns 0
"""

# Challenge 4
# Write a function named productthat takes an arbitrary number of numbers, multiplies them all together, and returns the product
"""
def product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))
"""
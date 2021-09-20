# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 22:50:21 2021

@author: Yauheny_Shaludzko
"""
from random import randint  # randint from random module is imported in order to generate random numbers

# Create list of 100 random numbers from 0 to 1000
''' For list creature is used generator. 
    for loop is used in order to generate 100 numbers.
    randint(0, 1000) is used for generation of random number from 0 to 1000 '''
num_list = [randint(0, 1000) for i in range(100)]
print("unsorted list:", num_list)  # Result output printing

'''As sorting algorithm MergeSort was chosen
   I found it more clear to understand than QuickSort & TimSort
   Also it much more effective than BubbleSort & InsertionSort'''


def merge(left, right):  # creating merge function
    if len(left) == 0:  # If the first array is empty
        return right  # than we can return the second array as the result

    if len(right) == 0:  # If the second array is empty
        return left  # than we can return the first array as the result
    result = []  # blank list for the resulting array creating
    index_left = index_right = 0  # setting nulls to indexes

    # Now go through both arrays until all the elements
    # make it into the resultant array

    while len(result) < len(left) + len(right):  # while loop creation
        if left[index_left] <= right[index_right]:  # if condition
            result.append(left[index_left])  # then append left element to the resulting array
            index_left += 1  # left index increasing on 1
        else:
            result.append(right[index_right])  # else append right element to the resulting array
            index_right += 1  # right index increasing on 1

        if index_right == len(right):  # If the end of either array reached, then we can
            result += left[index_left:]  # add the remaining elements from the other array to result
            break  # and break the loop

        if index_left == len(left):  # If the end of either array reached, then we can
            result += right[index_right:]  # add the remaining elements from the other array to result
            break  # and break the loop

    return result  # returning resulting array


def merge_sort(array):  # merge_sort function creation

    if len(array) < 2:  # If the input array contains fewer than two elements,
        return array  # then return it as the result of the function

    midpoint = len(array) // 2  # midpoint index defining
    ''' Sort the array by recursively splitting the input

    into two equal halves, sorting each half and merging them

    together into the final result'''

    return merge(  # merging result returning

        left=merge_sort(array[:midpoint]),  # left array defining

        right=merge_sort(array[midpoint:]))  # right array defining


print("sorted_list:", merge_sort(num_list))  # printing output result as 'sorted_list'

# creating empty lists for even and odd numbers
oddnum = []
evennum = []

# for each number in sorted list check if remainder of the division into 2 equals zero or not (it means that number even or add)
for i in num_list:
    # if remainder is 0...
    if i % 2 == 0:
        # then number is even and we add it to the list of even numbers
        evennum.append(i)
    # if reminder is not 0, then it is odd, and we add it to the list of odd numbers
    else: oddnum.append(i)

# print two lists of even and odd numbers
print("Even nums list:\n", evennum)
print("Odd nums list:\n", oddnum)

# counting average
# creating function which counts average for elements in list in parameter
def avg_count(any_list):
    # variable for sum of elements of list
    sum = 0
    # for each element of list we add this element to variable
    for i in any_list:
        sum = sum + i
    # then count average by dividing this sum to length of list and returning this value from function
    return sum / len(any_list)

# calling function of calculating average for lists with even and odd numbers separately and print average to console
print("Average for even nums:", avg_count(evennum))
print("Average for odd nums:", avg_count(oddnum))

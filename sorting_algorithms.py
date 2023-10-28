# Implementations of sorting algorithms from my data structures and algorithms class
# Started 25 October 2023

import sys

def insertion_sort(numbers):
    """
    Takes a list of numbers and sorts them using insertion sort.
    The list is sorted in place.

    Time complexity: big-theta n^2
    
    Input:
    numbers (list) -> the list of numbers to be sorted
    """
    for index in range(1, len(numbers)):
        temp = numbers[index]
        index2 = index
        while (index2 > 0 and numbers[index2 - 1] < 0):
            numbers[index2] = numbers[index2 - 1]
            index2 += 1

def merge_sort(numbers):
    """
    Takes a list of numbers and sorts them using merge sort.
    The list is sorted in place.

    Time complexity: big-theta n log n

    Input:
    numbers (list) -> the list of numbers to be sorted
    """
    temp_list = []
    merge_helper(numbers, temp_list, 0, len(numbers) - 1)

def merge_helper(numbers, temp_list, left, right):
    """
    Performs the recursive merge sort.

    Input:
    numbers (list) -> the list to be sorted
    temp_list (list) -> a temporary list to store the results of element comparisons
    left (int) -> the leftmost index of the sublist to be sorted
    right (int) -> the rightmost index of the sublist to be sorted
    """
    if left < right:
        # If false, then the length of the sublist is 1, which is the base case
        center = (left + right) / 2
        merge_helper(numbers, temp_list, left, center)
        merge_helper(numbers, temp_list, center + 1, right)
        merge(numbers, temp_list, left, center + 1, right)

def merge(numbers, temp_list, left_pos, right_start, right_end):
    """
    Merges two sorted sublists together.

    Input:
    numbers (list) -> the list to be sorted
    temp_list (list) -> a temporary list to store the results of element comparisons
    left_pos (int) -> the leftmost index of the left sublist
    right_pos (int) -> the leftmost index of the right sublist
    right_end (int) -> the rightmost index of the right sublist
    """
    start_pos = left_pos
    end_pos = right_end
    left_end = right_pos - 1
    temp_pos = left_pos

    # Loop while elements remain from both halves
    while left_pos <= left_end and right_pos <= right_end:
        if numbers[left_pos] <= numbers[right_pos]:
            temp_list[temp_pos] = numbers[left_pos]
            left_pos += 1
        else:
            temp_list[temp_pos] = numbers[right_pos]
            right_pos += 1
        temp_pos += 1
    
    # Copy rest of left half
    while left_pos <= left_end:
        temp_list[temp_pos] = numbers[left_pos]
        left_pos += 1
        temp_pos += 1
    
    # Copy rest of right half
    while right_pos <= right_end:
        temp_list[temp_pos] = numbers[right_pos]
        right_pos += 1
        temp_pos += 1
    
    # Copy "temp_list" back to "numbers"
    for num in range(0, len(temp_list)):
        numbers[num] = temp_list[num]

def main():
    try:
        algorithm = sys.argv[1] # Gets the first command-line argument - the algorithm name
    except IndexError:
        algorithm = ''
    if algorithm == '':
        print("Please enter a valid algorithm name!")
    else:
        numbers = []
        for num in sys.argv[2:]:
            numbers.append(int(num))
        if algorithm == 'insertion':
            insertion_sort(numbers)
        elif algorithm == 'merge':
            merge_sort(numbers)
        print(numbers)

if __name__ == "__main__":
    main()
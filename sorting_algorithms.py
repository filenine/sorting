# Implementations of sorting algorithms from my data structures and algorithms class
# Started 25 October 2023

import sys

def insertion_sort(numbers):
    """
    Takes a list of numbers and sorts them using insertion sort.
    The list is sorted in place.
    
    Input:
    numbers -> a list of numbers
    """
    for index in range(1, len(numbers)):
        temp = numbers[index]
        index2 = index
        while (index2 > 0 and numbers[index2 - 1] < 0):
            numbers[index2] = numbers[index2 - 1]
            index2 += 1

def main():
    try:
        algorithm = sys.argv[1] # Gets the first command-line argument - the algorithm name
    except ValueError:
        algorithm = ''
    if algorithm == '':
        print("Please enter a valid algorithm name!")
    else:
        numbers = []
        for num in sys.argv[2:]:
            numbers.append(int(num))
        if algorithm == 'insertion':
            insertion_sort(numbers)
        print(numbers)

if __name__ == "__main__":
    main()
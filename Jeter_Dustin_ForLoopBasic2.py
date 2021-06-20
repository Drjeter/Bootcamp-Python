# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def Biggie(list):
    for number in range(len(list)):
        if list[number] > 0:
            list[number] = "big"
    return list
x = Biggie([-1, 3, 5, -5])
print(x)

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of 
# positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def Positives(list):
    positives = 0
    for number in range(len(list)):
        if list[number] > 0:
            positives += 1
    list[len(list) - 1] = positives
    return list
x = Positives([-1, 1, 1, 1])
y = Positives([1, 6, -4, -2, -7, -2])
print(x)
print(y)

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def Sum(list):
    sum = 0
    for number in list:
        sum += number
    return sum
x = Sum([1,2,3,4])
y = Sum([6,3,-2])
print(x)
print(y)

# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def Average(list):
    sum = 0
    for number in list:
        sum += number
    average = sum / len(list)
    return average
x = Average([1, 2, 3, 4])
print(x)

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def Length(list):
    length = 0
    for item in list:
        length += 1
    return length
x = Length([37, 2, 1, -9])
y = Length([])
print(x)
print(y)

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. 
# If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def Minimum(list):
    if len(list) == 0:
        return False
    else:
        minimum = list[0]
        for number in list:
            if number < minimum:
                minimum = number
        return minimum
print(Minimum([37,2,1,-9]))
print(Minimum([]))


# Maximum - Create a function that takes a list and returns the maximum value in the array. 
# If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def Maximum(list):
    if len(list) == 0:
        return False
    else:
        maximum = list[0]
        for number in list:
            if number > maximum:
                maximum = number
        return maximum
print(Maximum([37,2,1,-9]))
print(Maximum([]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary 
# that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return 
# {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def Analysis(list):
    sum = 0
    length = 0
    minimum = list[0]
    maximum = list[0]
    for number in list:
        sum += number
        length += 1
        if number < minimum:
            minimum = number
        elif number > maximum:
            maximum = number
    average = sum / length
    return {'sumTotal': sum, 'average': average, 'minimum': minimum, 'maximum': maximum, 'length': length}
print(Analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. 
# Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def Reverse(list):
    for number in range(len(list)//2):
        x = list[number]
        list[number] = list[len(list)-1-number]
        list[len(list)-1-number] = x
    return list
print(Reverse([37,2,1,-9]))
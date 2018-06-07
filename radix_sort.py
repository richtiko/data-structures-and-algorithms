import math

numbers_range = 10**9
digits_range = 1000
digits_count = math.ceil(math.log(numbers_range, digits_range))
print(digits_count)
def counting_sort(array, get_key):
    digits = [0]*digits_range
    
    for i in range(0, len(array)):
        digits[get_key(array[i])] += 1

    for i in range(1, len(digits)):
        digits[i] = digits[i] + digits[i-1]
        
    result = [0] * len(array)
    for i in range(len(array)-1, -1, -1):
        result[digits[get_key(array[i])] - 1] = array[i]
        digits[get_key(array[i])] -= 1
        
    return result
        
def Radix_sort(array):
    n = len(array)
    for i in range(0, digits_count):
        array = counting_sort(array, lambda x: (x // (digits_range**i)) % digits_range )
    return array

def check_is_sorted(array):
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            raise RuntimeError("error")


import random
numbers = [random.randint(1, numbers_range) for i in range(1000000)]


check_is_sorted(Radix_sort(numbers))

print("ok")

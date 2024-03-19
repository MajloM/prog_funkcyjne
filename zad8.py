from functools import reduce

numbers_list = [21,3,0,131,2,1321]

sum_numbers = (reduce(lambda x, y: x + y, numbers_list))

print(sum_numbers)
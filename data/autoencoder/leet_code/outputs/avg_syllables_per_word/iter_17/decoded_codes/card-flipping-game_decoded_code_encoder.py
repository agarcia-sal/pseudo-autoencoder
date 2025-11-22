class Solution:
    def flipgame(self, fronts, backs):
        same = identify_same_numbers(fronts, backs)
        all_numbers = combine_all_numbers(fronts, backs)
        good_numbers = remove_numbers_in_set(all_numbers, same)
        if good_numbers:
            result = find_minimum_number(good_numbers)
            return result
        else:
            return 0

def identify_same_numbers(fronts, backs):
    same_numbers = set()
    for i in range(len(fronts)):
        if fronts[i] == backs[i]:
            same_numbers.add(fronts[i])
    return same_numbers

def combine_all_numbers(fronts, backs):
    combined_numbers = set()
    for num in fronts:
        combined_numbers.add(num)
    for num in backs:
        combined_numbers.add(num)
    return combined_numbers

def remove_numbers_in_set(all_numbers, remove_numbers):
    filtered_numbers = set()
    for num in all_numbers:
        if num not in remove_numbers:
            filtered_numbers.add(num)
    return filtered_numbers

def find_minimum_number(numbers):
    minimum_number = None
    for num in numbers:
        if minimum_number is None or num < minimum_number:
            minimum_number = num
    return minimum_number
class Solution:
    def optimalDivision(self, list_of_numbers):
        if len(list_of_numbers) == 1:
            return str(list_of_numbers[0])
        if len(list_of_numbers) == 2:
            return str(list_of_numbers[0]) + "/" + str(list_of_numbers[1])
        return str(list_of_numbers[0]) + "/(" + "/".join(str(num) for num in list_of_numbers[1:]) + ")"
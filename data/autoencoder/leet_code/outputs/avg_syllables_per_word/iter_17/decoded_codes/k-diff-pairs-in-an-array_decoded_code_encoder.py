class Solution:
    def findPairs(self, list_of_numbers, integer_k):
        if integer_k < 0:
            return 0

        number_counts = {}
        for number in list_of_numbers:
            number_counts[number] = number_counts.get(number, 0) + 1

        unique_pairs_count = 0
        for number in number_counts:
            if integer_k == 0:
                if number_counts[number] > 1:
                    unique_pairs_count += 1
            else:
                if number + integer_k in number_counts:
                    unique_pairs_count += 1

        return unique_pairs_count
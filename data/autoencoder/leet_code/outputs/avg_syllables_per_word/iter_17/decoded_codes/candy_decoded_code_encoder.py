class Solution:
    def candy(self, list_of_ratings):
        number_of_children = len(list_of_ratings)
        list_of_candies = self.initialize_candies(number_of_children)

        for index in range(1, number_of_children):
            if list_of_ratings[index] > list_of_ratings[index - 1]:
                list_of_candies[index] = list_of_candies[index - 1] + 1

        for index in range(number_of_children - 2, -1, -1):
            if list_of_ratings[index] > list_of_ratings[index + 1]:
                list_of_candies[index] = max(list_of_candies[index], list_of_candies[index + 1] + 1)

        total_candies = self.sum_candies(list_of_candies)
        return total_candies

    def initialize_candies(self, number_of_children):
        return [1] * number_of_children

    def sum_candies(self, list_of_candies):
        total = 0
        for candy_count in list_of_candies:
            total += candy_count
        return total
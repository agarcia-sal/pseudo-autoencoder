from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        number_of_people = len(statements)
        maximum_number_of_good_people = 0

        # Iterate over all subsets of people, using bits of i to indicate good/bad status
        for i in range(1 << number_of_people):
            list_of_good_people = [False] * number_of_people
            list_of_bad_people = [False] * number_of_people

            for j in range(number_of_people):
                if (i & (1 << j)) != 0:
                    list_of_good_people[j] = True
                else:
                    list_of_bad_people[j] = True

            valid_combination = True

            # Validate the current assignment against all statements made by good people
            for j in range(number_of_people):
                if list_of_good_people[j]:
                    for k in range(number_of_people):
                        # If person j claims person k is bad but person k is good, or
                        # person j claims person k is good but person k is bad, invalid combination
                        if (statements[j][k] == 0 and list_of_good_people[k]) or \
                           (statements[j][k] == 1 and list_of_bad_people[k]):
                            valid_combination = False
                            break
                    if not valid_combination:
                        break

            if valid_combination:
                count_of_good_people = sum(list_of_good_people)
                if count_of_good_people > maximum_number_of_good_people:
                    maximum_number_of_good_people = count_of_good_people

        return maximum_number_of_good_people
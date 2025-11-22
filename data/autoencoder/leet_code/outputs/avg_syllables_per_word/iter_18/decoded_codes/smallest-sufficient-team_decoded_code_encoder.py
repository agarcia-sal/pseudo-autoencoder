from typing import List, Dict

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        mapping_skills_to_indices = self.create_mapping_of_skills_to_indices(req_skills)
        number_of_skills = len(req_skills)
        number_of_people = len(people)

        skill_bitmasks_for_people = [0] * number_of_people
        for index_of_person, skill_set in enumerate(people):
            mask = 0
            for skill in skill_set:
                if skill in mapping_skills_to_indices:  # Defensive check
                    mask |= 1 << mapping_skills_to_indices[skill]
            skill_bitmasks_for_people[index_of_person] = mask

        max_state = 1 << number_of_skills
        minimum_team_size_dp = [float('inf')] * max_state
        previous_person_for_state_dp = [0] * max_state
        previous_state_dp = [0] * max_state

        minimum_team_size_dp[0] = 0

        for state in range(max_state):
            if minimum_team_size_dp[state] == float('inf'):
                continue
            for person_index in range(number_of_people):
                combined_state = state | skill_bitmasks_for_people[person_index]
                if minimum_team_size_dp[state] + 1 < minimum_team_size_dp[combined_state]:
                    minimum_team_size_dp[combined_state] = minimum_team_size_dp[state] + 1
                    previous_person_for_state_dp[combined_state] = person_index
                    previous_state_dp[combined_state] = state

        current_state = max_state - 1
        answer_team_indices = []
        while current_state > 0:
            person = previous_person_for_state_dp[current_state]
            answer_team_indices.append(person)
            current_state = previous_state_dp[current_state]

        answer_team_indices.reverse()  # To return in the order of selection
        return answer_team_indices

    def create_mapping_of_skills_to_indices(self, req_skills: List[str]) -> Dict[str, int]:
        return {skill: idx for idx, skill in enumerate(req_skills)}
from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        skill_to_index = {}
        for i, skill in enumerate(req_skills):
            skill_to_index[skill] = i

        total_skills = len(req_skills)
        total_people = len(people)

        skill_masks = [0] * total_people
        for i, skill_list in enumerate(people):
            mask = 0
            for skill in skill_list:
                if skill in skill_to_index:
                    mask |= 1 << skill_to_index[skill]
            skill_masks[i] = mask

        max_state = 1 << total_skills
        min_team_size = [inf] * max_state
        last_person = [0] * max_state
        previous_state = [0] * max_state

        min_team_size[0] = 0

        for state in range(max_state):
            if min_team_size[state] == inf:
                continue
            for person_id in range(total_people):
                combined_state = state | skill_masks[person_id]
                if min_team_size[state] + 1 < min_team_size[combined_state]:
                    min_team_size[combined_state] = min_team_size[state] + 1
                    last_person[combined_state] = person_id
                    previous_state[combined_state] = state

        current_state = max_state - 1
        answer = []
        while current_state != 0:
            answer.append(last_person[current_state])
            current_state = previous_state[current_state]

        return answer
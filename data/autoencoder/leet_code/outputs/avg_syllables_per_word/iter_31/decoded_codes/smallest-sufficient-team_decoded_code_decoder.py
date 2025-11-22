from typing import List, Dict

class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_to_index: Dict[str, int] = {skill: i for i, skill in enumerate(req_skills)}
        total_skills = len(req_skills)
        total_people = len(people)

        people_skills_mask = [0] * total_people
        for i, person_skills in enumerate(people):
            mask = 0
            for skill in person_skills:
                if skill in skill_to_index:
                    mask |= 1 << skill_to_index[skill]
            people_skills_mask[i] = mask

        max_state = 1 << total_skills
        INF = float('inf')

        min_team_size = [INF] * max_state
        chosen_person = [0] * max_state
        previous_state = [0] * max_state
        min_team_size[0] = 0

        for curr_state in range(max_state):
            if min_team_size[curr_state] == INF:
                continue
            for i in range(total_people):
                combined_state = curr_state | people_skills_mask[i]
                if min_team_size[curr_state] + 1 < min_team_size[combined_state]:
                    min_team_size[combined_state] = min_team_size[curr_state] + 1
                    chosen_person[combined_state] = i
                    previous_state[combined_state] = curr_state

        final_state = max_state - 1
        answer = []
        while final_state != 0:
            answer.append(chosen_person[final_state])
            final_state = previous_state[final_state]

        answer.reverse()
        return answer
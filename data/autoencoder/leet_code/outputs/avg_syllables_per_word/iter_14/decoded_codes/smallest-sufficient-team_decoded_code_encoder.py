from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_to_index_mapping = {skill: i for i, skill in enumerate(req_skills)}
        total_required_skills = len(req_skills)
        total_people = len(people)

        people_skills_bitmask_list = [0] * total_people
        for i, ss in enumerate(people):
            bitmask = 0
            for s in ss:
                if s in skill_to_index_mapping:
                    bitmask |= 1 << skill_to_index_mapping[s]
            people_skills_bitmask_list[i] = bitmask

        max_state = 1 << total_required_skills
        minimum_team_size_list = [inf] * max_state
        last_added_person_index_list = [0] * max_state
        previous_skill_set_list = [0] * max_state

        minimum_team_size_list[0] = 0

        for i in range(max_state):
            if minimum_team_size_list[i] == inf:
                continue
            for j in range(total_people):
                new_skill_set = i | people_skills_bitmask_list[j]
                if minimum_team_size_list[i] + 1 < minimum_team_size_list[new_skill_set]:
                    minimum_team_size_list[new_skill_set] = minimum_team_size_list[i] + 1
                    last_added_person_index_list[new_skill_set] = j
                    previous_skill_set_list[new_skill_set] = i

        current_skill_set = max_state - 1
        answer_list = []
        while current_skill_set != 0:
            answer_list.append(last_added_person_index_list[current_skill_set])
            current_skill_set = previous_skill_set_list[current_skill_set]

        return answer_list
from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_to_index_map = {}
        skill_index = 0
        for skill in req_skills:
            skill_to_index_map[skill] = skill_index
            skill_index += 1

        total_skills = len(req_skills)
        total_people = len(people)

        skill_bit_mask_list = [0] * total_people
        for person_index in range(total_people):
            for skill in people[person_index]:
                if skill in skill_to_index_map:  # Safeguard if skill not in req_skills
                    skill_bit_mask_list[person_index] |= 1 << skill_to_index_map[skill]

        f_list = [inf] * (1 << total_skills)
        g_list = [0] * (1 << total_skills)
        h_list = [0] * (1 << total_skills)
        f_list[0] = 0

        for skill_state in range(1 << total_skills):
            if f_list[skill_state] == inf:
                continue
            for person_index in range(total_people):
                combined_state = skill_state | skill_bit_mask_list[person_index]
                if f_list[skill_state] + 1 < f_list[combined_state]:
                    f_list[combined_state] = f_list[skill_state] + 1
                    g_list[combined_state] = person_index
                    h_list[combined_state] = skill_state

        current_state = (1 << total_skills) - 1
        answer_list = []
        while current_state != 0:
            answer_list.append(g_list[current_state])
            current_state = h_list[current_state]

        answer_list.reverse()
        return answer_list
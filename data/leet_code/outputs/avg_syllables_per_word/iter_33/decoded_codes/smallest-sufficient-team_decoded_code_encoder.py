from math import inf

class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_to_index = {}
        for i, skill in enumerate(req_skills):
            skill_to_index[skill] = i

        total_skills = len(req_skills)
        total_people = len(people)

        people_skill_masks = [0] * total_people
        for i in range(total_people):
            skill_mask = 0
            for skill in people[i]:
                if skill in skill_to_index:
                    skill_mask |= 1 << skill_to_index[skill]
            people_skill_masks[i] = skill_mask

        dp_min_team_size = [inf] * (1 << total_skills)
        dp_last_person_index = [0] * (1 << total_skills)
        dp_previous_skill_set = [0] * (1 << total_skills)

        dp_min_team_size[0] = 0

        for current_skill_set in range(1 << total_skills):
            if dp_min_team_size[current_skill_set] == inf:
                continue
            for person_index in range(total_people):
                combined_skill_set = current_skill_set | people_skill_masks[person_index]
                if dp_min_team_size[current_skill_set] + 1 < dp_min_team_size[combined_skill_set]:
                    dp_min_team_size[combined_skill_set] = dp_min_team_size[current_skill_set] + 1
                    dp_last_person_index[combined_skill_set] = person_index
                    dp_previous_skill_set[combined_skill_set] = current_skill_set

        final_skill_set = (1 << total_skills) - 1
        answer_team = []
        while final_skill_set != 0:
            answer_team.append(dp_last_person_index[final_skill_set])
            final_skill_set = dp_previous_skill_set[final_skill_set]

        return answer_team
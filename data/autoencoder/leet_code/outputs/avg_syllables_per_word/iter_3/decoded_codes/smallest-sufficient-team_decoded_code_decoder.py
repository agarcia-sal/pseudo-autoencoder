class Solution:
    def smallestSufficientTeam(self, req_skills, people):
        skill_index_map = {skill: i for i, skill in enumerate(req_skills)}
        m, n = len(req_skills), len(people)
        people_skills = [0] * n
        for i, skills in enumerate(people):
            bitmask = 0
            for skill in skills:
                bitmask |= 1 << skill_index_map[skill]
            people_skills[i] = bitmask

        size = 1 << m
        min_team_size = [float('inf')] * size
        chosen_person = [0] * size
        previous_state = [0] * size
        min_team_size[0] = 0

        for skill_set in range(size):
            if min_team_size[skill_set] == float('inf'):
                continue
            for i, p_skills in enumerate(people_skills):
                combined_skills = skill_set | p_skills
                if min_team_size[skill_set] + 1 < min_team_size[combined_skills]:
                    min_team_size[combined_skills] = min_team_size[skill_set] + 1
                    chosen_person[combined_skills] = i
                    previous_state[combined_skills] = skill_set

        current_state = size - 1
        answer = []
        while current_state != 0:
            answer.append(chosen_person[current_state])
            current_state = previous_state[current_state]
        return answer
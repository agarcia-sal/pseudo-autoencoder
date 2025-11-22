class Solution:
    def smallestSufficientTeam(self, required_skills, list_of_people):
        # Create a mapping from skill to its index
        def create_skill_index_map(skills):
            return {skill: i for i, skill in enumerate(skills)}

        skill_index_map = create_skill_index_map(required_skills)
        total_skills = len(required_skills)
        total_people = len(list_of_people)

        # Convert each person's skills to a bitmask
        people_skill_bitmask_list = [0] * total_people
        for i in range(total_people):
            bitmask = 0
            for skill in list_of_people[i]:
                bitmask |= 1 << skill_index_map[skill]
            people_skill_bitmask_list[i] = bitmask

        max_state = 1 << total_skills
        minimum_team_size_list = [float('inf')] * max_state
        last_person_added_list = [0] * max_state
        previous_state_list = [0] * max_state
        minimum_team_size_list[0] = 0

        for current_state in range(max_state):
            if minimum_team_size_list[current_state] == float('inf'):
                continue
            for person_index in range(total_people):
                new_state = current_state | people_skill_bitmask_list[person_index]
                if minimum_team_size_list[current_state] + 1 < minimum_team_size_list[new_state]:
                    minimum_team_size_list[new_state] = minimum_team_size_list[current_state] + 1
                    last_person_added_list[new_state] = person_index
                    previous_state_list[new_state] = current_state

        final_state = max_state - 1
        answer_list = []
        while final_state != 0:
            answer_list.append(last_person_added_list[final_state])
            final_state = previous_state_list[final_state]

        return answer_list[::-1]
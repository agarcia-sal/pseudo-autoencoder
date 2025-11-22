from math import atan2, degrees

class Solution:
    def visiblePoints(self, points, angle, location):
        list_of_angles = []
        count_of_extra_points = 0

        loc_x, loc_y = location

        for x, y in points:
            if x == loc_x and y == loc_y:
                count_of_extra_points += 1
                continue
            angle_in_radians = atan2(y - loc_y, x - loc_x)
            angle_in_degrees = degrees(angle_in_radians)
            list_of_angles.append(angle_in_degrees)

        list_of_angles.sort()
        extended_angles = list_of_angles + [a + 360 for a in list_of_angles]
        list_of_angles = extended_angles

        maximum_visible_points = 0
        left_pointer = 0

        for right_pointer in range(len(list_of_angles)):
            while list_of_angles[right_pointer] - list_of_angles[left_pointer] > angle:
                left_pointer += 1
            maximum_visible_points = max(maximum_visible_points, right_pointer - left_pointer + 1)

        return maximum_visible_points + count_of_extra_points
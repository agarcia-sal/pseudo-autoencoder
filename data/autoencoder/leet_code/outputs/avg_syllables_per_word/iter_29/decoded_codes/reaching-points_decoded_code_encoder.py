class Solution:
    def reachingPoints(self, start_x: int, start_y: int, target_x: int, target_y: int) -> bool:
        while target_x >= start_x and target_y >= start_y:
            if target_x == start_x and target_y == start_y:
                return True
            if target_x > target_y:
                if target_y > start_y:
                    target_x %= target_y
                else:
                    return (target_x - start_x) % target_y == 0
            else:
                if target_x > start_x:
                    target_y %= target_x
                else:
                    return (target_y - start_y) % target_x == 0
        return False
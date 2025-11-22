from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points):
        ans = 0
        for p1 in points:
            cnt = defaultdict(int)
            for p2 in points:
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]
                d = dx * dx + dy * dy
                ans += cnt[d]
                cnt[d] += 1
        return ans * 2
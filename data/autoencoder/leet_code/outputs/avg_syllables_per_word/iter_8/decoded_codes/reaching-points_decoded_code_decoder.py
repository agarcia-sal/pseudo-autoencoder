class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                if ty > sy:
                    tx = tx % ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty = ty % tx
                else:
                    return (ty - sy) % tx == 0
        return False
class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        while tx >= sx and ty >= sy:
            if tx == sx and ty == sy:
                return True
            if tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    # ty == sy, check if (tx - sx) is multiple of ty
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    # tx == sx, check if (ty - sy) is multiple of tx
                    return (ty - sy) % tx == 0
        return False
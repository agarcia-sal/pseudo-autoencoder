def combinationSum(cands, target):
    res = []
    def backtrack(i, tgt, path):
        if tgt == 0:
            res.append(path)
            return
        if tgt < 0:
            return
        for j in range(i, len(cands)):
            backtrack(j, tgt - cands[j], path + [cands[j]])
    backtrack(0, target, [])
    return res
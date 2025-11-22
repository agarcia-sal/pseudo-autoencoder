def letterCombinations(digits):
    if not digits:
        return []
    mapping = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    output = []
    def backtrack(comb, nxt):
        if not nxt:
            output.append(comb)
        else:
            for l in mapping[nxt[0]]:
                backtrack(comb + l, nxt[1:])
    backtrack("", digits)
    return output
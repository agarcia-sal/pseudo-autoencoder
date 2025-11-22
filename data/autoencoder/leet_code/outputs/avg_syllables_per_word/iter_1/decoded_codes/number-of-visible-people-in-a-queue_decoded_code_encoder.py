def process_heights(heights):
    n = len(heights)
    ans = [0] * n
    stk = []
    for i in range(n):
        while stk and heights[stk[-1]] < heights[i]:
            ans[stk.pop()] += 1
        if stk:
            ans[stk[-1]] += 1
        stk.append(i)
    return ans
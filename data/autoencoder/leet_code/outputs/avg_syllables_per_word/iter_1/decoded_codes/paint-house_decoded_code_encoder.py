def min_cost(costs):
    if not costs:
        return 0
    prev_r, prev_b, prev_g = costs[0]
    for i in range(1, len(costs)):
        curr_r = costs[i][0] + min(prev_b, prev_g)
        curr_b = costs[i][1] + min(prev_r, prev_g)
        curr_g = costs[i][2] + min(prev_r, prev_b)
        prev_r, prev_b, prev_g = curr_r, curr_b, curr_g
    return min(prev_r, prev_b, prev_g)
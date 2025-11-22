from collections import deque

def predict_party_victory(senate: str) -> str:
    radiant = deque(i for i, s in enumerate(senate) if s == 'R')
    dire = deque(i for i, s in enumerate(senate) if s == 'D')
    n = len(senate)

    while radiant and dire:
        r = radiant.popleft()
        d = dire.popleft()
        if r < d:
            radiant.append(r + n)
        else:
            dire.append(d + n)

    return "Radiant" if radiant else "Dire"
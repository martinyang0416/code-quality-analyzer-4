import collections

def predictPartyVictory(senate):
    radiant = collections.deque()
    dire = collections.deque()
    n = len(senate)
    for i, c in enumerate(senate):
        if c == 'R':
            radiant.append(i)
        else:
            dire.append(i)
    
    while radiant and dire:
        r = radiant[0]
        d = dire[0]
        if r < d:
            radiant.popleft()
            dire.popleft()
            radiant.append(r + n)
        else:
            dire.popleft()
         
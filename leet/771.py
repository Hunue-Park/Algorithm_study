# jewels and stones

def numJewelsInStones(self, J, S):
    return sum(s in J for s in S)
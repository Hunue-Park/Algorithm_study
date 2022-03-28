# letter combinations of a phone number
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_boards = [[],[], ['a', 'b', 'c'], ['d', 'e', 'f'], 
                    ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'], 
                    ['p', 'q','r','s'],['t','u','v'],['w','x','y','z']]

        if not digits:
            return []

        digit = list(map(int, digits))

        select = []

        for d in digit:
            select.append(phone_boards[d])
        # *select 는 언패킹 오퍼레이터. 
        prod = list(product(*select))
        result = []
        for char in prod:
            tmp = ""
            for c in char:
                tmp += c
            result.append(tmp)
        return result

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        # 같은 철자로 이루어진 단어 원소를 각각의 리스트로 보낸다.
        #     같은 철자로 이루어진걸 어떻게 확인? 
        #         -> 단어를 알파벳별로 쪼개고 정렬시키면 같은 알파벳으로 구성되면 똑같은 결과물이 나옴
        # 해당 리스트 들을 원소로 가지는 2차원 리스트를 출력한다.
        result = defaultdict(list)
        for str in strs:
            # ''.join 은 애너그램key 를 만드는 부분 append() 부분은 value 를 넣는다.
            result[''.join(sorted(str))].append(str)
        # 리턴값은 딕셔너리의 value 만! 
        return list(result.values())
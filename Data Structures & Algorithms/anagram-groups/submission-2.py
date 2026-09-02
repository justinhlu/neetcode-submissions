class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            freqArr = [0] * 26
            for c in s:
                freqArr[ord(c) - ord('a')] += 1
            res[tuple(freqArr)].append(s)
        return list(res.values())
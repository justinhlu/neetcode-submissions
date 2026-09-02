class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {}

        for string in strs:
            sortedStr = "".join(sorted(string))
            print(sortedStr)
            if sortedStr in anaDict:
                anaDict[sortedStr].append(string)
            else:
                anaDict[sortedStr] = [string]
        return list(anaDict.values())
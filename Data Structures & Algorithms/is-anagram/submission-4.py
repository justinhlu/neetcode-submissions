class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        if len(s) != len(t):
            return False
            
        for c in s:
            if c in s_map:
                s_map[c] = s_map[c] + 1
            else:
                s_map[c] = 1

        for c in t:
            if c in t_map:
                t_map[c] = t_map[c] + 1
            else:
                t_map[c] = 1
        
        
        for c in s:
            if c in s_map and c in t_map:
                if s_map[c] != t_map[c]:
                    return False
            else:
                return False
        
        return True

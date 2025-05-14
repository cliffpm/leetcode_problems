class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if s and t different lengths, cannot be anargrams
        if len(s) != len(t):
            return False
        
        #anagram if frequency of each character is the same 
        #and contains same unique characters per s and t

        s_char_to_count = Counter(s)
        t_char_to_count = Counter(t)

        if s_char_to_count.keys() != t_char_to_count.keys():
            return False
        
        for char in s_char_to_count.keys():
            if s_char_to_count.get(char) != t_char_to_count.get(char):
                return False
            else: continue

        return True

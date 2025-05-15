class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      '''
      All anagrams will have the same sorted word when they are all sorted. This can be used in a hashmap where the 
      sorted word is the key and the values is all the words that have this word when sorted.
      Return the values afterwards
      '''
        res = []
        hm = {}
        for word in strs:
            curr = word
            sort = "".join(sorted(list(word)))
            if sort not in hm:
                hm[sort] = [word]
            else: hm.get(sort).append(word)
        return list(hm.values())
            

        

        


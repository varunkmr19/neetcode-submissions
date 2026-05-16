class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # early return: edge case
        if len(strs) == 1:
            return [strs]

        output = []
        seen = set()
        for i in range(0, len(strs)):
            if i in seen:
                continue
            
            anagrams = []
            anagrams.append(strs[i])
            for j in range(i+1, len(strs)):
                if j in seen:
                    continue

                if Counter(strs[i]) == Counter(strs[j]):
                    anagrams.append(strs[j])
                    seen.add(j)

            output.append(anagrams)

        return output
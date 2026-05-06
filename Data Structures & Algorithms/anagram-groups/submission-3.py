from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i in range(len(strs)):
            sorted_text = "".join(sorted(strs[i]))
            anagrams[sorted_text].append(i)

        res = []
        for vals in anagrams.values():
            sub_res = []
            for val in vals:
                sub_res.append(strs[val])
            res.append(sub_res)

        return res



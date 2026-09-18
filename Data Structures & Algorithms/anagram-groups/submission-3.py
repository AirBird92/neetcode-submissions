class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        offset = ord("a")
        groups = defaultdict(list)
        for s in strs:
            freqs = [0] * 26
            for c in s:
                freqs[ord(c) - offset] += 1
            groups[tuple(freqs)].append(s)
        return list(groups.values())
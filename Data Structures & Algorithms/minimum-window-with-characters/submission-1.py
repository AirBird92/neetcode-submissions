class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ls, lt = len(s), len(t)
        if ls < lt:
            return ""

        t_freq_map = defaultdict(int)
        for c in t:
            t_freq_map[c] += 1

        s_freq_map = defaultdict(int)
        left = found = 0
        need = len(t_freq_map)
        res_len = float('inf')
        res = ""
        for right in range(ls):
            cur = s[right]
            s_freq_map[cur] += 1

            if cur in t_freq_map and s_freq_map[cur] == t_freq_map[cur]:
                found += 1

            while found == need:
                if right - left + 1 <  res_len:
                    res_len = right - left + 1
                    res = s[left : right + 1]

                s_freq_map[s[left]] -= 1
                if s[left] in t_freq_map and s_freq_map[s[left]] < t_freq_map[s[left]]:
                    found -= 1
                left += 1
        return res

class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        sizes = []
        for s in strs:
            sizes.append(str(len(s)))
        return f"{",".join(sizes)}#{"".join(strs)}"

    def decode(self, s: str) -> List[str]:
        print(s)
        if not s:
            return []

        i = 0
        while s[i] != "#":
            i += 1
        sizes = list(map(int, s[:i].split(",")))
        
        i += 1
        res = []
        for l in sizes:
            res.append(s[i:i + l])
            i += l
        return res
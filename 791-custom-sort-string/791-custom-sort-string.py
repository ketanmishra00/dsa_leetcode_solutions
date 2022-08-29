class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        cc = Counter(s)
        for x in order:
            if x in cc:
                res.append(x * cc.pop(x))
        if cc:
            for x in cc.copy():
                res.append(x * cc.pop(x))
        return ''.join(res)
        
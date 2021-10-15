```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        sCounter = collections.Counter(s[:len(p)-1])
        pCounter = collections.Counter(p)
        for i in range(len(p)-1, len(s)):
            sCounter[s[i]] +=1 
            if sCounter == pCounter:
                res.append(i-len(p)+1)
            sCounter[s[i-len(p)+1]] -= 1
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]
        return res
```


https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.

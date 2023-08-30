class Solution:
    def maxUniqueSplit(self, s):
        n = len(s)

        def backtrack(s,path):
            if not s:
                res.append(path)

            for i in range(1,len(s)+1):
                if s[:i] not in path:
                    backtrack(s[i:],path+[s[:i]])

        res = []
        backtrack(s,[])
        return max([len(i) for i in res])
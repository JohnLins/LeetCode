class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:


        children = []
        s = {}
        for i in range(len(edges)+1):
            children.append([])
        for i in range(len(edges)):
            children[edges[i][0]].append(edges[i][1])
            children[edges[i][1]].append(edges[i][0])


        def rec(n, prev):
            size = 1
            for c in children[n]:
                if c != prev:
                    size += rec(c, n)
            s[n] = size
            return size

        rec(0,None)

        output = 0
        for n in range(len(edges)+1):
            sizes = set()
            for c in children[n]:
                if s[c] < s[n]:
                    sizes.add(s[c])
            if len(sizes) in [0,1]:
                output += 1
        return output


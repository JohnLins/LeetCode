class Solution:


    def generateParenthesis(self, n: int) -> List[str]:
        things = []
        things.append("()")

        while len(things[0]) < n*2:
            print(things)
            new = set()
            for i in range(len(things)):
                for j in range(len(things[i])):
                    thing = things[i][:j]+"()"+things[i][j:]
                    new.add(thing)
            things = list(new)



        return things



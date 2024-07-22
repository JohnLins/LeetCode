class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        start = 0
        lastwasslash = False
        if path[-1] != "/":
            path += "/"
        for i in range(len(path)):
            if (path[i] == '/') and start != i and not lastwasslash:
                directory = path[start:i]
                if directory not in ["/.","/.."]:
                    stack.append(directory)

                if directory == "/..":
                    if len(stack) != 0:
                        print(stack.pop())

                start = i+1
            if path[i] != '/':
                lastwasslash = False
            else:
                lastwasslash = True
                start = i
        print(stack)
        output = ""
        for i in stack:
            output += i
        if output == "":
            return "/"
        return output

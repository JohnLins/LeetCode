class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i = 0
        j = 0
        for k in range(len(commands)):
            if commands[k] == "UP":
                i-=1
            elif commands[k] == "RIGHT":
                j+=1
            elif commands[k] == "DOWN":
                i+=1
            elif commands[k] == "LEFT":
                j-=1

        return (i*n)+j

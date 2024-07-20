class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        toadd = []

        larger = num1
        smaller = num2
        if num1 < num2:
            larger = num2
            smaller = num1


        dic = {"0":0, "1":1, "2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8": 8, "9":9}

        zeros = ""
        for s in range(len(smaller)):
            carry = 0
            y = ""
            for i in range(len(larger)):

                x = (dic[smaller[len(smaller)-s-1]]) * (dic[larger[len(larger)-1-i]])+(carry)

                if x >= 10:
                    y = str((int)(x%10))+y
                    carry = (int)(x/10)
                else:
                    y = str(x)+y
                    carry = 0
            if carry != 0:
                y = str(carry) + y
            toadd.append(y+zeros)
            zeros += "0"
        print(toadd)

        output = ""
        carry = 0
        digitsexist = len(toadd)
        fromright = 0
        while digitsexist>0:
            digitsexist = 0
            x = carry
            for j in range(len(toadd)):
                if fromright < len(toadd[j]):
                    digitsexist += 1
                    x += dic[toadd[j][len(toadd[j])-1-fromright]]
            fromright += 1
            output = str(x%10) + output
            carry = (int)(x/10)

        z = 0
        while z < len(output)-1 and output[z] == "0":
            z += 1

        return output[z:]



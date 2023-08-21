### method1:
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_str = bin(x)
        y_str = bin(y)

        x_str = x_str[2:]
        y_str = y_str[2:]

        if len(x_str) == min(len(x_str), len(y_str)):
            x_str = (len(y_str) - len(x_str))*'0' + x_str
        else:
            y_str =(len(x_str) - len(y_str))*'0' + y_str

        count = 0
        for i in range(len(y_str)):
            if x_str[i] != y_str[i]:
                count = count + 1

        return count

### method2:
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x^y
        z_str = bin(z)[2:]
        print(z_str)
        count = 0
        for i in range(len(z_str)):
            if z_str[i] == '1':
                count += 1
        return count

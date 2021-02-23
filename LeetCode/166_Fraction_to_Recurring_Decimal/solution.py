class Solution:
    def principal_period(self, s):
        i = (s + s).find(s, 1, -1)
        return None if i == -1 else s[:i]

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        decimalStrArray = []
        result = numerator // denominator
        remaining = numerator % denominator

        decimalStrArray.append(f"{result}")
        numerator = remaining * 10

        idx = 10
        while idx > 0:
            result = numerator // denominator
            remaining = numerator % denominator
            decimalStrArray.append(f"{result}")
            numerator = remaining * 10
            idx -= 1

        print(decimalStrArray)
        decimals = decimalStrArray[0]
        del decimalStrArray[0]
        digits = "".join(decimalStrArray)
        repeatingPattern = self.principal_period(digits)

        if repeatingPattern == None:
            decimals = decimals + "." + digits
        else:
            decimals = decimals + ".(" + repeatingPattern + ")"

        return decimals


decimalStr = Solution().fractionToDecimal(1, 2)
print(decimalStr)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        ans = []
        s = ""
        def backtracking(digits, index, s):
            if index == len(digits):
                ans.append(s)
                return
            letters = letterMap[int(digits[index])]
            for letter in letters:
                s += letter
                backtracking(digits, index + 1, s)
                s = s[:-1]
        if digits == "": return ans
        else:
            backtracking(digits, 0, s)
            return ans

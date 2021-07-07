# if right < left 인 이유..
# For the output string to be right, stack of ")" most be larger than stack of "(". If not, it creates string like "())"

# if not left and not right 인 이유..
# Since elements in each of stack are the same, we can simply express them with a number. For example, left = 3 is like a stacks ["(", "(", "("]

class Solution:
# @param {integer} n
# @return {string[]}
    def generateParenthesis(self, n):
        if n is None:
            return []

        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans

    def dfs(self, left, right, ans, string):

        if right < left:
            return
        if not left and not right:
            print(string)
            ans.append(string)
            return
        #print(string)
        if left:
            self.dfs(left - 1, right, ans, string + "(")

        if right:
            self.dfs(left, right - 1, ans, string + ")")

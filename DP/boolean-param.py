class Solution:
    def solveRecursive(self, expression, operands, i, j, dp):
        expression_cnt = {"T": 0, "F": 0}
        if(dp[i][j]!=-1):
            return dp[i][j]
        if(i == j):
            expression_cnt[expression[i]]+=1
            return expression_cnt

        elif(i>j):
            expression_cnt['F']+=1
            return expression_cnt

        else:
            for k in range(i, j):
                c1 = Solution.solveRecursive(self, expression, operands, i, k, dp)
                c2 = Solution.solveRecursive(self, expression, operands, k+1, j, dp)
                for key in c1.keys():
                    if(c1[key]>0):
                        for key2 in c2.keys():
                            if(c2[key2]>0):
                                if(key == 'T'):
                                    exp1 = True
                                else:
                                    exp1 = False

                                if(key2 == 'T'):
                                    exp2 = True
                                else:
                                    exp2 = False

                                if(operands[k] == "^"):
                                    result = exp1^exp2

                                elif(operands[k]=="&"):
                                    result = exp1 and exp2

                                else:
                                    result = exp1 or exp2

                                if(result):
                                    expression_cnt['T'] += c1[key]*c2[key2]
                                else:
                                    expression_cnt['F'] += c1[key]*c2[key2]


            dp[i][j] = expression_cnt
            return dp[i][j]

    def cnttrue(self, A):
        expressions = []
        operands = []
        for i in range(len(A)):
            if(A[i]!="|" and A[i]!="&" and A[i]!="^"):
                expressions.append(A[i])
            else:
                operands.append(A[i])

        dp = [[-1 for i in range(len(expressions)+1)] for j in range(len(expressions)+1)]
        return (self.solveRecursive(expressions, operands, 0, len(expressions) - 1, dp)['T'])%(10**3 + 3)
        
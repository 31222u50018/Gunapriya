def solve(scores, ages):
   sa = [[a,s] for a,s in zip(ages,scores)]

   sa.sort()
   scores = [s for a,s in sa]

   maxScore = 0
   n = len(scores)
   dp = [0] * n

   for i in range(n):
      score = scores[i]
      dp[i] = score

      for j in range(i):
         if scores[j] <= score:
            dp[i] = max(dp[i],dp[j] + score)
      maxScore = max(maxScore, dp[i])

   return maxScore

scores = [5,7,9,14,19]
ages = [5,6,7,8,9]
print(solve(scores, ages))
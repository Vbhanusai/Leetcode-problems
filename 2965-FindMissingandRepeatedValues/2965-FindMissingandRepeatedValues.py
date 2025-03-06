class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N=len(grid[0])
        sum_of_ele=0
        sum_of_ele_sq=0
        for i in range(N):
            for j in range(N):
                sum_of_ele+=grid[i][j]
                sum_of_ele_sq+=grid[i][j]**2
        print(sum_of_ele,sum_of_ele_sq)
        n=N**2
        b_minus_a = ( (n*(n+1))//2 ) - sum_of_ele
        b_plus_a = ( (n*(n+1)*(2*n+1))//6 - sum_of_ele_sq )//b_minus_a
        print(b_minus_a,b_plus_a)
        b = (b_plus_a + b_minus_a)//2
        a = (b_plus_a - b_minus_a)//2
        return [a,b]
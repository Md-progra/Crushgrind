class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_multiplier = 1
        right_multiplier = 1
        n = len(nums)
        left_arr = [0]*n
        right_arr = [0]*n
        answer = [] * n
        for i in range(n):
            j = -i-1 #(moves as i moves)
            left_arr[i] = left_multiplier
            right_arr[j] = right_multiplier
            left_multiplier *= nums[i]
            right_multiplier *= nums[j]
        for l,r in zip(left_arr,right_arr):
            answer.append(l*r)
        return answer



        
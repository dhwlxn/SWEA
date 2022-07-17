N = int(input())
 
nums = list(map(int, input().split())) 
nums.sort() 
 
mid = N // 2 
print(nums[mid])
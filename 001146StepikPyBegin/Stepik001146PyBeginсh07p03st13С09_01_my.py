n = int(input())
nums = []
nums2 = []
for i in range(n):
    nums.append(int(input()))
    print("nums.append", nums)
nums2 = sorted(nums)
print("sorted(nums)", nums2)
print(nums2[n - 2])
print(nums2[n - 1])

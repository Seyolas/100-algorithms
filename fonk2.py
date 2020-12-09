#bir dizinin monoton olup olmadığını bulmak

a=[6,5,4,4]
b=[1,1,1,3,3,4,3,2,4,2]
c=[1,1,2,3,7]

def çözüm(nums):
    return (all(nums[i]<=nums[i+1] for i in range(len(nums)-1)) or
            all(nums[i]>=nums[i+1] for i in range(len(nums)-1)))


print(çözüm(a))


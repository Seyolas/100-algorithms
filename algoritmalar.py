import numpy as np

#0ları sona taşıyan fonksiyon

array1=[1,7,0,7,8,0,10,12,0,4]

def çözüm(nums):
    for i in nums:
        if i ==0:
            nums.remove(0)
            nums.append(0)
    return nums


print(çözüm(array1))






# Move Zeros to end While mainting the the relative order of non zeros numbers
def moveZeros(nums):
    lastNonZeroFoundAt = 0
    for i in range(len(nums)):
        if nums[i] !=0:
            nums[i], nums[lastNonZeroFoundAt] =nums[lastNonZeroFoundAt],nums[i]
            lastNonZeroFoundAt+=1
    return nums

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    print("Moved Zeros to End:", moveZeros(nums))  
def productExceptSelf( nums):
    n = len(nums)
    answer = [1] * n

        # Step 1: prefix product (from left)
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

        # Step 2: suffix product (from right)
    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer
 
if __name__ == "__main__":
    nums = [1,2,3,4]
    print("product of array except itself:", productExceptSelf(nums)) 
        
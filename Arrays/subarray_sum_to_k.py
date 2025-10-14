def subarray_sum_to_k(arr, k):
    count=0
    prefix_sum=0
    prefix_sum_map={0:1}
    for i in range(len(arr)):
        prefix_sum+=arr[i]
        if prefix_sum - k in prefix_sum_map:
            count+=prefix_sum_map[prefix_sum-k]
        prefix_sum_map[prefix_sum]=prefix_sum_map.get(prefix_sum,0)+1
    return count

if __name__ == "__main__":
    arr=[1,2,3,4,5]
    k=5
    print(subarray_sum_to_k(arr,k))

def even(nums):
    x = []
    for i in nums:
        if i % 2 == 0 and i<51:
            x.append(i)
    return x
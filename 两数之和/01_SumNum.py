def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    """
    #  暴力穷举
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == target - nums[j]:
                return [i, j]
    """

    temp_nums = list(nums)

    #  排序
    for i in range(1, len(nums)):
        for j in range(0, len(nums) - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    #  找到排序后的下标
    return_head = 0
    return_tail = len(nums) - 1
    sum_num = nums[return_head] + nums[return_tail]
    while sum_num != target:
        if sum_num > target:
            return_tail -= 1
        elif sum_num < target:
            return_head += 1
        sum_num = nums[return_head] + nums[return_tail]

    #  对应到list中的下标并return
    head = temp_nums.index(nums[return_head])
    tail = temp_nums.index(nums[return_tail])
    if head > tail:
        head, tail = tail, head

    return [head, tail]


if __name__ == "__main__":
    nums = [3, 2, 6]
    target = 9
    a = twoSum(nums, target)
    print(a)

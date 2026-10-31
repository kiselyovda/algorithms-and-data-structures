def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
    left = 0
    right = len(nums) - 1
    while left != right:
        tmp = nums[left] + nums[right]
        if tmp == target:
            return nums[left], nums[right]
        if tmp < target:
            left += 1
            continue
        right -= 1
    return None


def main():
    nums = [2, 4, 8, 9, 11, 12, 16, 21]
    target = 19
    result = two_sum(nums=nums, target=target)
    print(result)


if __name__ == '__main__':
    main()

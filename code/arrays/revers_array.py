def revers_array(nums: list[int]) -> list[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
    return nums


def main() -> None:
    nums = [2, 7, 8, 9, 11, 12, 16, 21]
    result = revers_array(nums=nums)
    print(result)


if __name__ == "__main__":
    main()

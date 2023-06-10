from collections import Counter


def find_duplicate(nums):
    if (
        not nums
        or not all(isinstance(num, int) for num in nums)
        or any(num < 0 for num in nums)
        or len(nums) == len(set(nums))
    ):
        return False
    return Counter(nums).most_common(1)[0][0]

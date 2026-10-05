class Solution:
    def rotate(self, nums: list[int], k: int) -> None:

        rotated = [0] * len(nums)

        k = k % len(nums)

        for i, num in enumerate(nums):
            rotated[((i + k)) % len(nums)] = num

        nums[:] = rotated[:]
        """
        Do not return anything, modify nums in-place instead.
        """

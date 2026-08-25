class Solution:
	def hasDuplicate(self, nums: list[int]) -> bool:
		num_set= set(nums)
		return len(num_set) != len(nums)

        
from interfaces.sort_interface import SortAlgorithm


class BubbleSortStrategy(SortAlgorithm):
  def __init__(self) -> None:
    super().__init__()
    self.nums = None

  def sort(self, nums):
    self.nums = nums.copy()
    self._sort()
    print(self.nums)

  def _sort(self):
    for i in range(len(self.nums)):
      swaps = 0

      for j in range(1, len(self.nums) - i):
        if self.nums[j - 1] > self.nums[j]:
          self.nums[j - 1], self.nums[j] = self.nums[j], self.nums[j - 1]
          swaps += 1
      
      if not swaps:
        return
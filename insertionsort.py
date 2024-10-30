from SortInterface import SortAlgorithm


class InsertionSortStrategy(SortAlgorithm):
  def __init__(self) -> None:
    super().__init__()
    self.nums = None

  def sort(self, nums):
    self.nums = nums.copy()
    self._sort()
    print(self.nums)
  
  def _sort(self):
    for i in range(1, len(self.nums)):
      key = self.nums[i]
      j = i - 1

      while j >= 0 and key < self.nums[j]:
        self.nums[j + 1] = self.nums[j]
        j -= 1
      self.nums[j + 1] = key
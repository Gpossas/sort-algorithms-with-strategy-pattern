from interfaces.sort_interface import SortAlgorithm


class QuickSortStrategy(SortAlgorithm):
  def __init__(self) -> None:
    super().__init__()
    self.nums = None

  def sort(self, nums):
    self.nums = nums.copy()
    self._quicksort(0, len(self.nums) - 1)
    print(self.nums)
  
  def _quicksort(self, left, right):
    if left >= right:
      return
    
    partition_index = self.partition(left, right)
    self._quicksort(left, partition_index - 1)
    self._quicksort(partition_index + 1, right)

  def partition(self, left, right):
    pivot = self.nums[right]
    partition_index = left
    for i in range(left, right):
      if self.nums[i] < pivot:
        self.nums[i], self.nums[partition_index] = self.nums[partition_index], self.nums[i]
        partition_index += 1
    self.nums[partition_index], self.nums[right] = self.nums[right], self.nums[partition_index]
    return partition_index
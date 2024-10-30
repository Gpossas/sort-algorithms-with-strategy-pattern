from interfaces.sort_interface import SortAlgorithm


class SortClass:
  def __init__(self) -> None:
    self.nums = []
    with open("extra.txt") as f:
      for line in f:
        self.nums.append(int(line))

  def sort(self, algorithm: SortAlgorithm):
    algorithm.sort(self.nums)

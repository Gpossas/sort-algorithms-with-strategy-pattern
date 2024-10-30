# usage
from bubblesort import BubbleSortStrategy
from insertionsort import InsertionSortStrategy
from quicksort import QuickSortStrategy
from sort import SortClass


sort_class = SortClass()

sort_class.sort(InsertionSortStrategy())
sort_class.sort(QuickSortStrategy())
sort_class.sort(BubbleSortStrategy())
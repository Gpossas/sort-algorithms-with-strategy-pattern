# usage
from algorithms.bubblesort import BubbleSortStrategy
from algorithms.insertionsort import InsertionSortStrategy
from algorithms.quicksort import QuickSortStrategy
from sort import SortClass


my_sort = SortClass()

my_sort.sort(InsertionSortStrategy())
my_sort.sort(QuickSortStrategy())
my_sort.sort(BubbleSortStrategy())

# Start by reading the vertical input lists from input.txt and have 2 vertical lists sorted ascending

from typing import List, Tuple
from collections import Counter

file_path = 'input.txt'


def read_input() -> Tuple[List[int], List[int]]:
  """
  'Throughout the Chief's office, the historically significant locations are
    listed not by name but by a unique number called the Location ID. To make
    sure they don't miss anything, the Historians split into two groups,
    each searching the office and trying to create their own complete list
    of location IDs.'

  Reads the file and parses the lines into two lists of integers.
  """
  list1 = []
  list2 = []
  with open(file_path, 'r') as file:
    lines = file.readlines()

  for line in lines:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

  return list1, list2


def count_occurrences(list: List[int]) -> Counter:
  """
  Counts the occurrences of each element in a list.
  """
  return Counter(list)


def get_total_distance_between_lists() -> int:
  """
  'Pair up the smallest number in the left list with the smallest number in the
  right list, then the second-smallest left number with the second-smallest
  right number, and so on.

  Within each pair, figure out how far apart the two numbers are; you'll need
  to add up all of those distances. For example, if you pair up a 3 from the
  left list with a 7 from the right list, the distance apart is 4; if you pair
  up a 9 with a 3, the distance apart is 6.'
  """
  list_1, list_2 = read_input()
  list_1.sort()
  list_2.sort()
  diff_sum: int = 0
  for index in range(len(list_1)):
    diff_sum += abs(list_1[index] - list_2[index])
  return diff_sum


def get_similarity_score() -> int:
  list_1, list_2 = read_input()
  list_1.sort()
  counter_list2 = Counter(list_2)

  similarity_sum = 0

  for value in list_1:
    similarity_sum += value * counter_list2[value]

  return similarity_sum


if __name__ == "__main__":
  print(get_total_distance_between_lists())  # 1223326
  print(get_similarity_score()) # 21070419

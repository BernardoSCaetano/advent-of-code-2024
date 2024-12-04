from typing import List, Tuple
from re import findall


class Solution():

  def read_corrupted_file(self) -> str:
    with open("input.txt", 'r') as file:
      corrupted_file = file.read()

    return corrupted_file

  def clean_up_file(self, corrupted_file_String: str) -> List[str]:
    '''
    Clean file should only contain mul(int1,int2) where int1 and int2 are integers
    :param corrupted_file_String: original content from input.txt
    :return: cleaned up file
    '''
    # regex: str = r"(mul\((\d+),(\d+)\))"
    regex: str = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"

    match_list = findall(regex, corrupted_file_String)

    return match_list

  def multiply_all_values(self, numbers_to_multiply: List[Tuple[str, str]]) -> (
    int):
    return sum(int(n1) * int(n2) for full_match, n1, n2 in numbers_to_multiply
               if full_match.startswith("mul("))

  def multiply_values_after_do_and_dont(self, numbers_to_multiply: List[
    Tuple[str, str, str]]) -> int:
    enabled = True
    total = 0  # Initialize a variable to accumulate the sum

    for full_match, n1, n2 in numbers_to_multiply:
      if full_match.startswith("do()"):
        enabled = True
      elif full_match.startswith("don't()"):
        enabled = False
      elif enabled:
        total += int(n1) * int(n2)  # Add the product to the total

    return total  # Return the accumulated sum


if __name__ == "__main__":
  solution = Solution()
  corrupted_file = solution.read_corrupted_file()
  cleaned_up_list = solution.clean_up_file(corrupted_file)
  print(solution.multiply_all_values(cleaned_up_list))  # 174960292
  print(
    solution.multiply_values_after_do_and_dont(cleaned_up_list))  # 56275602

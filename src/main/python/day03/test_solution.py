from solution import Solution
import unittest

class TestSolution(unittest.TestCase):

  def test_read_file(self):
    solution = Solution()
    raw_file: str = solution.read_corrupted_file()

    mul_tuples = solution.clean_up_file(raw_file)

    sum_all_multiplications = solution.multiply_all_values(mul_tuples)

    self.assertEqual(174960292, sum_all_multiplications)

    sum_all_multiplications = solution.multiply_values_after_do_and_dont(
      mul_tuples)

    self.assertEqual(56275602, sum_all_multiplications)

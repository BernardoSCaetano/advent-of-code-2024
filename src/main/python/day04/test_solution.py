from unittest import TestCase
from solution import (read_input_and_create_matrix, word_search_count,
                      x_two_MAS_search_count)

class TestSolution(TestCase):

  def test_solution(self):

    matrix = read_input_and_create_matrix()

    self.assertEqual(word_search_count(matrix, "XMAS"), 2496)
    self.assertEqual(x_two_MAS_search_count(matrix), 1967)

from typing import List, Tuple


def read_input_and_create_matrix() -> List[List[str]]:
  with open("input.txt", 'r') as file:
    matrix = [[char for char in line.strip()] for line in file]

  return matrix


directions: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0),
                                     (1, 1), (1, -1), (-1, 1), (-1, -1)]


def search(matrix, i, j, direction, word):
  if len(word) == 0:
    return True

  if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][
    j] != word[0]:
    return False

  temp = matrix[i][j]
  matrix[i][j] = ' '

  if search(matrix, i + direction[0], j + direction[1], direction, word[1:]):
    matrix[i][j] = temp
    return True

  matrix[i][j] = temp
  return False


def word_search_count(matrix: List[List[str]], word: str) -> int:
  """
  Count for appeareces of a word in a matrix. Look for Horizontal, Vertical and
  Diagonal appearences. The word can be read in any direction.

  :param matrix:  List of Lists of characters
  :param word:    Word to search
  :return:        Number of appearences of the word in the matrix
  """
  word_appearances: int = 0
  for i, line in enumerate(matrix):
    for j, char in enumerate(line):
      if char == word[0]:
        for direction in directions:  # We need to check all directions and count the appearances
          if search(matrix, i, j, direction, word):
            word_appearances += 1
  return word_appearances


def get_diagonal_words(matrix: List[List[str]], i: int, j: int) -> Tuple[str,
str]:
  return (matrix[i - 1][j - 1] + matrix[i][j] + matrix[i + 1][j + 1],
          matrix[i - 1][j + 1] + matrix[i][j] + matrix[i + 1][j - 1])


def x_two_MAS_search_count(matrix: List[List[str]]) -> int:
  """
  Look for the word in the matrix in a X format. The word must appear twice in 
  the matrix. For now, we are only looking for the word "MAS" in the 
  where the same "A" is used for both appearences.

  M.S
  .A.
  M.S
  
  :param matrix:  List of Lists of characters
  :return:        Number of appearences of the word in the matrix
  """
  word_appearances: int = 0

  for i in range(len(matrix)):
    for j, char in enumerate(matrix[i]):
      if char == "A":
        # get both diagonols, check if they are mas or sam, if so, counter + 1
        try:
          word1, word2 = get_diagonal_words(matrix, i, j)
        except IndexError:
          continue
        if (word1 == "MAS" or word1 == "SAM") and (
          word2 == "MAS" or word2 == "SAM"):
          word_appearances += 1
  return word_appearances


if __name__ == "__main__":
  matrix = read_input_and_create_matrix()
  print(word_search_count(matrix, "XMAS"))  # 3601
  print(x_two_MAS_search_count(matrix))  # 3601

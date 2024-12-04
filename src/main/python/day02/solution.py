from day01.solution import file_path

from typing import List

file_path = "input.txt"


def read_file():
  with open(file_path, 'r') as file:
    lines = file.readlines()

  reports = []
  for line in lines:
    reports.append(list(map(int, line.split())))
  return reports


def is_safe_report(report):
  if len(report) == 1:
    return True

  is_ascending = True
  is_descending = True

  for i in range(1, len(report)):
    current_level = report[i]
    previous_level = report[i - 1]

    if abs(current_level - previous_level) > 3:
      return False

    elif current_level > previous_level:
      is_descending = False
    elif current_level < previous_level:
      is_ascending = False
    else:
      return False

  return is_ascending or is_descending

def get_number_of_safe_reports(reports : List[int]) -> int:
  return sum([is_safe_report(report) for report in reports])

def get_number_of_safe_reports_with_damping(reports : List[int]) -> int:
  safe_report_counter = 0

  for report in reports:

    if is_safe_report(report):
      safe_report_counter += 1
    else:
      for i in range(len(report)):
        if is_safe_report(report[:i] + report[i+1:]):
          safe_report_counter += 1
          break

  return safe_report_counter


if __name__ == "__main__":
  reports = read_file()
  print(get_number_of_safe_reports(reports))  # 246
  print(get_number_of_safe_reports_with_damping(reports))  # 318


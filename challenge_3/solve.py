#!/usr/bin/python3

import os

right_step = 3
down_step = 1

def part_one():
	i = 0
	j = 0
	line_len = len(matrix[0])
	column_len = len(matrix)
	count = 0

	while True:
		i += right_step
		j += down_step

		if j >= column_len:
			break
		if i > line_len-1:
			i = i % line_len
		if matrix[j][i] == "#":
			count += 1

	return count
	

def part_two():
	global right_step
	global down_step

	result = 0

	right_step = 1
	down_step = 1
	count = part_one()
	print(f"Intermediate Count: {count}")
	result = count

	right_step = 3
	down_step = 1
	count = part_one()
	print(f"Intermediate Count: {count}")
	result *= count

	right_step = 5
	down_step = 1
	count = part_one()
	print(f"Intermediate Count: {count}")
	result *= count

	right_step = 7
	down_step = 1
	count = part_one()
	print(f"Intermediate Count: {count}")
	result *= count

	right_step = 1
	down_step = 2
	count = part_one()
	print(f"Intermediate Count: {count}")
	result *= count

	return result

input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_3/input.txt")
with open(input_path, "r") as input_fp:
	matrix = []
	for line in input_fp.readlines():
		matrix_line = []
		for char in line.strip():
			matrix_line.append(char)
		matrix.append(matrix_line)
	print("\n".join(["".join(line) for line in matrix]))
	count = part_one()
	print(f"Count: {count}")

	count = part_two()
	print(f"Count: {count}")

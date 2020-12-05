#!/usr/bin/python3

import os

def get_id(row, col):
	return row * 8 + col


def process_col_letter(letter, col_range):
	range_size = col_range[1]-col_range[0]+1

	if letter == "L":
		return (col_range[0], col_range[1]-range_size/2)
	elif letter == "R":
		return (col_range[0]+range_size/2, col_range[1])


def process_row_letter(letter, row_range):
	range_size = row_range[1]-row_range[0]+1

	if letter == "F":
		return (row_range[0], row_range[1]-range_size/2)
	elif letter == "B":
		return (row_range[0]+range_size/2, row_range[1])

def get_row_col_from_pass(boarding_pass):
	row_range = (0, 127)
	col_range = (0, 7)
	for idx, letter in enumerate(boarding_pass):
		if idx < 7:
			row_range = process_row_letter(letter, row_range)
		else:
			col_range = process_col_letter(letter, col_range)
	row = row_range[0]
	col = col_range[0]
	return row, col


def part_one():
	ids = set()
	passes = {}
	for line in input_fp.readlines():
		boarding_pass = line.strip()
		row, col = get_row_col_from_pass(boarding_pass)
		pass_id = get_id(row, col)
		ids.add(pass_id)
		passes[boarding_pass] = pass_id
	print(f"MaxId: {max(ids)}")
	return ids, passes

def num_to_pass(row, col):
	row_bin_num_str = format(row, "07b")
	col_bin_num_str = format(col, "03b")
	result = ""
	for num in row_bin_num_str:
		if num == "0":
			result += "B"
		else:
			result += "F"
	for num in col_bin_num_str:
		if num == "0":
			result += "L"
		else:
			result += "R"
	return result


def part_two(ids, passes):
	missing_passes = []
	for row in range(128):
		for col in range(8):
			boarding_pass = num_to_pass(row, col)
			if boarding_pass not in passes:
				missing_passes.append(boarding_pass)

	print(missing_passes)
	for missing_pass in missing_passes:
		row, col = get_row_col_from_pass(missing_pass)
		missing_pass_id = get_id(row, col)
		if missing_pass[:-3] == "FFFFFFF" or missing_pass[:-3] == "BBBBBBB":
			print(f"ignoring missing pass {missing_pass}")
			continue
		if missing_pass_id+1 in ids and missing_pass_id-1 in ids:
			print(f"My pass is: {missing_pass_id}")


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_5/input.txt")
with open(input_path, "r") as input_fp:
	ids, passes = part_one()
	input_fp.seek(0)
	part_two(ids, passes)

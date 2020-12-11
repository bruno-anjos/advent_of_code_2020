#!/usr/bin/python3

import os

def calc_possibilities(numbers):
	possibilities = {}
	maxIdx = len(numbers)-1

	for i, number in enumerate(numbers):
		if i == maxIdx:
			break
		possible = [numbers[i+1]]
		for j in range(2, 4):
			if i + j >= maxIdx:
				break
			if numbers[i+j] - number <= 3:
				possible.append(numbers[i+j])
		possibilities[number] = possible
	return possibilities

def calc_num_possibilities(possibilities, precompiled_possibilities, number):
	poss_sum = 0
	if number not in possibilities:
		return 1
	for possible in possibilities[number]:
		if possible in precompiled_possibilities:
			poss_sum += precompiled_possibilities[possible]
		else:
			poss_sum += calc_num_possibilities(possibilities, precompiled_possibilities, possible)
	if number not in precompiled_possibilities:
		precompiled_possibilities[number] = poss_sum
	return poss_sum


def part_two(numbers):
	precompiled_possibilities = {}
	possibilities = calc_possibilities(numbers)
	print(possibilities)
	print(calc_num_possibilities(possibilities, precompiled_possibilities, 0))

def part_one(numbers):
	one_diff = 0
	three_diff = 0
	maxIdx = len(numbers)-1

	for i, number in enumerate(numbers):
		if i == maxIdx:
			break

		diff = numbers[i+1] - number
		if diff == 1:
			one_diff += 1
		elif diff == 3:
			three_diff += 1

	print(f"result: {one_diff * three_diff}")


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_10/input.txt")
with open(input_path, "r") as input_fp:
	numbers = [0]
	numbers.extend([int(line.strip()) for line in input_fp.readlines()])
	numbers.sort()
	numbers.append(numbers[-1]+3)
	part_one(numbers)
	part_two(numbers)

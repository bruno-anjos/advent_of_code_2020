#!/usr/bin/python3

import os

def proccess_last_val(numbers_to_turns, last_num):
	occurs = numbers_to_turns[last_num]
	if len(occurs) == 2:
		return occurs[1]-occurs[0]
	return 0

def add_num(numbers_to_turns, turn, num):
	if num in numbers_to_turns:
		occurs = numbers_to_turns[num]
		if len(occurs) == 2:
			occurs.pop(0)
		occurs.append(turn)
	else:
		numbers_to_turns[num] = [turn]

def part_one(initial_list):
	numbers_to_turns = {}

	for i, number in enumerate(initial_list):
		numbers_to_turns[number] = [i+1]

	last_num = initial_list[-1]
	for turn in range(len(initial_list)+1, 30000001):
		num = proccess_last_val(numbers_to_turns, last_num)
		add_num(numbers_to_turns, turn, num)
		last_num = num
		print(turn)

	print(last_num)


def load_input():
	line = input_fp.readline()
	line = line.strip()
	initial_list = [int(num) for num in line.split(",")]
	return initial_list

input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_15/input.txt")
with open(input_path, "r") as input_fp:
	initial_list = load_input()
	part_one(initial_list)
#!/usr/bin/python3

import os

def num_to_bin(num):
	return format(num, "036b")

def apply_mask(mask, num):
	result = ""
	for (mask_val, num_val) in zip(mask, num):
		val = num_val if mask_val == "X" else mask_val
		result += val
	return int(result, 2)


def part_one(instructions):
	mask = ""
	memory = {}

	for instruction in instructions:
		if instruction[INST_ID] == MASK:
			mask = instruction[VALUE]
		else:
			memory[instruction[MEM_ADDR]] = apply_mask(mask, num_to_bin(instruction[VALUE]))

	count = sum(memory.values())
	print(count)

def calculate_mem_addrs(mask, addr):
	result = ""
	for (mask_val, addr_val) in zip(mask, addr):
		val = ""
		if mask_val == "0":
			val = addr_val
		elif mask_val == "1":
			val = mask_val
		else:
			val = "X"
		result += val

	result = result[::-1]
	first = result.find("X")
	if first == -1:
		return result

	possibilities = []
	for res_val in result:
		new_possibilities = []
		vals = ["0", "1"] if res_val == "X" else [res_val]
		for val in vals:
			if len(possibilities) == 0:
				new_possibilities = vals
			for possibility in possibilities:
				new_possibilities.append(possibility+val)
		possibilities = new_possibilities

	final = []
	for possibility in possibilities:
		final.append(possibility[::-1])

	return final


def part_two(instructions):
	mask = ""
	memory = {}

	for instruction in instructions:
		if instruction[INST_ID] == MASK:
			mask = instruction[VALUE]
		else:
			bin_num = num_to_bin(int(instruction[MEM_ADDR]))
			mem_addrs = calculate_mem_addrs(mask, bin_num)
			for mem_addr in mem_addrs:
				memory[int(mem_addr, 2)] = instruction[VALUE]

	count = sum(memory.values())
	print(count)


MEM = "mem"
MASK = "mask"

MEM_ADDR = "addr"

INST_ID = "id"
VALUE = "value"

def load_input():
	instructions = []

	for line in input_fp.readlines():
		line = line.strip()
		splitted = line.split(" = ")
		left = splitted[0]
		right = splitted[1]

		if left == "mask":
			instructions.append({INST_ID: MASK, VALUE: right})
		else:
			index = left[4:-1]
			num = int(right)
			instructions.append({INST_ID: MEM, MEM_ADDR: index, VALUE: num})

	return instructions


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_14/input.txt")
with open(input_path, "r") as input_fp:
	instructions = load_input()
	part_one(instructions)
	part_two(instructions)
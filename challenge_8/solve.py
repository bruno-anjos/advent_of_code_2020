#!/usr/bin/python3

import os

def try_jumps(ops):
	tried = set()

	while True:
		ptr = 0
		acc = 0
		visited = set()
		trying = -1

		while True:
			if ptr in visited:
				break

			if ptr not in ops:
				print(f"finished")
				break

			visited.add(ptr)
			op = ops[ptr]
			opcode = op[0]
			if opcode == "acc":
				acc += int(op[1])
			elif opcode == "jmp":
				if trying == -1 and ptr not in tried:
					trying = ptr
				else:
					ptr += int(op[1])
					continue
			ptr += 1

		if len(ops)-2 in visited:
			print(f"Found switch at {trying} to nop")
			print(f"acc: {acc}")
			break
		else:
			tried.add(trying)

def try_nops(ops):
	tried = set()

	while True:
		ptr = 0
		acc = 0
		visited = set()
		trying = -1

		while True:
			if ptr in visited:
				break

			if ptr not in ops:
				print(f"finished")
				break

			visited.add(ptr)
			op = ops[ptr]
			opcode = op[0]
			if opcode == "nop":
				if trying == -1 and ptr not in tried:
					trying = ptr
					ptr += int(op[1])
					continue
			elif opcode == "acc":
				acc += int(op[1])
			elif opcode == "jmp":
				ptr += int(op[1])
				continue
			ptr += 1

		if len(ops)-2 in visited:
			print(f"Found switch at {trying} to jmp")
			print(f"acc: {acc}")
			break
		else:
			tried.add(trying)

def part_two(ops):
	ptr = 0
	visited = set()
	acc = 0
	jmps_to_try = set()
	nops_to_try = set()

	while True:
		if ptr in visited:
			break

		if ptr not in ops:
			print(f"finished")
			break

		visited.add(ptr)
		op = ops[ptr]
		opcode = op[0]
		if opcode == "nop":
			nops_to_try.add(ptr)
		elif opcode == "acc":
			acc += int(op[1])
		elif opcode == "jmp":
			jmps_to_try.add(ptr)
			ptr += int(op[1])
			continue
		ptr += 1

	try_jumps(ops)
	try_nops(ops)


	print(f"acc: {acc}")


def part_one(ops):
	ptr = 0
	visited = set()
	acc = 0
	while True:
		if ptr in visited:

			break

		visited.add(ptr)
		op = ops[ptr]
		opcode = op[0]
		if opcode == "acc":
			acc += int(op[1])
		elif opcode == "jmp":
			ptr += int(op[1])
			continue
		ptr += 1
	print(f"acc: {acc}")


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_8/input.txt")
with open(input_path, "r") as input_fp:
	ops = {}
	for idx, line in enumerate(input_fp.readlines()):
		line = line.strip()
		splits = line.split(" ")
		ops[idx] = splits

	part_one(ops)
	part_two(ops)
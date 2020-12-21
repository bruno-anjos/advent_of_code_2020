#!/usr/bin/python3

import os

def eval_exp(exp):
	while True:
		begin = exp.rfind("(")
		end = exp.find(")", begin)
		if begin != -1:
			sub_exp = exp[begin + 1:end]
			res = eval_exp(sub_exp)
			exp = exp[:begin] + str(res) + exp[end+1:]
		else:
			break

	splits = exp.split(" ")
	while "+" in splits:
		pos = splits.index("+")
		new_splits = []
		for i in range(pos-1):
			new_splits.append(splits[i])
		new_splits.append(int(splits[pos-1])+int(splits[pos+1]))
		for i in range(pos+2, len(splits)):
			new_splits.append(splits[i])
		splits = new_splits

	num_ops = len(splits) // 2
	curr_left_val = int(splits[0])
	curr_idx = 1
	for i in range(num_ops):
		op = splits[curr_idx]
		rval = splits[curr_idx+1]
		if op == "*":
			curr_left_val = curr_left_val * int(rval)
		curr_idx += 2
	return curr_left_val

def part_one(expressions):
	sum = 0
	for exp in expressions:
		sum += int(eval_exp(exp))
	print(sum)


def load_input():
	expressions = []
	for line in input_fp.readlines():
		line = line.strip()
		expressions.append(line)

	return expressions


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_18/input.txt")
with open(input_path, "r") as input_fp:
	exp = load_input()
	part_one(exp)

#!/usr/bin/python3

import os

def check_password_part_one(password, character, minOccur, maxOccur):
	count = 0
	for char in password:
		if char == character:
			count += 1
		if count > maxOccur:
			break

	return count >= minOccur and count <= maxOccur


def part_one():
	valid = []
	input_fp.seek(0)
	for line in input_fp.readlines():
		splits = line.split(": ")
		constraints = splits[0]
		password = splits[1].strip()
		constraintsSplit = constraints.split(" ")
		maxMinSplits = constraintsSplit[0].split("-")
		minOccur = int(maxMinSplits[0])
		maxOccur = int(maxMinSplits[1])
		character = constraintsSplit[1]
		if check_password_part_one(password, character, minOccur, maxOccur):
			valid.append(password)
	print(len(valid))


def check_password_part_two(password, character, firstPos, secondPos):
	firstIs = password[firstPos] == character
	secondIs = password[secondPos] == character

	return (firstIs or secondIs) and (not (firstIs and secondIs))


def part_two():
	valid = []
	input_fp.seek(0)
	for line in input_fp.readlines():
		splits = line.split(": ")
		constraints = splits[0]
		password = splits[1].strip()
		constraintsSplit = constraints.split(" ")
		posSplits = constraintsSplit[0].split("-")
		firstPos = int(posSplits[0])-1
		secondPos = int(posSplits[1])-1
		character = constraintsSplit[1]
		if check_password_part_two(password, character, firstPos, secondPos):
			valid.append(password)
	print(len(valid))


inputPath = os.path.expanduser("~/git/advent_of_code_2020/challenge_2/input.txt")
with open(inputPath, "r") as input_fp:
	part_one()
	part_two()

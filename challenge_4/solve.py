#!/usr/bin/python3

import os
import re

valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

reg = re.compile(r"[a-f0-9]+")

def validate_field(field, value):
	print(f"f: {field}, v: {value}")

	if value.isnumeric():
		numeric = True
		castval = int(value)
	else:
		numeric = False

	if field == "byr":
		return numeric and castval >= 1920 and castval <= 2002
	elif field == "iyr":
		return numeric and castval >= 2010 and castval <= 2020
	elif field == "eyr":
		return numeric and castval >= 2020 and castval <= 2030
	elif field == "hgt":
		if len(value) < 4:
			return False

		suffix = value[-2:]
		prefix = value[0:-2]

		if not prefix.isnumeric():
			return False

		prefixval = int(prefix)
		if suffix == "cm":
			return prefixval >= 150 and prefixval <= 193
		elif suffix == "in":
			return prefixval >= 59 and prefixval <=76
	elif field == "hcl":
		valid_begin = value[0] == "#" and len(value) == 7
		if not valid_begin:
			return False
		match = reg.match(value[1:])
		return valid_begin and match != None and match.span()[1] == 6
	elif field == "ecl":
		return value in valid_ecls
	elif field == "pid":
		return len(value) == 9 and numeric
	elif field == "cid":
		return True
	else:
		return False

def part_two():
	valid = 0

	curr_passport = set(mandatory_fields)
	for line in input_fp.readlines():
		line = line.strip()

		if line == "":
			print(f"Remaining: {curr_passport}")
			if check_passport(curr_passport):
				valid += 1
			curr_passport = set(mandatory_fields)
			continue

		keyvalues = line.split(" ")
		for keyval in keyvalues:
			key_val = keyval.split(":")
			key = key_val[0]
			val = key_val[1]
			if validate_field(key, val):
				curr_passport.discard(key)
			else:
				print("invalid")

	if check_passport(curr_passport):
		valid += 1

	return valid


def check_passport(curr_passport):
	if len(curr_passport) == 0 or (len(curr_passport) == 1 and "cid" in curr_passport):
		return True
	return False

def part_one():
	valid = 0

	curr_passport = set(mandatory_fields)
	for line in input_fp.readlines():
		line = line.strip()

		if line == "":
			if check_passport(curr_passport):
				valid += 1
			curr_passport = set(mandatory_fields)
			continue

		keyvalues = line.split(" ")
		for keyval in keyvalues:
			key = keyval.split(":")[0]
			curr_passport.discard(key)


	if check_passport(curr_passport):
		valid += 1

	return valid

mandatory_fields = ["byr","iyr","eyr","hgt","hcl","ecl","pid","cid"]

input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_4/input.txt")
with open(input_path, "r") as input_fp:
	valid = part_one()
	print(f"Valid: {valid}")

	input_fp.seek(0)
	valid = part_two()
	print(f"Valid: {valid}")
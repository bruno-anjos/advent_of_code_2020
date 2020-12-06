import os


def part_two():
	group_set = set()
	count = 0
	first = True

	for line in input_fp.readlines():
		line = line.strip()
		if line == "":
			first = True
			count += len(group_set)
			group_set = set()
			continue

		curr_user_set = set()
		for letter in line:
			curr_user_set.add(letter)

		if first:
			first = False
			group_set = curr_user_set
		else:
			group_set = group_set.intersection(curr_user_set)

	count += len(group_set)
	print(f"Count: {count}")


def part_one():
	answers_set = set()
	count = 0
	for line in input_fp.readlines():
		line = line.strip()
		if line == "":
			count += len(answers_set)
			answers_set = set()
			continue
		for letter in line:
			answers_set.add(letter)

	count += len(answers_set)
	print(f"Count: {count}")


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_6/input.txt")
with open(input_path, "r") as input_fp:
	part_one()
	input_fp.seek(0)
	part_two()
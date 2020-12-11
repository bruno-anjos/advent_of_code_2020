import os

def check_sum(target, preamble, preamble_set):
	for value in preamble:
		if target - value in preamble_set:
			return True
	return False


def part_one(numbers):
	preamble = (0, 24)
	ptr = 25

	while ptr < len(numbers):
		preamble_range = numbers[preamble[0]:preamble[1]+1]
		valid = check_sum(numbers[ptr], preamble_range, set(preamble_range))
		if not valid:
			print(f"First number not sum: {numbers[ptr]}")
			return numbers[ptr]
		ptr += 1
		preamble = (preamble[0]+1, preamble[1]+1)

def part_two(numbers, target):
	begin_ptr = 0
	end_ptr = 0
	curr_sum = numbers[0]
	while True:
		if curr_sum == target:
			final_range = numbers[begin_ptr: end_ptr+1]
			print(final_range)
			print(min(final_range) + max(final_range))
			break
		elif curr_sum < target:
			end_ptr += 1
			curr_sum += numbers[end_ptr]
		else:
			begin_ptr += 1
			end_ptr = begin_ptr
			curr_sum = numbers[begin_ptr]


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_9/input.txt")
with open(input_path, "r") as input_fp:
	numbers = [int(line.strip()) for line in input_fp.readlines()]
	target = part_one(numbers)
	part_two(numbers, target)
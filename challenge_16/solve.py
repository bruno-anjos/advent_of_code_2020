#!/usr/bin/python3

import os

class Rule:
	def __init__(self, rule_id, rule_ranges):
		self.rule_id = rule_id
		self.rule_ranges = rule_ranges

	def InRange(self, value):
		for rule_range in self.rule_ranges:
			(range_min, range_max) = rule_range
			if value >= range_min and value <= range_max:
				return True
		return False

def process_rule(line, rules):
	splits = line.split(": ")
	rule_id = splits[0]

	splits = splits[1].split(" or ")
	rule_ranges = []
	for raw_range in splits:
		range_split = raw_range.split("-")
		rule_range = (int(range_split[0]), int(range_split[1]))
		rule_ranges.append(rule_range)
	rules[rule_id] = (Rule(rule_id, rule_ranges))


def load_input():
	rules_header = "rules"
	my_ticket_header = "your ticket:"
	nearby_tickets_header = "nearby tickets:"

	rules = {}
	nearby_tickets = []

	reading = rules_header
	for line in input_fp.readlines():
		line = line.strip()
		if line == "":
			continue
		elif line == my_ticket_header:
			reading = my_ticket_header
			continue
		elif line == nearby_tickets_header:
			reading = nearby_tickets_header
			continue

		if reading == rules_header:
			process_rule(line, rules)
		elif reading == my_ticket_header:
			my_ticket = [int(val) for val in line.split(",")]
		else:
			nearby_tickets.append([int(val) for val in line.split(",")])

	return rules, my_ticket, nearby_tickets

def part_one(rules, my_ticket, nearby_tickets):
	valid_tickets = []
	invalid_sum = 0
	for ticket in nearby_tickets:
		invalid_ticket = False
		for val in ticket:
			num = int(val)
			invalid = True
			for rule in rules.values():
				if rule.InRange(num):
					invalid = False
					break
			if invalid:
				invalid_sum += num
				invalid_ticket = True
		if not invalid_ticket:
			valid_tickets.append(ticket)

	print(invalid_sum)
	return valid_tickets


def build_possibilities(rules, valid_tickets):
	cols = len(valid_tickets[0])
	possibilities = {}
	for col in range(cols):
		possibilities[col] = rules.keys()

	return possibilities


def get_col_to_reduce(possibilities, reduced_cols):
	reduced_col = -1
	all_size_one = True

	for col, possibility in possibilities.items():
		if len(possibility) != 1:
			print(f"{col} size != 1")
			all_size_one = False
			continue
		if col in reduced_cols:
			print(f"{col} in reduced")
			continue
		if reduced_col == -1:
			reduced_col = col
			reduced_cols.add(reduced_col)

	return reduced_col, all_size_one

def part_two(rules, my_ticket, valid_tickets):
	possibilities = build_possibilities(rules, valid_tickets)

	for valid_ticket in valid_tickets:
		for col, num in enumerate(valid_ticket):
			new_possibilities = []
			for possibility in possibilities[col]:
				if rules[possibility].InRange(num):
					new_possibilities.append(possibility)
			possibilities[col] = new_possibilities

	all_size_one = False
	reduced_cols = set()
	while not all_size_one:
		reduced_col, all_size_one = get_col_to_reduce(possibilities, reduced_cols)
		if all_size_one:
			print("all size one")
			break

		removing = possibilities[reduced_col][0]
		print(f"reducing {reduced_col}")
		for col in possibilities:
			if col == reduced_col:
				continue
			if removing in possibilities[col]:
				possibilities[col].remove(removing)

	result = 1
	for col, possibility in possibilities.items():
		if "departure" in possibility[0]:
			result *= my_ticket[col]

	print(possibilities)
	print(result)


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_16/input.txt")
with open(input_path, "r") as input_fp:
	rules, my_ticket, nearby_tickets = load_input()
	valid_tickets = part_one(rules, my_ticket, nearby_tickets)
	valid_tickets.append(my_ticket)
	part_two(rules, my_ticket, valid_tickets)

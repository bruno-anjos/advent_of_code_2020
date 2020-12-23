#!/usr/bin/python3

import os

class SimpleRule():
	def __init__(self, rule_nr, text):
		self.text = text
		self.rule_nr = rule_nr
		print(f"SimpleRule: {text}")
	def eval(self, rules, texts):
		possibilities = []
		for text in texts:
			if text[:len(self.text)] == self.text:
				curr_text = text[len(self.text):]
				possibilities.append(curr_text)
		return possibilities


class PipeRule():
	def __init__(self, rule_nr, left_side, right_side):
		self.left_side = left_side
		self.right_side = right_side
		self.rule_nr = rule_nr
		print(f"PipeRule: {left_side}, {right_side}")
	def eval(self, rules, texts):
		possibilities = texts
		for rule_nr in self.left_side:
			rule = rules[rule_nr]
			possibilities = rule.eval(rules, possibilities)
			if len(possibilities) == 0:
				break

		new_possibilities = possibilities
		possibilities = texts

		for rule_nr in self.right_side:
			rule = rules[rule_nr]
			possibilities = rule.eval(rules, possibilities)
			if len(possibilities) == 0:
				break

		new_possibilities.extend(possibilities)
		return new_possibilities


class ComposedRule():
	def __init__(self, rule_nr, rule_nrs):
		self.rule_nrs = rule_nrs
		self.rule_nr = rule_nr
		print(f"ComposedRule: {rule_nrs}")
	def eval(self, rules, texts):
		possibilities = texts

		for rule_nr in self.rule_nrs:
			rule = rules[rule_nr]
			possibilities = rule.eval(rules, possibilities)
			if len(possibilities) == 0:
				break

		return possibilities


def parse_basic_rule(rule_nr, text):
	return SimpleRule(rule_nr, text[1:-1])


def parse_pipe_rule(rule_nr, text):
	splits = text.split(" | ")
	left_side = [int(rule_nr) for rule_nr in splits[0].split(" ")]
	right_side = [int(rule_nr) for rule_nr in splits[1].split(" ")]
	return PipeRule(rule_nr, left_side, right_side)


def parse_composed_rule(rule_nr, text):
	return ComposedRule(rule_nr, [int(rule_nr) for rule_nr in text.split(" ")])


def load_input():
	rules = {}
	input_lines = []
	read_rules = True

	for line in input_fp.readlines():
		line = line.strip()
		if line == "":
			read_rules = False
			continue

		if read_rules:
			splits = line.split(": ")
			rule_nr = int(splits[0])

			if '"' in splits[1]:
				rules[rule_nr] = parse_basic_rule(rule_nr, splits[1])
			elif '|' in splits[1]:
				rules[rule_nr] = parse_pipe_rule(rule_nr, splits[1])
			else:
				rules[rule_nr] = parse_composed_rule(rule_nr, splits[1])
		else:
			input_lines.append(line)

	return rules, input_lines


def part_one(rules, input_lines):
	match_zero = 0
	for line in input_lines:
		possibilities = rules[0].eval(rules, [line])
		print(f"Line: {line}, {possibilities}")
		if len(possibilities) > 0:
			match_zero += 1
	print(match_zero)


def part_two(rules, input_lines):
	rules[8] = PipeRule(8, [42], [42, 8])
	rules[11] = PipeRule(11, [42, 31], [42, 11, 31])

	match_zero = 0

	for line in input_lines:
		possibilities = rules[0].eval(rules, [line])
		print(f"Line: {line}, {possibilities}")
		if '' in possibilities:
			match_zero += 1
	print(match_zero)


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_19/input.txt")
with open(input_path, "r") as input_fp:
	rules, input_lines = load_input()
	part_one(rules, input_lines)
	part_two(rules, input_lines)
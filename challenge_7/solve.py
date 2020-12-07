#!/usr/bin/python3

import os

def part_one(inner_to_outer):
	bag = "shiny gold"
	toExplore = [bag]
	explored = set()
	containing = set()
	
	while len(toExplore) > 0:
		bag = toExplore.pop()
		if bag in explored:
			continue
		if bag not in inner_to_outer:
			continue
		outer_bags = inner_to_outer[bag]
		for outer_bag in outer_bags:
			toExplore.append(outer_bag)
			containing.add(outer_bag)
		explored.add(bag)
	print(containing)
	print(len(containing))


def explore_bag(outer_to_inner, bag):
	if bag not in outer_to_inner:
		print(f"{bag} has no children")
		return 1
	print(f"exploring {bag}")
	inner_bags = outer_to_inner[bag]
	inner_bag_count = 0
	for multiplier, inner_bag in inner_bags:
		print(f"will explore {inner_bag} * {multiplier}")
		inner_bag_count += multiplier * explore_bag(outer_to_inner, inner_bag)
	return 1 + inner_bag_count


def part_two(outer_to_inner):
	bag = "shiny gold"
	print(explore_bag(outer_to_inner, bag)-1)


def load_input():
	inner_to_outer = {}
	outer_to_inner = {}
	for line in input_fp.readlines():
		line = line.strip()
		
		outermost_innermosts = line.split(" contain ")

		outermost = outermost_innermosts[0]
		index_to_cut = outermost.find("bag")
		outermost = outermost[:index_to_cut].strip()

		innermosts_split = outermost_innermosts[1].split(",")
		if innermosts_split[0].strip() == "no other bags.":
			continue
		outer_to_inner[outermost] = []
		for innermost in innermosts_split:
			innermost = innermost.strip()
			begin_to_cut = innermost.find(" ")
			end_to_cut = innermost.find("bag")
			multiplier = int(innermost[:begin_to_cut])
			innermost = innermost[begin_to_cut+1:end_to_cut].strip()
			if innermost in inner_to_outer:
				inner_to_outer[innermost].append(outermost)
			else:
				inner_to_outer[innermost] = [outermost]
			outer_to_inner[outermost].append((multiplier, innermost))

	return inner_to_outer, outer_to_inner


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_7/input.txt")
with open(input_path, "r") as input_fp:
	inner_to_outer, outer_to_inner = load_input()
	part_one(inner_to_outer)
	part_two(outer_to_inner)
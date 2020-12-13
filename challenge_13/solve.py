#!/usr/bin/python3

import os
import math
import sympy.ntheory.modular

def part_one(first_timestamp, bus_ids):
	best_id = bus_ids[0]
	best_diff = -1

	for bus_id in bus_ids:
		quotient = first_timestamp // bus_id
		diff = abs(bus_id * (quotient+1) - first_timestamp)
		if diff < best_diff or best_diff == -1:
			best_diff = diff
			best_id = bus_id

	print(f"Result: {best_diff *  best_id}")

def part_two(first_timestamp, bus_ids):
	bus_mods = {}
	for idx, bus_id in enumerate(bus_ids):
		if bus_id == 'x':
			continue
		bus_id_int = int(bus_id)
		bus_mods[bus_id_int] = (bus_id_int - idx) % bus_id_int
	  
	result = sympy.ntheory.modular.crt(bus_mods.keys(), bus_mods.values())
	print(f"Result: {result}")

input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_13/input.txt")
with open(input_path, "r") as input_fp:
	first_timestamp = int(input_fp.readline().strip())
	bus_ids = [bus_id for bus_id in input_fp.readline().strip().split(",")]
	bus_ids_cleaned = [int(bus_id) for bus_id in bus_ids if bus_id != "x"]
	part_one(first_timestamp, bus_ids_cleaned)
	part_two(first_timestamp, bus_ids)
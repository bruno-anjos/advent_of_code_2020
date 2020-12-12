#!/usr/bin/python3

import os
from copy import copy, deepcopy

def update_seat_part_one(i, j, seat_grid):
	seat = seat_grid[i][j]

	if seat == ".":
		return ".", False

	adjacents = 0
	min_i = i-1 if i-1 >= 0 else i
	max_i = i+1 if i+1 < len(seat_grid) else i
	min_j = j-1 if j-1 >= 0 else j
	max_j = j+1 if j+1 < len(seat_grid[0]) else j

	for aux_i in range(min_i, max_i+1):
		for aux_j in range(min_j, max_j+1):
			if aux_i == i and aux_j == j:
				continue
			if seat_grid[aux_i][aux_j] == "#":
				adjacents += 1

	if seat == "L" and adjacents == 0:
		return "#", True
	elif seat == "#" and adjacents >= 4:
		return "L", True
	else:
		return seat, False



def part_one(seat_grid):
	old_seat_grid = deepcopy(seat_grid)
	while True:
		changed = False
		for i, seat_line in enumerate(old_seat_grid):
			for j, seat in enumerate(seat_line):
				new_seat, changed_seat = update_seat_part_one(i, j, old_seat_grid)
				if changed_seat:
					changed = True
				new_list = list(seat_grid[i])
				new_list[j] = new_seat
				seat_grid[i] = "".join(new_list)

		if not changed:
			break

		aux_grid = old_seat_grid
		old_seat_grid = seat_grid
		seat_grid = aux_grid

	occupied = 0
	for seat_line in seat_grid:
		for seat in seat_line:
			if seat == "#":
				occupied += 1

	print(f"occupied: {occupied}")

def update_seat_part_two(i, j, seat_grid):
	seat = seat_grid[i][j]

	max_row = len(seat_grid)-1
	max_col = len(seat_grid[0])-1

	if seat == ".":
		return ".", False

	adjacents = 0
	for i_var in range(-1, 2):
		for j_var in range(-1, 2):
			if i_var == 0 and j_var == 0:
				continue
			attempt = 1
			while True:
				aux_i = i + i_var * attempt
				aux_j = j + j_var * attempt
				if aux_i >= 0 and aux_i <= max_row and \
					aux_j >= 0 and aux_j <= max_col:
					adj = seat_grid[aux_i][aux_j]
					if adj == ".":
						attempt += 1
						continue
					
					if adj == "#":
						adjacents += 1
				break

	if seat == "L" and adjacents == 0:
		return "#", True
	elif seat == "#" and adjacents >= 5:
		return "L", True
	else:
		return seat, False

def part_two(seat_grid):
	old_seat_grid = deepcopy(seat_grid)

	while True:
		changed = False
		for i, seat_line in enumerate(old_seat_grid):
			for j, seat in enumerate(seat_line):
				new_seat, changed_seat = update_seat_part_two(i, j, old_seat_grid)
				if changed_seat:
					changed = True
				new_list = list(seat_grid[i])
				new_list[j] = new_seat
				seat_grid[i] = "".join(new_list)

		if not changed:
			break

		aux_grid = old_seat_grid
		old_seat_grid = seat_grid
		seat_grid = aux_grid

	occupied = 0
	for seat_line in seat_grid:
		for seat in seat_line:
			if seat == "#":
				occupied += 1

	print(f"occupied: {occupied}")


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_11/input.txt")
with open(input_path, "r") as input_fp:
	seat_grid = [line.strip() for line in input_fp.readlines()]
	part_one(deepcopy(seat_grid))
	part_two(seat_grid)

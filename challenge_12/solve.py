#!/usr/bin/python3

import os

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

VERTICAL = "vertical"
HORIZONTAL = "horizontal"
FACING = "facing"

def execute_move_part_one(move, value, state):
	if move == "N":
		state[VERTICAL] += value
	elif move == "S":
		state[VERTICAL] -= value
	elif move == "E":
		state[HORIZONTAL] += value
	elif move == "W":
		state[HORIZONTAL] -= value
	elif move == "R":
		state[FACING] = (state[FACING] + (value // 90)) % 4
	elif move == "L":
		state[FACING] = (state[FACING] - (value // 90)) % 4
	elif move == "F":
		if state[FACING] == NORTH:
			state[VERTICAL] += value
		elif state[FACING] == SOUTH:
			state[VERTICAL] -= value
		elif state[FACING] == EAST:
			state[HORIZONTAL] += value
		elif state[FACING] == WEST:
			state[HORIZONTAL] -= value


def part_one(moves):
	state = {
		VERTICAL: 0,
		HORIZONTAL: 0,
		FACING: EAST,
	}

	for (move, value) in moves:
		execute_move_part_one(move, value, state)

	print(f"Result: {abs(state[VERTICAL]) + abs(state[HORIZONTAL])}")


VERTICAL_DELTA = "v_delta"
HORIZONTAL_DELTA = "h_delta"
SHIP = "ship"
WAYPOINT = "waypoint"
QUADRANT = 0

def rotate(waypoint, rotations):
	real_rotations = rotations % 4
	for rotation in range(real_rotations):
		h_delta = waypoint[HORIZONTAL_DELTA]
		v_delta = waypoint[VERTICAL_DELTA]
		waypoint[HORIZONTAL_DELTA] = v_delta
		waypoint[VERTICAL_DELTA] = -h_delta
		waypoint[QUADRANT] = (waypoint[QUADRANT] + 1) % 4


def execute_move_part_two(move, value, ship, waypoint):
	if move == "N":
		waypoint[VERTICAL_DELTA] += value
	elif move == "S":
		waypoint[VERTICAL_DELTA] -= value
	elif move == "E":
		waypoint[HORIZONTAL_DELTA] += value
	elif move == "W":
		waypoint[HORIZONTAL_DELTA] -= value
	elif move == "R":
		rotate(waypoint, (value // 90))
		return
	elif move == "L":
		rotate(waypoint, -(value // 90))
		return
	elif move == "F":
		for i in range(value):
			ship[VERTICAL] += waypoint[VERTICAL_DELTA]
			ship[HORIZONTAL] += waypoint[HORIZONTAL_DELTA]
		return
	h_delta = waypoint[HORIZONTAL_DELTA]
	v_delta = waypoint[VERTICAL_DELTA]
	quadrant = 0
	if h_delta >= 0 and v_delta < 0:
		quadrant = 1
	elif h_delta < 0 and v_delta < 0:
		quadrant = 2
	elif h_delta < 0 and v_delta >= 0:
		quadrant = 3
	waypoint[QUADRANT] = quadrant



def part_two(moves):
	ship = {
		VERTICAL: 0,
		HORIZONTAL: 0,
	}

	waypoint = {
		VERTICAL_DELTA: 1,
		HORIZONTAL_DELTA: 10,
		QUADRANT: 0
	}

	for (move, value) in moves:
		execute_move_part_two(move, value, ship, waypoint)

	print(f"Result: {abs(ship[VERTICAL]) + abs(ship[HORIZONTAL])}")

input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_12/input.txt")
with open(input_path, "r") as input_fp:
	moves = []
	for line in input_fp.readlines():
		line = line.strip()
		move = line[:1]
		value = int(line[1:])
		moves.append((move, value))
	part_one(moves)
	part_two(moves)
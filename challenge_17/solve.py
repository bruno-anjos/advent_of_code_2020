#!/usr/bin/python3

import os
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

def load_input():
	values_matrix = []
	for line in input_fp.readlines():
		line = line.strip()
		values_matrix.append(line)

	return values_matrix

def get_neighbors(matrix, pos, size):
	(initial_i, initial_j, initial_z) = pos
	active = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			for z in range(-1, 2):
				curr_i = initial_i + i
				curr_j = initial_j + j
				curr_z = initial_z + z
				if curr_i == initial_i and curr_j == initial_j and curr_z == initial_z:
					continue
				if curr_i >= size or curr_i < 0:
					continue
				if curr_j >= size or curr_j < 0:
					continue
				if curr_z >= size or curr_z < 0:
					continue

				if matrix[curr_i, curr_j, curr_z] == "#":
					active += 1

	return active

def update_matrix(matrix, size):
	new_matrix = np.full((size, size, size), ".")
	for i in range(size):
		for j in range(size):
			for z in range(size):
				char = matrix[i, j, z]
				active = get_neighbors(matrix, (i, j, z), size)
				if char == ".":
					if active == 3:
						new_matrix[i, j, z] = "#"
					else:
						new_matrix[i, j, z] = "."
				else:
					if active == 2 or active == 3:
						new_matrix[i, j, z] = "#"
					else:
						new_matrix[i, j, z] = "."
	return new_matrix


def part_one(values_matrix, num_cycles):
	size = num_cycles*2+len(values_matrix)*2
	matrix = np.full((size, size, size), ".")
	mid = size//2
	for i, value_line in enumerate(values_matrix):
		for j, char in enumerate(value_line):
			matrix[mid+i, mid+j, mid] = char

	for i in range(num_cycles):
		matrix = update_matrix(matrix, size)

	active = 0
	for i in range(size):
		for j in range(size):
			for z in range(size):
				if matrix[i, j, z] == "#":
					active += 1
	print(active)

def get_neighbors_pt_two(matrix, pos, size):
	(initial_i, initial_j, initial_z, initial_w) = pos
	active = 0
	for i in range(-1, 2):
		for j in range(-1, 2):
			for z in range(-1, 2):
				for w in range(-1, 2):
					curr_i = initial_i + i
					curr_j = initial_j + j
					curr_z = initial_z + z
					curr_w = initial_w + w
					if curr_i == initial_i and curr_j == initial_j and curr_z == initial_z and curr_w == initial_w:
						continue
					if curr_i >= size or curr_i < 0:
						continue
					if curr_j >= size or curr_j < 0:
						continue
					if curr_z >= size or curr_z < 0:
						continue
					if curr_w >= size or curr_w < 0:
						continue

					if matrix[curr_i, curr_j, curr_z, curr_w] == "#":
						active += 1

	return active

def update_matrix_pt_two(matrix, size):
	new_matrix = np.full((size, size, size, size), ".")
	for i in range(size):
		for j in range(size):
			for z in range(size):
				for w in range(size):
					char = matrix[i, j, z, w]
					active = get_neighbors_pt_two(matrix, (i, j, z, w), size)
					if char == ".":
						if active == 3:
							new_matrix[i, j, z, w] = "#"
						else:
							new_matrix[i, j, z, w] = "."
					else:
						if active == 2 or active == 3:
							new_matrix[i, j, z, w] = "#"
						else:
							new_matrix[i, j, z, w] = "."
	return new_matrix


def part_two(values_matrix, num_cycles):
	size = num_cycles*2+len(values_matrix)*2
	matrix = np.full((size, size, size, size), ".")
	mid = size//2
	for i, value_line in enumerate(values_matrix):
		for j, char in enumerate(value_line):
			matrix[mid+i, mid+j, mid, mid] = char

	for i in range(num_cycles):
		print(f"cycle {i}")
		matrix = update_matrix_pt_two(matrix, size)

	active = 0
	for i in range(size):
		for j in range(size):
			for z in range(size):
				for w in range(size):
					if matrix[i, j, z, w] == "#":
						active += 1
	print(active)


input_path = os.path.expanduser("~/git/advent_of_code_2020/challenge_17/input.txt")
with open(input_path, "r") as input_fp:
	matrix = load_input()
	part_one(matrix, 6)
	part_two(matrix, 6)
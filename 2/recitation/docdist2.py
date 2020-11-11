#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys, math
import cProfile

def word_frequencies_for_file(filename):
	line_list = []
	word_list = []
	freq_mapping = []
	freq = []
	with open(filename, 'r') as f:
		line_list = f.readlines()
		word_list = get_words_from_line_list(line_list)
		freq_mapping = count_frequency(word_list)
	return freq_mapping

def get_words_from_line_list(L):
	word_list = []
	for line in L:
		words_in_line = get_words_from_string(line)
		word_list.extend(words_in_line)
	return word_list

def get_words_from_string(line):
	word_list = []
	character_list = []
	for c in line:
		if c.isalnum():
			character_list.append(c)
		elif len(character_list) > 0:
			word = ''.join(character_list)
			word = word.lower()
			word_list.append(word)
			character_list = []
	
	if len(character_list) >0:
		word = ''.join(character_list)
		word = word.lower()
		word_list.append(word)
	return word_list

def count_frequency(word_list):
	L = []
	for new_word in word_list:
		# Loop statements may have an else clause
		for entry in L:
			if new_word == entry[0]:
				entry[1] = entry[1] +1
				break
		else:
			L.append([new_word, 1])
	return L

def vector_angle(L1, L2):
	numerator = inner_product(L1, L2)
	denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
	return math.acos(numerator/ denominator)

def inner_product(L1, L2):
	sum =0.0
	for word1, count1 in L1:
		for word2, count2 in L2:
			if word1 == word2:
				sum += count1 * count2
	return sum

def main():
	if len(sys.argv) != 3:
			print('Usuage: python docdist2.py filename_1 filename_2')
			exit()
	else:
		filename_1 = sys.argv[1]
		filename_2 = sys.argv[2]
		sorted_word_list_1 = word_frequencies_for_file(filename_1)
		sorted_word_list_2 = word_frequencies_for_file(filename_2)
		distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
		print("The distance between the documents is: %0.6f (radians)" % distance)

if __name__ == '__main__':
	cProfile.run('main()')
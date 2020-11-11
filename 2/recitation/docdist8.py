#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys, math
import cProfile
import string

translation_table = str.maketrans(string.punctuation + string.ascii_uppercase, ' '* len(string.punctuation) + string.ascii_lowercase)

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

def merge_sort(A):
	n = len(A)
	if n==1:
		return A
	mid = n //2
	L = merge_sort(A[:mid])
	R = merge_sort(A[mid:])
	return merge(L, R)

def merge(L, R):
	i = 0
	j = 0
	answer = []
	while i < len(L) and j < len(R):
		if L[i] < R[j]:
			answer.append(L[i])
			i += 1
		else:
			answer.append(R[j])
			j += 1
	if i < len(L):
		answer.extend(L[i:])
	if j < len(R):
		answer.extend(R[j:])
	return answer

def get_words_from_line_list(line):
	line = line[0].translate(translation_table)
	word_list = line.split()
	return word_list

def get_words_from_string(line):
	translation_table =string
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
	D = {}
	for new_word in word_list:
		if new_word in D:
			D[new_word] = D[new_word] +1
		else:
			D[new_word] = 1
	return D

def vector_angle(L1, L2):
	numerator = inner_product(L1, L2)
	denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
	return math.acos(numerator/ denominator)

def inner_product(L1, L2):
	sum =0.0
	for key in L1:
		if key in L2:
			sum += L1[key] * L2[key]
	return sum
	
def main():
	if len(sys.argv) != 3:
			print('Usuage: python docdist6.py filename_1 filename_2')
			exit()
	else:
		filename_1 = sys.argv[1]
		filename_2 = sys.argv[2]
		sorted_word_list_1 = word_frequencies_for_file(filename_1)
		sorted_word_list_2 = word_frequencies_for_file(filename_2)
		distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
		print("The distance between the documents is: %0.6f (radians)" % distance)

def get_words_from_text(text):
	text = text.translate(translation_table)
	word_list = text.split()
	return word_list



if __name__ == '__main__':
	cProfile.run('main()')
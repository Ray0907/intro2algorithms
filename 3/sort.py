#!/usr/bin/python3
# -*- coding: utf-8 -*-

def insertionSort(items):
	for index, value in enumerate(items):
		privot = index
		tmp =0
		while(privot > 0 and items[privot] < items[privot-1]):
			tmp = items[privot -1]
			items[privot -1 ] = items[privot]
			items[privot] = tmp
			privot = privot -1

	return items

def mergeSort(items):
	# privot = int(len(items)/2) -1
	mid = len(items) //2

	L = items[:mid]
	R = items[mid:]
	print(L,'\n',R)


if __name__ == '__main__':
	arr = [11, 7, 6, 10, 9, 28, 77]
	# arr = insertionSort(arr)
	mergeSort(arr)

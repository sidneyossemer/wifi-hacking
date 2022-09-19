#!/usr/bin/env python3

import sys
import string
import datetime
import re
from unicodedata import normalize
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-w", "--input", help="Base words")
parser.add_argument("-o", "--output", help="Output file")
parser.add_argument("-c", "--complexity", help="Complexity level")
parser.add_argument("-n", "--nRange", help="Range of numbers to combine")
args = parser.parse_args()

if (args.input == None):
	print('\nOptions:\n\t-w\tInput wordlist (Required)\n\t-o\tOutput wordlist. (If omitted: wordlist.txt)\n\t-n\tRange of numbers to combine. (If omitted: 1000)\n\t-c\tComplexity level: (If omitted: 1)\n\t\t0: Fast\n\t\t1: Normal\n\t\t2: Complex\n\t\t3: Aggressive\n\t\t4: Insane\n')
	print('Usage:\n\tpython '+sys.argv[0]+' -w words.txt\n\tpython '+sys.argv[0]+' -w words.txt -c 2\n\tpython '+sys.argv[0]+' -w words.txt -c 4 -n 20\n\tpython '+sys.argv[0]+' -w words.txt -o output.txt\n\tpython '+sys.argv[0]+' -w words.txt -c 3 -o output.txt')
	exit()
if (args.output == None):
	args.output = "wordlist.txt"
if (args.complexity == None or int(args.complexity) not in range(0, 5)):
	args.complexity = int(1)
if (args.nRange == None):
	args.nRange = int(1000)

dic = {'aioO':'@100','aeioOs':'43100$','aeiou':'AEIOU','IilLsS':'1111$$'}
wordlist = open(args.output, 'w')
date = datetime.datetime.now()

def function_2 (word):
	for l in range(int(args.nRange) + 1):
		wordlist.write(word+str(l)+'\n')
		wordlist.write(word+'@'+str(l)+'\n')

def function_1 (line):
	for i in dic:
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])))
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i]))+'@'+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).upper())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).upper()+'@'+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).lower())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).lower()+'@'+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).capitalize())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).capitalize()+'@'+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).title())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).title()+'@'+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+'\n')
		function_2(line.translate(str.maketrans(i,dic[i])).swapcase())
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,dic[i])).swapcase()+'@'+str(date.year)+'\n')

def main():
	print( f"{date:%Y-%m-%d %H:%M:%S}"+"\tProcess started")
	with open(args.input) as file:
		for t in file:
			linha = t.rstrip('\n')
			function_1(linha)
	wordlist.close()
	print( f"{date:%Y-%m-%d %H:%M:%S}"+"\tProcess finished. File "+args.output+" saved.")

if __name__ == '__main__':
  main()

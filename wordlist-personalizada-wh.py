#!/usr/bin/env python3
# Improvements made by @sidneyossemer / @hal0x9k
## Interactive mode added
## Updated swap characters dictionary
## Updated combinations set

import sys
import string
import datetime
import re
from unicodedata import normalize
import argparse
import os

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

swaps = {'aaeil':'4@311', 'uwm':'vmw', 'ogtssz':'067$52', '12334567890':'izebasgtbgo'}
chars = {'!', '@', '#', '$', '%', '&', '*', '(', ')', '_', '+', '-', '=', '[', ']', '{', '}', '/', '.', '|', '\\', '?', ',', ';', ':', '<', '>'}

wordlist = open(args.output, 'w')
date = datetime.datetime.now()

def removeDuplicates():
	lines_seen = set()
	cleanFile = open("clean.txt", "w")

	for line in open(str(args.output), "r"):
		if line not in lines_seen:
			cleanFile.write(line)
			lines_seen.add(line)
	cleanFile.close()

def combinations (word):
	for l in range(int(args.nRange) + 1):
            wordlist.write(word+str(l)+'\n')
            wordlist.write(str(l)+word+'\n')
            for c in chars:
                wordlist.write(word+c+'\n')
                wordlist.write(c+word+'\n')
                if (int(args.complexity) > 0):
                    wordlist.write(word+c+str(l)+'\n')
                    wordlist.write(word+str(l)+c+'\n')
                    wordlist.write(c+word+str(l)+'\n')
                    wordlist.write(c+str(l)+word+'\n')
                    wordlist.write(str(l)+word+c+'\n')
                    wordlist.write(str(l)+c+word+'\n')
                    if (int(args.complexity) > 1):
                        for c2 in chars:
                            wordlist.write(c+word+c2+'\n')
                            wordlist.write(c+word+c2+str(l)+'\n') 
                            wordlist.write(c+word+str(l)+c2+'\n')
                            wordlist.write(c+str(l)+word+c2+'\n') 
                            wordlist.write(c2+word+c+'\n')
                            wordlist.write(c2+word+c+str(l)+'\n')
                            wordlist.write(c2+word+str(l)+c+'\n')
                            wordlist.write(c2+str(l)+word+c+'\n')
                        if (int(args.complexity) > 2):
                            wordlist.write(str(l)+c+word+c2+str(l)+'\n') 
                            wordlist.write(str(l)+c+word+str(l)+c2+'\n') 
                            wordlist.write(str(l)+c2+word+c+str(l)+'\n')
                            wordlist.write(str(l)+c2+word+str(l)+c+'\n')
                            wordlist.write(c+str(l)+word+c2+str(l)+'\n') 
                            wordlist.write(c+str(l)+word+str(l)+c2+'\n') 
                            wordlist.write(c2+str(l)+word+c+str(l)+'\n')
                            wordlist.write(c2+str(l)+word+str(l)+c+'\n')
                        if (int(args.complexity) > 3):
                            for c3 in chars:
                                wordlist.write(c+str(l)+c2+word+str(l)+c3+'\n')
                                wordlist.write(c+str(l)+c3+word+str(l)+c2+'\n')
                                wordlist.write(c+str(l)+c2+word+c3+str(l)+'\n')
                                wordlist.write(c+str(l)+c3+word+c2+str(l)+'\n')
                                wordlist.write(c2+str(l)+c+word+str(l)+c3+'\n')
                                wordlist.write(c2+str(l)+c+word+c3+str(l)+'\n')
                                wordlist.write(c2+str(l)+c3+word+c+str(l)+'\n')
                                wordlist.write(c2+str(l)+c3+word+str(l)+c+'\n')
                                wordlist.write(c3+str(l)+c+word+str(l)+c3+'\n')
                                wordlist.write(c3+str(l)+c+word+c2+str(l)+'\n')
                                wordlist.write(c3+str(l)+c2+word+c+str(l)+'\n')
                                wordlist.write(c3+str(l)+c3+word+str(l)+c+'\n')

def alterCases (line):
	for i in swaps:
		wordlist.write(line.translate(str.maketrans(i,swaps[i]))+'\n')
		combinations(line.translate(str.maketrans(i,swaps[i])))
		wordlist.write(line.translate(str.maketrans(i,swaps[i]))+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).upper()+'\n')
		combinations(line.translate(str.maketrans(i,swaps[i])).upper())
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).upper()+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).lower()+'\n')
		combinations(line.translate(str.maketrans(i,swaps[i])).lower())
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).lower()+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).capitalize()+'\n')
		combinations(line.translate(str.maketrans(i,swaps[i])).capitalize())
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).capitalize()+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).title()+'\n')
		combinations(line.translate(str.maketrans(i,swaps[i])).title())
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).title()+str(date.year)+'\n')
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).swapcase()+'\n')
		combinations(line.translate(str.maketrans(i,swaps[i])).swapcase())
		wordlist.write(line.translate(str.maketrans(i,swaps[i])).swapcase()+str(date.year)+'\n')

def main():
	print( f"{date:%Y-%m-%d %H:%M:%S}"+"\tProcess started")
	with open(args.input) as file:
		for t in file:
			linha = t.rstrip('\n')
			alterCases(linha)
	removeDuplicates()
	wordlist.close()
	os.remove(args.output)
	os.rename('clean.txt', args.output)
	print( f"{date:%Y-%m-%d %H:%M:%S}"+"\tProcess finished. File "+args.output+" saved.")

if __name__ == '__main__':
	main()

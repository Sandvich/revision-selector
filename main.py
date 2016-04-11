#!/usr/bin/env python 
# -*- coding: utf-8 -*-
from random import randrange

def main():
	f = open('topics', 'r')
	topics = []
	for line in f:
		for item in line.split(','):
			topics.append(item.strip())

	selection = randrange(0,len(topics))
	print "You should revise " + str(topics[selection]) + " next!"

if __name__ == '__main__':
	main()
#!/usr/bin/env python 3

import operator
import logging
import sys
#for homework, you might want 'import math', and use things in the math library in our operator dictionary

#TODO: handle divide by 0, 

logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

operators = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'%': operator.mod,
	'^': operator.pow,
	'.': operator.floordiv,
	'&': operator.and_,
	'|': operator.or_,
	'~': operator.inv,
}  

def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			function = operators[token]
			arg2 = stack.pop()
			try:
				result = function(arg2)
				stack.append(result)
			except:
				arg1 = stack.pop()
				try:
					result = function(arg1, arg2)
					stack.append(result)
				except ZeroDivisionError:
					print('Division by Zero Error')
		logger.debug(stack)

	if len(stack) != 1:
		raise TypeError

	print(result)
	return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__':
	main()

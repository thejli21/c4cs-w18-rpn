#!/usr/bin/env python3

import operator

operators = {
 '+': operator.add,
 '-': operator.sub,
 '*': operator.mul,
 '/': operator.truediv,
 '^': operator.pow,
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
   arg1 = stack.pop()
   return function(arg1, arg2)

def main():
 while True:
  print(calculate(input("rpn calc> ")))

if __name__ == '__main__':
 main()

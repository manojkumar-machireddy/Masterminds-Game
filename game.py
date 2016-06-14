#!/usr/bin/python

import random

colors = ('Red', 'Green', 'Yell', 'Blue', 'Oren', 'pink')
code = []
print colors

for i in range(4):
  x = random.randint(0,5)
  code.append(colors[x])

print code

black = 0
white = 0

guess = []
while black < 4 :
  guess = []
  code_copy = []
  black = 0
  white = 0
  for i in range(4):
    y = raw_input("Enter your guess:")
    guess.append(y)
  print guess  
  code_copy = code[:]
  for i in range(4):
    if code_copy[i] == guess[i] :
      black = black+1
      code_copy[i] = 1
      guess[i] = 0

  for i in range(4):
    for j in range(4):
      if guess[i] == code_copy[j] :
        white = white + 1
        guess[i] = 0
        code_copy[j] = 1
    
  print "The number of blacks ",black,"The number of whites ",white
  
print "You won the game!!!"  
   


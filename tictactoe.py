# 2 PLAYER TIC-TAC-TOE
# by R. Awan, February 2018
# to play, run python tictactoe.py
# todo: use socket to run over network

import os
import random

board = [" ", " ", " ",
		" ", " ", " ",
		" ", " ", " "
		]



def draw_board():
	""" draw game board """
	print " %c | %c | %c " % (board[0], board[1], board[2])
	print "___|___|___"
	print " %c | %c | %c " % (board[3], board[4], board[5])
	print "___|___|___" 
	print " %c | %c | %c " % (board[6], board[7], board[8])
	print "   |   |   "

def player_move():
	""" method containing main game loop """
	done = False
	moves = ['X', 'O']
	current_move = moves[0]
	while not done:
		# Game loop
		print "Place %c where? Choose an empty space, numbered 0-8" % (current_move)
		print "beginning in the upper left."
		draw_board()
		# raise exception
		try:
			choice = int(raw_input("> "))
		except (ValueError, TypeError, IndexError):
			print "Please type a number between 0 and 8."
			# do something here to go back to top of while loop
			continue

		if (0 <= choice <= 8) and board[choice] == " ":
			board[choice] = current_move # variable set to variable?
			draw_board()
			is_winner()
			is_draw()
			if current_move == moves[0]:
				current_move = moves[1]
			else:
				current_move = moves[0]
		else:
			print "Please type a number between 0 or 8 and choose and empty space"

def is_winner():
	pass

def is_draw():
	pass

def start_game():
	print "Welcome to 2 Player Tic-Tac-Toe!"
	print "X moves first."
	draw_board()
	player_move()

def main():
	pass

start_game()




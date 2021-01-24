'''
Tic Tac Toe App
'''

import os

# create list of winning condition
win_condition = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

# variables
board = ['#', 1, 2, 3, 4, 5, 6, 7, 8, 9]
player1_mark = ''
player2_mark = ''
turn = 1
position = 0
choice = False
is_win = False

# display the board

def show_board(board):
	print('-----')
	print(f'{board[1]}|{board[2]}|{board[3]}')
	print('-----')
	print(f'{board[4]}|{board[5]}|{board[6]}')
	print('-----')
	print(f'{board[7]}|{board[8]}|{board[9]}')
	print('-----')

# change board

def change_board(position, mark):
	board[position] = mark

# check win

def check_win(mark):
	win = False
	for a,b,c in win_condition:
		if board[a] == board[b] == board[c] == mark:
			win = True
			break
	return win

# game logic

print('Welcome to Tic Tac Toe!')

show_board(board)
while player1_mark not in ['X','O']:
	player1_mark = input('Player 1, choose mark (X/O): ')
	if player1_mark == 'X':
		player2_mark = 'O'
	else:
		player2_mark = 'X'

while True:
	os.system('cls')
	show_board(board)
	choice = False
	if turn%2 == 1:
		while not choice:
			position = int(input('Player 1, choose a position (1-9): '))
			if position not in list(range(1,10)):
				continue
			if board[position] not in ['X','O']:
				choice = True
				change_board(position, player1_mark)
				is_win = check_win(player1_mark)
			else:
				choice = False
		turn += 1
	else:
		while not choice:
			position = int(input('Player 2, choose a position (1-9): '))
			if position not in list(range(1,10)):
				continue
			if board[position] not in ['X','O']:
				choice = True
				change_board(position, player2_mark)
				is_win = check_win(player2_mark)
			else:
				choice = False
		turn += 1

	if turn == 10 and is_win == False:
		print('It is a draw!')
		break
	elif is_win == True:
		if turn%2 == 1:
			print('Player 1 wins!')
		else:
			print('Player 2 wins!')
		break
	else:
		continue

print('Thank you for playing!')

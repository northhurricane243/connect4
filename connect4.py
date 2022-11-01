#!/usr/bin/env python
import random
import math
import sys
# import test
import numpy as np
import time

### check if a move is valid
def check_move(board, turn, col, pop):
    row = int(len(board)/7)
    if col in range(7):
        if pop:
            if board[col] != turn:
                return False
            else:
                return True
        elif not pop:
            for i in range(col, row * 7, 7):
                if board[i] == 0:
                    return True
            return False
        else:
            return False
    else:
        return False

### make a move into board
def apply_move(board, turn, col, pop):
    row = int(len(board)/7)
    board_temp = board.copy()
    if not pop:
        for i in range(col, row * 7 + 1, 7):
            if board_temp[i] == 0:
                board_temp[i] = turn 
                break
    elif pop:
        for i in range(col, row * 7 - 7, 7):
            board_temp[i] = board_temp[i + 7]
        board_temp[row * 7- 7 + col] = 0
    return board_temp.copy()


### check if any 0 left in board
def check_draw(board):
    check = True
    for i in range(len(board)):
        if board[i] != 0:
            check = True
        else:
            check = False
            break
    return check


### 
def check_victory(board,  who_played: int):
    check = check_four_piece(board, who_played)
    if check == 0:
        return check
    else:
        if check_four_piece(board, - who_played + 3):
            return - who_played + 3
        else:
            return check



def check_four_piece(board, who_played):
    row = int(len(board)/7)
    for i in range(row):
        for j in range(7):
            try:
                if board[7 * i + j] == board[7 * i + j + 1] == board[7 * i + j + 2] == board[7 * i + j + 3] == who_played:
                    return who_played #horizontal check
            except IndexError:
                pass
            try: 
                if board[7 * i + j] == board[7 * (i + 1) + j] == board[7 * (i + 2) + j] == board[7 * (i + 3) + j] == who_played:
                    return who_played #vertical check
            except IndexError:
                pass
            try:
                if j <= 3:
                    if board[7 * i + j] == board[7 * (i + 1) + j + 1] == board[7 * (i + 2) + j + 2] == board[7 * (i + 3) + j + 3] == who_played:
                        return who_played #right diagonal check
            except IndexError:
                pass
            try:
                if j >= 3: 
                    if board[7 * i + j] == board[7 * (i + 1) + j - 1] == board[7 * (i + 2) + j - 2] == board[7 * (i + 3) + j - 3] == who_played:
                        return who_played #left diagonal check
            except IndexError:
                pass
    return 0


### check if a direct win move is available
def detect_victory(board, turn):
    for col in range(7):
        for pop in (True, False):
            if check_move(board, turn, col, pop):
                board_test = board.copy()
                board_test = apply_move(board_test, turn, col, pop)
                if check_victory(board_test, turn) == turn:
                    return col, pop
    return 0


def computer_level_1(board, turn):
    computer_pop = bool(random.getrandbits(1))
    computer_col = random.randrange(0, 7)
    while not check_move(board, turn, computer_col, computer_pop):
        computer_pop = bool(random.getrandbits(1))
        computer_col = random.randrange(0, 7)
    return computer_col, computer_pop


def computer_level_2(board, turn):
    opponent_turn = - turn + 3
    try:
        computer_col, computer_pop = detect_victory(board, turn)
        return computer_col, computer_pop
    except TypeError: 
        if detect_victory(board, opponent_turn) != 0:
            for col in range(7):
                for pop in (True, False):
                    board_test = board.copy()
                    if check_move(board_test, turn, col, pop):
                        board_test = apply_move(board_test, turn, col, pop)
                        if detect_victory(board_test, opponent_turn) == 0:
                            return col, pop
        rand_col, rand_pop = computer_level_1(board, turn)
        return rand_col, rand_pop


def computer_move(board, turn, level):
    if level == 1:
        return computer_level_1(board, turn)
    elif level == 2:
        return computer_level_2(board, turn)

def computer_move_display(board, turn, level):
    computer_col, computer_pop = computer_move(board, turn, level)
    print("AI level" , level, "is making a move...")
    newboard = apply_move(board, turn, computer_col, computer_pop)
    display_board(newboard)
    return newboard

        
### count timer of a turn
def countdown(t):
    while(t):
        mins, sec = divmod(60)
        timer = '{:02d}:{:02d}'.format(mins, sec)
        print(timer, end = '\r')
        time.sleep(1)
        t -= 1

    print("Time out!")
    sys.exit()

###    
def display_board(board : list):
    row = int(len(board)/7)
    print()
    for i in range(row - 1, -1, -1):
        for j in range(7):
            print(board[7 * i + j], end = ' ')
        print() 
    print()

    pass

###
def start():
    print('=== Welcome to the Connect4 game ===\nThis game was created by Monarch and Nan-fang\nNo copyright is allowed in any form.\n')
    print('1.Start the game with a computer\n2.Start the game with another player')
    pass



###
def ask_input_text(player : int):
    col = int(input("Player " + str(player) + " select column: "))
    popinput = input("Do you want to pop? (Y/N): ")
    if popinput == 'Y' or popinput == 'y':
        pop = True
    elif popinput == 'N' or popinput == 'n':
        pop = False
    return col, pop


###
def ask_input(board, player):
    col, pop = ask_input_text(player)
    while not check_move(board, player, col, pop):
        print("Invalid! Please try again. ")
        col, pop = ask_input_text(player)
    newboard = apply_move(board, player, col, pop)
    display_board(newboard)
    return newboard

### check if win/draw condition is achieved and print text
def print_result(board):
    if check_victory(board, 1) == 1:
        print("Congratulation! Player 1 has won the game!")
        return True
    elif check_victory(board, 2) == 2:
        print("Congratulation! Player 2 has won the game!")
        return True
    elif check_draw(board):
        print("The board is full! This is a draw.")
        return True
    else: 
        return False
    
### start program here
def menu():
    start()
    choice = input('> ')
    try:
        row = int(input("Enter the row numbers (by default: 6): "))
    except: 
        row = 6
    board = []
    
    ###
    for _ in range(7 * row):
        board.append(0)
    display_board(board)

    ###
    if choice == '2': 
        while True:
            board = ask_input(board, 1)
            if print_result(board):
                break
            board = ask_input(board, 2)
            if print_result(board):
                break
    ###
    elif choice == '1':
        level = int(input("Select level: 1. Easy 2. Medium "))
        computer_turn = int(input("Do you want the CPU to be Player 1 or Player 2? "))
        while True:
            if computer_turn == 1: 
                board = computer_move_display(board, computer_turn, level)
                if print_result(board):
                    break
                board = ask_input(board, 2)
            elif computer_turn == 2: 
                board = ask_input(board, 1)
                if print_result(board):
                    break
                board = computer_move_display(board, computer_turn, level)
            else: 
                print("Invalid input! The program is exiting...")
                sys.exit()
            if print_result(board):
                    break


if __name__ == "__main__":
    menu()

#!/usr/bin/env python
import random
import math
# import test

def check_move(board, turn, col, pop):
    if col in range(0, row):
        if pop:
            if board[col] != turn:
                return False
            else:
                return True
        elif not pop:
            for i in range(col, (row - 1) * 7 + col, 7):
                if board[i] == 0:
                    return True
            return False
        else:
            return False
    else:
        return False

def apply_move(board, turn, col, pop):
    if not pop:
        for i in range(col, 7 * (row - 1) + col, 7):
            if board[i] == 0:
                board[i] = turn 
                break
    elif pop:
        board[7 * (row - 1) + col] = 0
        for i in range(col, 7 * (row - 1) + col - 7, 7):
            board[i] = board[i + 7] 
    return board.copy()

def check_victory(board, who_played): #comment: there might be better solution but we are NOT computer scientists
    for i in range(row - 1, -1, -1):
        for j in range(7):
            try:
                if board[7 * i + j] == board[7 * i + j + 1] == board[7 * i + j + 2] == board[7 * i + j + 3] == who_played:
                    return who_played
                elif board[7 * i + j] == board[7 * (i + 1) + j] == board[7 * (i + 2) + j] == board[7 * (i + 3) + j] == who_played:
                    return who_played
                elif board[7 * i + j] == board[7 * (i + 1) + j + 1] == board[7 * (i + 2) + j + 2] == board[7 * (i + 3) + j + 3] == who_played:
                    return who_played
                elif board[7 * i + j] == board[7 * (i + 1) + j - 1] == board[7 * (i + 2) + j - 2] == board[7 * (i + 3) + j - 3] == who_played:
                    return who_played
                else:
                    return 0
            except IndexError:
                pass

def computer_move(board, turn, level):
    # can co 3 level dua tren doc
    #nguoi choi duoc chon level cua may tinh
    #level 1: may tinh chon column ngau nhien
    #level 2: may tinh se uu tien nuoc di tao 4 neu da co 3
    #level 3: xem doc vi no rat la phuc tap
    return (0,False)
    
def display_board(board : list):
    for i in range(row - 1, -1, -1):
        for j in range(7):
            print(board[7 * i + j], end = ' ')
        print() 
    pass

def menu():
    print('=== Welcome to the Connect4 game ===\nThis game was created by Monarch and Nan-fang\nNo copyright is allowed in any form.\n')
    print('1.Start the game with a computer\n2.Start the game with another player')
    pass

def ask_input(board, player : int):
    turn = int(input("Player " + str(player) + " select column: "))
    popinput = input("Do you want to pop? (Y/N): ")
    if popinput == 'Y' or popinput == 'y':
        pop = True
    elif popinput == 'N' or popinput == 'n':
        pop = False
    while not check_move(board, player, turn, pop):
        print("Invalid! Please try again (Y/N)")
        turn, pop = ask_input(board, 1)
    apply_move(board, player, turn, pop)
    display_board(board)
    return turn, pop

def main():
    menu()
    choice = input('> ')
    global row
    row = int(input("Enter the row numbers: "))
    board = []
    for _ in range(7 * row):
        board.append(0)
    display_board(board)
    for i in range(3):
        ask_input(board, 1)
        ask_input(board, 2)
if __name__ == "__main__":
    main()




   
    

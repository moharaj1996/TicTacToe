import random
from colorama import init, Fore, Style
import os
init(autoreset=True)

def clear():
    os.system( 'cls' )

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
used_num = []

def winner(A, player, symbol):
    if (A[0][0] == A[0][1] == A[0][2] == symbol or
            A[1][0] == A[1][1] == A[1][2] == symbol or
            A[2][0] == A[2][1] == A[2][2] == symbol or
            A[0][0] == A[1][0] == A[2][0] == symbol or
            A[0][1] == A[1][1] == A[2][1] == symbol or
            A[0][2] == A[1][2] == A[2][2] == symbol or
            A[0][0] == A[1][1] == A[2][2] == symbol or
            A[2][0] == A[1][1] == A[0][2] == symbol):
        print(player + " Wins!")
        return True

# def winner(A, player, symbol):
#     for i in range(len(A) - 1):
#         for j in range(len(A) - 1):
#
#             if (A[i][j] == A[i][j + 1] == symbol or
#                     A[i][j] == A[i + 1][j] == symbol or
#                     A[i][j] == A[i + 1][j + 1] == symbol):
#                 break
#
#     print(player + " Wins!")
#     return True


def display_board(A):
    d = 1
    for a, b, c in A:
        # if a== 'X' or b== 'X' or c== 'X':

        print('', a, '|', b, '|', c)
        if d != len(A):
            print('___|___|___')
        else:
            print('   |   |   ')
        d = d + 1


def user_num_choice(player):
    num = 0
    while num not in range(1, 10) or num in used_num:
        if player != 'computer':
            num = int(input(player + "'s Turn : "))
        else:
            num = random.randint(1, 9)
        if num not in range(1, 10) and player != 'computer':
            print("enter num between 1-9")
        elif num in used_num and player != 'computer':
            print("position occupied enter again:")
        elif num in used_num and player == 'computer':
            pass
        else:
            used_num.append(num)
            clear()
            #print('\n' * 100)
            if player == 'computer':
                print("computer :", num)
            return num


def place_symbol(num, player_turn, symbol):
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == num:
                A[i][j] = symbol
    display_board(A)
    if winner(A, player_turn, symbol) == True:
        return True


def user_sym_choice(player1, player2):
    print(player1 + " will start with X")
    print(player2 + " will follow with O")
    count = 1
    while count <= 9:
        if count % 2 != 0:
            num1 = user_num_choice(player1)
            if num1:
                if place_symbol(num1, player1, (Fore.RED + Style.BRIGHT + 'X')) == True:
                    break


        else:
            num2 = user_num_choice(player2)
            if num2:
                if place_symbol(num2, player2, (Fore.GREEN + Style.BRIGHT + '0')) == True:
                    break

        count = count + 1

    if count >= 10:
        print("Game Tied!!")


def players_name():
    pl1 = input("enter player name : ")
    pl2 = "computer"
    display_board(A)
    user_sym_choice(pl1, pl2)


players_name()

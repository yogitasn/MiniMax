from player import *
import label

import oracle

import labels

import os





def solve_game():

    print('Solving game by minimax')

    state = HexapawnState(3)

    solver = minimax.Minimax('R')

    move, score = solver.minimax(state)



    if score == float('inf'):

        print('Winner is RED player')

    else:

        print('Winner is BLUE player')





def play_game():

    state = HexapawnState(3)

    print('Select a color [r]/b?')

    player_wants_red = input() == 'r'



    if player_wants_red:

        print('You are RED')

        red = HumanPlayer('R')

        blue = BotPlayer('B')

    else:

        print('You are BLUE')

        red = BotPlayer('R')

        blue = HumanPlayer('B')



    while not state.check_gameover():

        move = red.make_move(state)

        state.make_move(move)

        state.alternate_turn()



        if state.check_gameover():

            break



        move = blue.make_move(state)

        state.make_move(move)

        state.alternate_turn()



    if state.winner == 'R':

        print('Winner is RED player')

    else:

        print('Winner is BLUE player')

    state.draw_board()





def oracle_learn():

    state = HexapawnState(5)



    red = oracle.Oracle()

    blue = oracle.Oracle()



    for i in range(100):

        while not state.check_gameover():

            move = red.consult(state)

            try:

                state.make_move(move)

                state.alternate_turn()

            except oracle.GameoverException:

                state.winner = 'B'

                red.loss(state, move)

                break



            if state.check_gameover():

                break



            move = blue.consult(state)

            try:

                state.make_move(move)

                state.alternate_turn()

            except oracle.GameoverException:

                state.winner = 'R'

                blue.loss(state, move)

                break



        if state.winner == 'R':

            print('Winner is RED player')

        else:

            print('Winner is BLUE player')

        state.draw_board()



    for state, moves in red.learned.items():

        print(state, moves, os.linesep)



    for state, moves in blue.learned.items():

        print(state, moves, os.linesep)





def main():

    print('Starting a game of Hexapawn (3x3)')

    print('RED player moves first')

    print()



    # oracle_learn()

    print('Solve for winner? [y]/n:')

    should_solve = input() == 'y'

    print()



    if should_solve:

        solve_game()

    else:

        play_game()





if __name__ == '__main__':

    main()
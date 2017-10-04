#http://www.codeskulptor.org/#user39_P2aDyECEI0_237.py
"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 200      # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player


# Add your functions here.
#PLAYERX will always be considered the Machine Player.
def mc_trial(board,player):
    """ simulates multiple games"""
    _now_playing = player
    while board.check_win() is None:
        x_ = random.randrange(board.get_dim())
        y_ = random.randrange(board.get_dim())
        if (x_,y_) in board.get_empty_squares():
            board.move(x_,y_,_now_playing)
            if board.check_win() is not None:
                break
            _now_playing = provided.switch_player(_now_playing)

def mc_update_scores(scores,board,player):
    """ updates the grid of scores """
    for _row in range(board.get_dim()):
        for _col in range(board.get_dim()):
            current_square = board.square(_row,_col)
            if board.square(_row,_col) == board.check_win():
                scores[_row][_col] = scores[_row][_col] + SCORE_CURRENT
            elif board.square(_row,_col) == provided.EMPTY:
                pass
            else:
                scores[_row][_col]= scores[_row][_col] - SCORE_OTHER



def get_best_move(board,scores):
    """ finds the best move availalbe frm the grid of scores """   
    _empty_squares = []
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            _current_square = board.square(row,col)
            if _current_square == provided.EMPTY:    
                _empty_pair = (row,col)
                _empty_squares.append(_empty_pair)
    _scores_available_list = []
    _scores_available_dict = {}
    for k_,v_ in _empty_squares:
        _value = scores[k_][v_]
        _scores_available_list.append(_value)
        _scores_available_dict[_value] = (k_,v_)
    _max_available = max(_scores_available_dict)
    _container = []
    for _each in _scores_available_list:
        if _each == _max_available:
            _container.append(_each)
    print _container
    _length = len(_container)
    _dict_choice = {}
    for i_ in range(_length):
        _dict_choice[i_] = _scores_available_dict[_container[i_]]
    print _dict_choice
    print scores
    print _dict_choice[random.randrange(_length)]
    return _dict_choice[random.randrange(_length)]
    
#    print _max_available
                
def mc_move(board,player,trials):
    """ MC uses this collection of fns to select next move """
    _rows = board.get_dim()
    _cols = board.get_dim()
    _scores_grid = []
    for dummy in range(_rows):
        current_row = []
        for dummy in range(_cols):
            current_row.append(0)
        _scores_grid.append(current_row)
    _current_player = player
    for trial in range(trials):
        _cloned_board = board.clone()
        mc_trial(_cloned_board,_current_player)
        if _cloned_board.check_win() == provided.DRAW:
            pass
        else:
            mc_update_scores(_scores_grid,_cloned_board,_current_player)
    if board.check_win() != provided.DRAW:
        return get_best_move(board,_scores_grid)

mc_move(provided.TTTBoard(3),provided.PLAYERX, NTRIALS)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)     
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

'''
print provided.EMPTY = 1
print provided.PLAYERX = 2
print provided.PLAYERO = 3
print provided.DRAW = 4
'''
#               print "row = " + str(row), "col = "+str(col), "square value = ", board.square(row,col)
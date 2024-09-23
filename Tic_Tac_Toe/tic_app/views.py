from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Initial game state
game_state = {
    'board': [['' for _ in range(3)] for _ in range(3)],
    'current_player': 'X',
    'message': 'Player X, it’s your turn!',
    'winner': None,
    'moves': 0,
}

def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

def reset_game():
    global game_state
    game_state = {
        'board': [['' for _ in range(3)] for _ in range(3)],
        'current_player': 'X',
        'message': 'Player X, it’s your turn!',
        'winner': None,
        'moves': 0,
    }

def tic_tac_toe(request):
    return render(request, 'tic_tac_toe.html', game_state)

def tic_tac_toe_move(request, row, col):
    row, col = int(row) - 1, int(col) - 1  # Convert to 0-indexed

    if game_state['board'][row][col] == '' and not game_state['winner']:
        # Make the move
        game_state['board'][row][col] = game_state['current_player']
        game_state['moves'] += 1
        
        # Check for winner
        winner = check_winner(game_state['board'])
        if winner:
            game_state['winner'] = winner
            game_state['message'] = f'Player {winner} wins!'
        elif game_state['moves'] == 9:
            game_state['message'] = 'It\'s a draw!'
        else:
            # Switch player
            game_state['current_player'] = 'O' if game_state['current_player'] == 'X' else 'X'
            game_state['message'] = f'Player {game_state["current_player"]}, it’s your turn!'
    
    return redirect('tic_tac_toe')

def tic_tac_toe_reset(request):
    reset_game()
    return redirect('tic_tac_toe')

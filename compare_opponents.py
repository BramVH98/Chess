'''
This python script checks if you and another chess.com have faced the same person/people, this assumes that you have one pgn file with all the played games stored somewhere. 
'''
import chess.pgn

def extract_rapid_opponents(pgn_file, username):
    """
    Extracts the list of unique rapid game opponents from a PGN file.
    """
    opponents = set()
    
    with open(pgn_file, 'r') as file:
        while True:
            game = chess.pgn.read_game(file)
            if game is None:
                break  # End of file
            
            # Get game details
            time_control = game.headers.get("TimeControl", "")
            white_player = game.headers.get("White", "")
            black_player = game.headers.get("Black", "")
            
            # Check if the game is a rapid game (600-1800 seconds per side)
            if time_control and time_control.isdigit():
                total_seconds = int(time_control)
                if 600 <= total_seconds <= 1800:  # Rapid time controls
                    if white_player == username:
                        opponents.add(black_player)
                    elif black_player == username:
                        opponents.add(white_player)
    
    return opponents

# Example Usage
your_pgn_file = r"<path to all games in one pgn file here>"  # Path to your downloaded PGN file
your_username = "<your username here>"

brothers_pgn_file = r"<path to all games in one pgn file here>  # Path to your brother's downloaded PGN file
brothers_username = "<username to compare to here>"

your_opponents = extract_rapid_opponents(your_pgn_file, your_username)
brothers_opponents = extract_rapid_opponents(brothers_pgn_file, brothers_username)

# Find common opponents
common_opponents = your_opponents.intersection(brothers_opponents)
print(f"Common rapid opponents: {common_opponents}")

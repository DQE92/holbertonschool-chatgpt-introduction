#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Augmenté à 9 pour mieux correspondre à la largeur

def check_winner(board):
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True
    
    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    
    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        
        # Boucle jusqu'à obtenir une entrée valide
        while True:
            try:
                row = int(input(f"Joueur {player} - Entrez la ligne (0, 1, ou 2): "))
                col = int(input(f"Joueur {player} - Entrez la colonne (0, 1, ou 2): "))
                
                if not (0 <= row <= 2 and 0 <= col <= 2):
                    print("Position invalide ! Les valeurs doivent être entre 0 et 2.")
                    continue
                    
                if board[row][col] != " ":
                    print("Cette case est déjà occupée ! Réessayez.")
                    continue
                    
                break
            except ValueError:
                print("Entrée invalide ! Veuillez entrer un nombre.")
        
        # Placer le symbole du joueur
        board[row][col] = player
        
        # Vérifier s'il y a un gagnant
        if check_winner(board):
            print_board(board)
            print(f"Le joueur {player} a gagné !")
            break
            
        # Vérifier s'il y a égalité
        if is_board_full(board):
            print_board(board)
            print("Match nul !")
            break
            
        # Changer de joueur
        player = "O" if player == "X" else "X"

tic_tac_toe()
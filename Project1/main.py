# main.py
import random
import game_logic

def main():
    game = game_logic.Game2048()
    game.display()
    
    while True:
        try:
            move = input("Enter move (W/A/S/D or Q to quit): ").strip().lower()
            if move == 'q':
                print("Game Ended. Goodbye!")
                break
            
            if move not in ['w', 'a', 's', 'd']:
                print("Invalid input. Please enter W, A, S, D, or Q to quit.")
                game.display()
                continue
            
            if not game.make_move(move):
                print("Invalid move. Try again.")
                game.display()
                continue
            
            game.display()
            
            if game.is_won():
                print("Congratulations! You won!")
                break
            elif game.is_game_over():
                print("Game Over! No more valid moves.")
                break
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()
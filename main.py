import numpy as np
import random

def print_grid(grid, reveal=False, selected=None):
    for i in range(grid.shape[0]):
        row_str = ""
        for j in range(grid.shape[1]):
            if reveal:
                row_str += "B " if grid[i, j] == 1 else ". "
            else:
                row_str += ". "
        print(row_str)
    print()

def main():
    print("Bem-vindo ao jogo da bomba!")
    grid_size = 3
    grid = np.zeros((grid_size, grid_size), dtype=int)

    # Posição aleatória da bomba
    bomb_row = random.randint(0, grid_size - 1)
    bomb_col = random.randint(0, grid_size - 1)
    grid[bomb_row, bomb_col] = 1

    score = 0
    while True:
        print_grid(grid)
        try:
            guess = input("Digite sua tentativa (linha,coluna) ou 'sair': ")
            if guess.lower() == 'sair':
                print("Jogo encerrado. Pontuação final:", score)
                print("Posição da bomba era:", (bomb_row, bomb_col))
                print("Grid revelado:")
                print_grid(grid, reveal=True)
                break
            row, col = map(int, guess.strip().split(","))
            if row < 0 or row >= grid_size or col < 0 or col >= grid_size:
                print("Posição inválida. Tente novamente.")
                continue
            if grid[row, col] == 1:
                print("BOOM! Você encontrou a bomba!")
                print("Pontuação final:", score)
                print("Grid revelado:")
                print_grid(grid, reveal=True)
                break
            else:
                print("Nada por aqui procure em outro local!")

                score += 1
        except Exception as e:
            print(f"Entrada inválida: {e}")

if __name__ == "__main__":
    main()
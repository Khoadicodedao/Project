# ─── import tkinter and random function ──────────────────────────────────────────────────────────────────────────
from tkinter import *
import random

# ─── create a 100*100 cells grid and assigned it to a variable called current_grid ──────────────────────────────────────────────────────────────────────────
current_grid = [[0]*100]*100
number_of_rows = len(current_grid)
number_of_column = len(current_grid[0])

# ─── generate random dead or alive cells in current_grid ──────────────────────────────────────────────────────────────────────────

def random_cells(grid, row, column):
    for i in range(row):
        for j in range(column):
            grid[i][j] = random.randint(0,1)
random_cells(current_grid, number_of_rows, number_of_column)


# ─── COUNT NEIBORS FUNCTION ──────────────────────────────────────────────────────────────────────────

def count_neighbors(grid , row, column):
    count = 0
    for i in (row - 1, row ,row + 1):
        if 0 <= i <= 3:
            for j in [column - 1, column , column + 1]:
                if 0 <= j <= 3 and (i,j) != (row, column) and grid[i][j] == 1:
                    count += 1
    return count


# ─── iterate through evercolumn single cells in the arracolumn and find out the current cell alive or dead
next_grid = current_grid
for e in range(number_of_rows):
    for f in range(number_of_column):
        count = count_neighbors(current_grid, e, f)
        if current_grid[e][f] == 0 and count == 3:
            next_grid[e][f] = 1
        elif (current_grid[e][f] == 1) and (count < 2 or count > 3):
            next_grid[e][f] = 0
next_grid, current_grid = current_grid, next_grid


# ─── CREATE WINDOW TITLE ────────────────────────────────────────────────────────
root = Tk()
root.title('GAME OF LIFE')
root.geometry('1920x1080')
root.configure(background='light yellow')

# ─── CREATE START BUTTON ────────────────────────────────────────────────────────
Start_button = Button(root, text='Start', bd=5, activeforeground='red',bg='green',font='Arial', width=12) 
                    
Start_button.pack(side = 'bottom') 
root.mainloop()


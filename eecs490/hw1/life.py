def printDash(length):
	for i in range(length):
		print('-', end='')
	print()

def printGrid(grid): 
	printDash(len(grid[0])+2)
	for row in grid:
		print('|', end='')
		for col in row:
			if col: print('*', end ='')
			else: print(' ', end='')
			
		print('|')
	printDash(len(grid[0])+2)
	print()

def addLiveCells(grid, live_cells):
	for live_cell in live_cells:
		grid[live_cell[0]][live_cell[1]] = 1

def findNextState(grid, nextGrid, row, col):
	alive = grid[row][col]
	liveNeighbors = 0
	for i in range(row-1, row+2):
		if i < 0 or i > len(grid)-1: 
			continue
		for j in range(col-1, col+2):

			if j < 0 or j > len(grid[0]) - 1:
				continue
			if grid[i][j] == 1:
				liveNeighbors += 1
	liveNeighbors -= grid[row][col]
	if alive:
		if not (liveNeighbors < 2 or liveNeighbors > 3):
			nextGrid[row][col] = 1
	else:
		if liveNeighbors == 3:
			nextGrid[row][col] = 1

def simulate(rows, cols, steps, live_cells):
	grid = [[0 for i in range(cols)] for j in range(rows)]
	addLiveCells(grid, live_cells)

	for i in range(steps):
		nextGrid = [[0 for i in range(cols)] for j in range(rows)]
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				findNextState(grid, nextGrid, i, j)

		printGrid(nextGrid)
		grid = list(nextGrid)

def main():
	rows = 20
	cols = 50
	steps = 20
	live_cells = ((1, 25), (2, 23), (2, 25), (3, 13), (3, 14),
	              (3, 21), (3, 22), (3, 35), (3, 36), (4, 12),
	              (4, 16), (4, 21), (4, 22), (4, 35), (4, 36),
	              (5, 1), (5, 2), (5, 11), (5, 17), (5, 21),
	              (5, 22), (6, 1), (6, 2), (6, 11), (6, 15),
	              (6, 17), (6, 18), (6, 23), (6, 25), (7, 11),
	              (7, 17), (7, 25), (8, 12), (8, 16), (9, 13),
	              (9, 14))
	simulate(rows, cols, steps, live_cells)

if __name__ == '__main__':
	main()
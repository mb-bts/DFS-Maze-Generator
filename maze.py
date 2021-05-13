import random
from PIL import Image

class Cell:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False

    def get_neighbours(self, n, cells):
        neighbours = []

        i = self.row
        j = self.col

        if i > 0 and not cells[get_index(n, i-1, j)].visited:
            top = cells[get_index(n, i-1, j)]
            neighbours.append(top)
        if j < n-1 and not cells[get_index(n, i, j+1)].visited:
            right = cells[get_index(n, i, j+1)]
            neighbours.append(right)
        if i < n-1 and not cells[get_index(n, i+1, j)].visited:
            bottom = cells[get_index(n, i+1, j)]
            neighbours.append(bottom)
        if j > 0 and not cells[get_index(n, i, j-1)].visited:
            left = cells[get_index(n, i, j-1)]
            neighbours.append(left)

        return neighbours

def initialize_cells(n):
    count = 0
    cells = []
    for i in range(n):
        for j in range(n):
            cell = Cell(i, j)
            # a value of 1 indicates that a wall is present
            cell.top = 1 if (count-n) >= 0 else None
            cell.right = 1 if (count+1) % n != 0 else None
            cell.bottom = 1 if count+(n-1) < n**2 else None
            cell.left = 1 if count % n != 0 else None
            cells.append(cell)
            count += 1

    return cells

def remove_wall(cell_1, cell_2):
    row_difference = cell_2.row - cell_1.row
    if row_difference == 1:
        # setting these values to 0 indicates that a wall is no longer present
        cell_1.bottom = cell_2.top = 0
    elif row_difference == -1:
        cell_1.top = cell_2.bottom = 0

    column_difference = cell_2.col - cell_1.col
    if column_difference == 1:
        cell_1.right = cell_2.left = 0
    elif column_difference == -1:
        cell_1.left = cell_2.right = 0

def finished(cells):
    for cell in cells:
        if cell.visited == False:
            return False
    return True

def get_index(n, i, j):
    return (i * n) + j

def get_solution(n, cells):
    solution = []
    cell = cells[-1]

    while cell.row != 0 or cell.col != 0:
        prev_i = cell.prev_row
        prev_j = cell.prev_col
        solution.append((n, prev_i, prev_j))
        diff_i = cell.row - prev_i
        diff_j = cell.col - prev_j

        if diff_i == 1:
            # 0.5 is added/subtracted because the format_maze function multiplies by 2
            solution.append((n, prev_i+0.5, prev_j))
        elif diff_i == -1:
            solution.append((n, prev_i-0.5, prev_j))

        if diff_j == 1:
            solution.append((n, prev_i, prev_j+0.5))
        elif diff_j == -1:
            solution.append((n, prev_i, prev_j-0.5))

        cell = cells[get_index(n, prev_i, prev_j)]

    return solution

def format_maze(n, cells, solution):

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (200, 50, 100)

    # each side is (2*n)+1 because walls are represented by squares of equal size to the cells
    maze = Image.new("RGB", ((2*n)+1, (2*n)+1))

    for cell in cells:

        row = cell.row*2
        col = cell.col*2

        maze.putpixel((col+1, row+1), white)

        if cell.right == 0:
            maze.putpixel((col+2, row+1), white)
        else:
            maze.putpixel((col+2, row+1), black)
        if cell.bottom == 0:
            maze.putpixel((col+1, row+2), white)
        else:
            maze.putpixel((col+1, row+2), black)

    maze.putpixel((2*n-1, 2*n-1), red)
    for cell in solution:
        maze.putpixel((int(cell[2]*2+1), int(cell[1]*2)+1), red)

    # colours the entrance and exit of the maze
    maze.putpixel((0, 1), red)
    maze.putpixel((2*n, 2*n-1), red)

    maze = maze.resize((2000, 2000), 0)
    maze.save("maze.png")

    return maze

def main():

    n = 20 # n is the number of cells in each row, where n > 1

    stack = []
    cells = initialize_cells(n)
    current = cells[0]
    current.visited = True

    while not finished(cells):
        neighbours = current.get_neighbours(n, cells)
        if len(neighbours) != 0:
            random_neighbour = random.choice(neighbours)
            stack.append(current)
            remove_wall(current, random_neighbour)
            prev = current
            current = random_neighbour
            current.visited = True
        elif len(stack) != 0:
            current = stack.pop()

        if not hasattr(current, "prev_row"):
            current.prev_row = prev.row
        if not hasattr(current, "prev_col"):
            current.prev_col = prev.col

    solution = get_solution(n, cells)

    maze = format_maze(n, cells, solution)
    maze.show()

if __name__ == "__main__":
    main()

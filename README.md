# dfs-maze-generator
In contrast to randomised versions of Kruskal's and Prim's algorithms, a randomised depth-first search generates a maze with an appropriate number of dead ends. It is this which makes these mazes appear as though they could have been designed by hand. In addition to generation, this script will show a maze's solution by backtracking from finish to start without the need for an additional search. **Here is an example:**
<p align="center"><img src="Images/Example.png" width="400"></p><br>
I’ve structured the mazes such that each equally sized square represents either empty space (0) or a wall (1). All red numbers will remain that number every time a maze is generated. All green numbers can end up being either a 1 or a 0 depending on the maze. Despite appearing to be an 11x11 maze, the maze below is actually a 5x5 where each blue square is a cell.

<br><p align="center"><img src="Images/Structured.png" width="300"> <img src="Images/StructuredLabelled.png" width="300"></p>

The exact same maze is shown below. In this case, it is clear that this is a 5x5 maze because the walls are thin. The 1s and 0s show how this maze’s structure corresponds to the one above, where the exact same sequence of 1s and 0s is depicted.
<br><p align="center"><img src="Images/Regular.png" width="300"> <img src="Images/RegularLabelled.png" width="300"></p>

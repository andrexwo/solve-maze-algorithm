# Maze Solver using Stack

This project is an implementation of a **maze solver** using a **stack-based depth-first search (DFS)** approach. The project was developed for the **Data Structures** course at **UFPB (Universidade Federal da Paraíba)**.

## Features

- **Custom Stack Implementation**: The stack was implemented from scratch without using built-in Python data structures.
- **Maze Representation**: The maze is represented as a 2D grid loaded from a CSV file.
- **Pathfinding Algorithm**: The algorithm explores paths recursively and backtracks if necessary.
- **Graphical Visualization**: The maze and the player's movement are displayed using **Pygame**.

## How It Works

1. The maze is loaded from a CSV file, where:
   - `0` represents a wall
   - `1` represents a valid path
   - The player's initial position and the goal (prize) are randomly placed.
2. The DFS algorithm starts from the initial position and explores adjacent cells.
3. If a valid move is found, it is pushed onto the stack and the player moves.
4. If no valid move is found, the player backtracks and tries a different path.
5. The process repeats until the goal is reached or all possibilities are exhausted.

## File Structure

```
maze_solver/
├── main_maze.py       # Main execution file
├── maze.py            # Maze class with logic for loading and visualizing the maze
├── pilha.py           # Custom stack implementation
├── labirinto1.txt     # Maze data file
└── README.md          # Project documentation
```

## Dependencies

- Python 3.x
- `pygame`
- `numpy`

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/maze_solver.git
   ```
2. Install dependencies:
   ```sh
   pip install pygame numpy
   ```
3. Run the program:
   ```sh
   python main_maze.py
   ```

## Author

Developed by **André Luiz Carvalho** for the **Data Structures** course at UFPB.

## License

This project is licensed under the MIT License.


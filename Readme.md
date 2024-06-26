# Conway's Game of Life - Python Implementation

[![Watch the video](https://img.youtube.com/vi/)](https://github.com/ahmedsaad562000/conways-game-of-life/assets/76961547/988d489e-ab4f-47ad-8efb-699af0fa05ac)



## Description

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

This repository contains a Python implementation of Conway's Game of Life using Pygame for visualization.

## Features

- Simulation of Conway's Game of Life rules.
- Interactive grid where you can set the initial configuration **(using your mouse)**.
- Start, pause simulation
- reset all cells.
- randomize cells.

## Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/ahmedsaad562000/conways-game-of-life.git
   cd Conway
   ```

2. **Create a Conda environment**:
   ```sh
   conda env create -f environment.yaml
   conda activate conway
   ```

## Usage

1. **Run the game**:
   ```sh
   python main.py
   ```

2. **Controls**:
   - Click on any cell in the grid to set the initial configuration.
   - Press `Space` to start/pause the simulation.
   - Press `C` to clear the grid.
   - Press `R` to randomize the cells' positon.

## Conway's Game of Life Rules

1. **Survival**: A live cell with two or three live neighbors stays alive.
2. **Death by Isolation**: A live cell with fewer than two live neighbors dies.
3. **Death by Overcrowding**: A live cell with more than three live neighbors dies.





























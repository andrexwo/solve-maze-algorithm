# -*- coding: utf-8 -*-
import time
from maze import Maze
from collections import deque
from pilha import Pilha

s = deque()
maze_csv_path = "labirinto1.txt"
maze = Maze()

maze.load_from_csv(maze_csv_path)
maze.run()
maze.init_player()

pilha = Pilha() # criação da pilha
pilha.empilhar(maze.get_init_pos_player()) # empilho a primeira coordenada, a inicial do jogador

#criação da função checa adjacente, usando recursividade
def checaAdj(pos, visited=None):
    if visited is None:
        visited = set()
    if pilha.vazia():
        return False

    visited.add(pos)
    maze.mov_player(pos)
    time.sleep(0.01)

    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dx, dy in direcoes:
        nova_pos = (pos[0] + dx, pos[1] + dy)
        if nova_pos in visited or not maze.is_free(nova_pos):
            continue

        if maze.find_prize(nova_pos):
            pilha.empilhar(nova_pos)
            maze.mov_player(nova_pos)
            return True
        
        pilha.empilhar(nova_pos)

        if checaAdj(nova_pos, visited):
            return True

        pilha.desempilhar()
        visited.remove(nova_pos)
        maze.mov_player(pos)
    
    return False

visited = set()
checaAdj(maze.get_init_pos_player(), visited)

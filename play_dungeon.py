import pygame
from pygame.locals import *
import sys
from maze import Maze
from player import Player


def main():
    pygame.init()
    res = wi, hi = (800, 600)
    d_surf = pygame.display.set_mode(res)

    clock = pygame.time.Clock()
    fps = 30

    tile_sq = 33
    tile_px = 16
    mz_px = tile_px * tile_sq
    mz = Maze(size=tile_sq, tile_px=tile_px)
    mz_rect = Rect((wi - mz_px) / 2, (hi - mz_px) / 2, mz_px, mz_px)

    player = Player()

    while True:

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == 27:
                pygame.quit()
                sys.exit()
            elif e.type == KEYDOWN:
                player.handle_input(e.key)
                # TODO check player position is legal. need to save last pos.

        d_surf.fill((0, 0, 0))
        draw_maze(d_surf, mz, mz_rect)
        draw_player(d_surf, player, mz, mz_rect)
        pygame.display.update()
        clock.tick(fps)


def draw_maze(d_surf, mz, mz_rect):
    """define a rect for each tile in mz.maze and draw it."""
    t_px = mz.maze[0][0].px
    for y in range(len(mz.maze)):
        for x in range(len(mz.maze[0])):
            rct_left = mz_rect.left + t_px * x
            rct_top = mz_rect.top + t_px * y
            tile_rct = Rect(rct_left, rct_top, t_px, t_px)
            d_surf.fill(mz.maze[y][x].col, tile_rct)  # PH


def draw_player(d_surf, player, mz, mz_rect):
    """Draw the player."""
    rct_left = mz_rect.left + mz.tile_px * player.x
    rct_top = mz_rect.top + mz.tile_px * player.y
    ply_rct = Rect(rct_left, rct_top, mz.tile_px, mz.tile_px)
    d_surf.fill((127, 255, 127), ply_rct)  # PH


if __name__ == '__main__':
    main()

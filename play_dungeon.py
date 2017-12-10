import pygame
from pygame.locals import *
import sys
from math import sqrt
from maze import Maze
from player import Player


# TODO some sort of 'fog of war' effect.
# TODO a zoom effect, so we scroll around the maze, and it is bigger than scr?
# but might be HARD.
# TODO a logical tree in maze class; loot in terminii
# TODO antagonists
# TODO tweening


def main():
    pygame.init()
    res = wi, hi = (800, 600)
    d_surf = pygame.display.set_mode(res)

    clock = pygame.time.Clock()
    fps = 30

    tile_sq = 33
    tile_px = 48
    mz_px = tile_px * (tile_sq + 2)
    mz = Maze(size=tile_sq, tile_px=tile_px)
    damp = 4

    player = Player()
    p_anchor = Rect((wi - tile_px) // 2, (hi - tile_px) // 2, tile_px, tile_px)
    
    mz_rect = Rect(p_anchor.left - (player.x * tile_px),
                   p_anchor.top - (player.y * tile_px),
                   mz_px, mz_px)

    while True:

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == 27:
                pygame.quit()
                sys.exit()
            elif e.type == KEYDOWN:
                player.handle_input(e.key)

            if mz.move_is_legal(player):
                player.update_pos()
            else:
                player.next_x, player.next_y = player.x, player.y

        mz_rect = position_maze(p_anchor, player, mz_rect, tile_px, damp)
        damp = update_damping(p_anchor, mz_rect)
        d_surf.fill((0, 0, 0))
        draw_maze(d_surf, mz.mz, mz_rect)
        draw_player(d_surf, player, mz, mz_rect)
        pygame.display.update()
        clock.tick(fps)


def update_damping(p_anchor, mz_rect):
    x_delta = mz_rect.left - p_anchor.left
    y_delta = mz_rect.top - p_anchor.top
    delta = abs(max(x_delta, y_delta))
    new_damp = int(sqrt(delta) / 2)
    return new_damp


def position_maze(p_anchor, player, mz_rect, tile_px, dmp):
    """Return a new mz_rect based on the player's position, to keep the player centred."""
    new_left = p_anchor.left - tile_px * player.x
    new_top = p_anchor.top - tile_px * player.y
    left_delta = new_left - mz_rect.left
    top_delta = new_top - mz_rect.top
    if abs(left_delta) > dmp:
        if left_delta > 0:
            left_delta = dmp
        else:
            left_delta = -dmp
    if abs(top_delta) > dmp:
        if top_delta > 0:
            top_delta = dmp
        else:
            top_delta = -dmp
    new_mz_rect = Rect(mz_rect.left + left_delta, mz_rect.top + top_delta, mz_rect.width, mz_rect.height)
    return new_mz_rect


def draw_maze(d_surf, mz, mz_rect):
    """define a rect for each tile in mz.maze and draw it."""
    t_px = mz[0][0].px
    for y in range(len(mz)):
        for x in range(len(mz[0])):
            rct_left = mz_rect.left + t_px * x
            rct_top = mz_rect.top + t_px * y
            tile_rct = Rect(rct_left, rct_top, t_px, t_px)
            d_surf.fill(mz[y][x].col, tile_rct)  # PH


def zoom(mz, px_delta):
    """Zoom by incrementing or decrementing tile size. Returns the new tile size."""
    mz.tile_px += px_delta
    for y in range(len(mz.mz)):
        for x in range(len(mz.mz)):
            mz.mz[y][x].px += px_delta
    return mz.tile_px


def draw_player(d_surf, player, mz, mz_rect):
    """Draw the player."""
    rct_left = mz_rect.left + mz.tile_px * player.x
    rct_top = mz_rect.top + mz.tile_px * player.y
    ply_rct = Rect(rct_left, rct_top, mz.tile_px, mz.tile_px)
    d_surf.fill((127, 255, 127), ply_rct)  # PH


if __name__ == '__main__':
    main()

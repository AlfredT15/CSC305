"""Agile Dungeon main game loop"""
import sys
import pygame
from common.game import Game


def main():
    """Main function for game which creates the game instance and runs it."""

    # Start up pygame and make a blank window
    pygame.init()

    # Make a game instance
    game = Game()

    # Run the game
    game.run_game()

if __name__ == "__main__":
    main()
    sys.exit()

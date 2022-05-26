from tower.game import TowerGame
import click
from tower.game import start_game


@click.group()
def main():
    """
    Entrypoint for the Tower Defense Game from the command line.
    """

@main.command(help="Launches the Tower Defense Game")
def launch():
    start_game()

if __name__ == "__main__":
    main()

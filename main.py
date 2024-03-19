from engine.main import Game
import scriptred
import my_script
from  sample_scripts import sample3
if __name__ == "__main__":
    G = Game((40, 40), my_script, scriptred)
    G.run_game()


from snake import SnakeGame
import random

sg = SnakeGame(human_player=False)
#sg.run()

while True:
    sg.clock.tick(10)
    print(sg.xs, sg.ys)
    sg.dirs = random.randint(0, 3)  # 0=Up, 1=Left, 2=Down, 3=Right
    sg.next_step()
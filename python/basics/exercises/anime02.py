from random import randint
from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Stars


def background(screen):
    effects = [
        Stars(screen, 200)
    ]
    screen.play([Scene(effects, 10)])


def ship(screen):
    center = (screen.width//2, screen.height//2)
    screen.move(*center)
    screen.draw(10, 10, colour=255)


def main(screen):
    background(screen)
    ship(screen)
    # while True:
    #     background(screen)
    #     # screen.print_at('Hello world!',
    #     #                 randint(0, screen.width), randint(0, screen.height),
    #     #                 colour=randint(0, screen.colours - 1),
    #     #                 bg=randint(0, screen.colours - 1))
    #     ev = screen.get_key()
    #     if ev in (ord('Q'), ord('q')):
    #         return
    #     screen.refresh()


if __name__ == '__main__':
    Screen.wrapper(main)

from setting import *
from circle import circle

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill("#bdc3c7")
        circle.display()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

main()
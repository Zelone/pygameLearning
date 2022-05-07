import pygame
pygame.init()

def draw(WINDOW,BG_COLOR):
    WINDOW.fill(BG_COLOR)
    pygame.display.update()

def main(WIDTH,HEIGHT):
    BG_COLOR = 'gray85'
    TITLE_TEXT = 'Minesweeper'
    WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))#,flag=pygame.OPENGL)
    pygame.display.set_caption(TITLE_TEXT)
    CLOCK= pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            #if event.type == pygame.KEYDOWN:
            #if event.type == pygame.KEYUP:
            #if event.type == pygame.MOUSEMOTION:
            #if event.type == pygame.MOUSEWHEEL:
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #if event.type == pygame.MOUSEBUTTONUP:
            
        CLOCK.tick(60)
        draw(WINDOW,BG_COLOR)
    pygame.quit()

if __name__ == "__main__":
    WIDTH,HEIGHT = 700,800
    main(WIDTH,HEIGHT)
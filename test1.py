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
            print('N',end='')
            if event.type == pygame.QUIT:
                print('Q:',event)
                run = False
                break
            #print(event.type)
            if event.type == pygame.KEYDOWN:
                print(event)
                print(event.unicode,event.key)
                print(pygame.mouse.get_pos())
                print(pygame.mouse.get_rel())#from previous position
            if event.type == pygame.KEYUP:
                print(event)
                print(event.unicode,event.key)
                print(pygame.mouse.get_pos())
                print(pygame.mouse.get_rel())#from previous position
            if event.type == pygame.MOUSEMOTION:
                print(event)
                print('motion')
                print('')
            if event.type == pygame.MOUSEWHEEL:
                print(event)
                print('wheel')
                print('')
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event)
                print('DOWN',event.button)#1:leftclick, 2:middleclick, 3:rightclick, 4:scrollup, 5:scrolldown
                print(event.pos)
                print(pygame.mouse.get_rel())#from previous position 
            if event.type == pygame.MOUSEBUTTONUP:
                print(event)
                print('UP',event.button)#1:leftclick, 2:middleclick, 3:rightclick, 4:scrollup, 5:scrolldown
                print(event.pos)
                print(pygame.mouse.get_rel())#from previous position you started clicking
        CLOCK.tick(60)
        draw(WINDOW,BG_COLOR)
    pygame.quit()

if __name__ == "__main__":
    WIDTH,HEIGHT = 700,800
    main(WIDTH,HEIGHT)
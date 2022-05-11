import pygame
pygame.init()

RANDOM_COLOR = (90,210,148)
RANDOM_COLOR = (0,0,0)
def draw(WINDOW,WIDTH,HEIGHT,BG_COLOR,BOARDS,):
    WINDOW.fill(BG_COLOR)
    for BOARD in BOARDS:
        x,y,row,col,xo,yo,perh = BOARD['Coords']
        w = WIDTH - x - xo 
        h = w*perh
        if h + y +yo > HEIGHT:
            h= HEIGHT - y - yo
        wpart , hpart = float(int((w*100)/col))/100 , float(int((h*100)/row))/100
        w = wpart * col
        h = hpart * row
        for i in range(row):
            for j in range(col):
                view = BOARD['Views'][BOARD['Background'][i*row+j]]
                if view['type'] == 'C':
                    color =  view['color']
                pygame.draw.rect(WINDOW,color,(x+j*wpart,y +i*hpart ,wpart,hpart))

    pygame.display.update()

def main(WIDTH,HEIGHT):
    BG_COLOR = 'gray85'
    TITLE_TEXT = 'Minesweeper'
    WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))#,flag=pygame.OPENGL)
    pygame.display.set_caption(TITLE_TEXT)
    CLOCK= pygame.time.Clock()
    
    BOARD = {}
    BOARD['Coords'] =[4,4,15,15,4,4,0.75] #x,y,rows,cols,-x,-y,height=perwidth
    BOARD['Hidden'] = {i:1 for i in range(BOARD['Coords'][2] * BOARD['Coords'][3])}
    BOARD['Background'] = {i:1  for i in range(BOARD['Coords'][2] * BOARD['Coords'][3])}
    BOARD['Background'][5]  = 2
    BOARD['Machines'] = {}
    BOARD['Items'] = {}
    BOARD['Players'] = {}
    BOARD['Views'] = {}
    BOARD['Views'][1] = {'type':'C','color':'forestgreen','comment':'background'}
    BOARD['Views'][2] = {'type':'C','color':'purple','comment':'background'}
    BOARD['ItemsEntity'] = {}
    BOARDS=[BOARD]
    print(BOARDS)
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
        draw(WINDOW,WIDTH,HEIGHT,BG_COLOR,BOARDS)
    pygame.quit()


if __name__ == "__main__":
    WIDTH,HEIGHT = 1200,600
    main(WIDTH,HEIGHT)
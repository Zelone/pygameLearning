import pygame
pygame.init()

RANDOM_COLOR = (90,210,148)
RANDOM_COLOR = (0,0,0)
MAX_TICKS = 60

def drawBOARDS(WINDOW,WIDTH,HEIGHT,BG_COLOR,BOARDS):
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
def renderTICKS(WINDOW,font,wpart,TICKS,y,strr):
    #RENDER WORDS 
    render = font.render(strr+"Hi "+':'.join([str(i) for i in TICKS]),True,"Black")
    rr = WIDTH - render.get_width()-20 
    rr = rr - rr % wpart
    WINDOW.blit(render,(rr,y))
    return 0

def draw(WINDOW,WIDTH,HEIGHT,BG_COLOR,TICKS,EVENT_TICK,event_bol):
    WINDOW.fill(BG_COLOR)
    font = pygame.font.SysFont("arial", 12)
    PPart = 75
    wpart = WIDTH / PPart
    partloc = 0
    #RENDER LINES
    for _ in range(PPart):
        partloc += wpart 
        pygame.draw.line(WINDOW,'black',(partloc,25),(partloc,30),1)
    
    renderTICKS(WINDOW,font,wpart,TICKS,10,'')
    #if(event_bol):
    renderTICKS(WINDOW,font,wpart,EVENT_TICK,30,'event ')

    pygame.display.update()
    return 0

def main(WIDTH,HEIGHT):
    BG_COLOR = 'white'
    TITLE_TEXT = 'Platform'
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
    TICK = [0 for _ in range(7) ]
    EVENT_TICK = [0 for _ in range(5) ]

    #print(BOARDS)
    run = True
    while run: 
        #tick loop
        LEN = len(TICK)-1
        TICK[LEN] += 1
        while (TICK[LEN] >= MAX_TICKS):
            TICK[LEN] = 0
            LEN -= 1
            if LEN < 0: break
            TICK[LEN] += 1
        event_bol = False
        for event in pygame.event.get():

            LEN = len(EVENT_TICK)-1
            EVENT_TICK[LEN] += 1
            while (EVENT_TICK[LEN] >= MAX_TICKS):
                EVENT_TICK[LEN] = 0
                LEN -= 1
                if LEN < 0: break
                EVENT_TICK[LEN] += 1

            pygame.mouse.set_pos = (WIDTH/2,HEIGHT/2)
            #events loop
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                run = False
                break
            if event.type == pygame.MOUSEMOTION:
                mouse_rel_move = event.rel
                if mouse_rel_move != (0,0):
                    None
                    #mouse movement  
            #if event.type == pygame.KEYDOWN:
            #if event.type == pygame.KEYUP:
            #if event.type == pygame.MOUSEMOTION:
            #if event.type == pygame.MOUSEWHEEL:
            #if event.type == pygame.MOUSEBUTTONDOWN:
            #if event.type == pygame.MOUSEBUTTONUP:
            event_bol = True
            #drawEVENTS(WINDOW,WIDTH,HEIGHT,BG_COLOR,EVENT_TICK)

        CLOCK.tick(60)
        draw(WINDOW,WIDTH,HEIGHT,BG_COLOR,TICK,EVENT_TICK,event_bol)
        event_bol = False
        #drawBOARDS(WINDOW,WIDTH,HEIGHT,BG_COLOR,BOARDS)
    print(TICK)
    print(EVENT_TICK)
    pygame.quit()


if __name__ == "__main__":
    WIDTH,HEIGHT = 1000,600
    main(WIDTH,HEIGHT)

"""
Valid Sequence for actions 

1.Event 

2.Actions then 

3.results 

4.show effects 

"""
"""
Block in 3D space 
Texture of visible side 
change angle of viewing as mouse moves 
with acceleration code

numpy add or change sequence as movement (LAzy code )


"""
import pygame
pygame.init()
screen = pygame.display.set_mode((300, 350))
done = False
clock = pygame.time.Clock()
#pressed = pygame.key.get_pressed()
#timer = 0;
class gvar:
    ##x first then y
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    xp = 0
    yp = 0
    turn = 1
    timer = 0;
class gamef:   
    def grid_d():
        #Framerate of 10
        myfont = pygame.font.SysFont("monospace", 25)
        label = myfont.render("Player "+str(gvar.turn)+" turn", 1, (255,255,255))
        screen.blit(label, (0, 300))
        label = myfont.render("FPS 100", 1, (255,255,255))
        screen.blit(label, (0, 325))
        myfont = pygame.font.SysFont("monospace", 80)
        for x in range(3):
            for y in range(3):
                tmp = ""
                if(gvar.grid[x][y] == 0):
                    color=(64,64,64)
                    
                elif (gvar.grid[x][y] == 1):
                    color=(255,0,0)
                    tmp = "X"
                else:
                    color=(0,0,255)
                    tmp = "O"
                pygame.draw.rect(screen, color, pygame.Rect(x*100,y*100, 100, 100))
                label = myfont.render(str(tmp), 1, (255,255,255))
                screen.blit(label, (x*100+28, y*100+10))
                if(x == gvar.xp and y == gvar.yp):
                     pygame.draw.rect(screen, (128,128,128), pygame.Rect(x*100+10,y*100+10, 80, 80))
    def keydet():
        pressed = pygame.key.get_pressed()
        if (gvar.timer >= 25):
            if pressed[pygame.K_UP]:
                if (gvar.yp -1 >=0):
                    gvar.yp -= 1
                    gvar.timer = 0
            if pressed[pygame.K_DOWN]:
                if (gvar.yp +1 <= 2):
                    gvar.yp += 1
                    gvar.timer = 0
            if pressed[pygame.K_LEFT]:
                if (gvar.xp -1 >=0):
                    gvar.xp -= 1
                    gvar.timer = 0
            if pressed[pygame.K_RIGHT]:
                if (gvar.xp +1 <= 2):
                    gvar.xp += 1
                    gvar.timer = 0
            if pressed[pygame.K_RETURN]:
                if (gvar.grid[gvar.xp][gvar.yp] == 0):
                    gvar.grid[gvar.xp][gvar.yp] = gvar.turn
                    if gvar.turn == 1:gvar.turn = 2;
                    else:gvar.turn = 1;
    def check_winner():
        xgrid = gvar.grid
        if(xgrid[0][0] == xgrid[0][1] and xgrid[0][0] == xgrid[0][2] and xgrid[0][0] != 0):
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(0,0,300,30))
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("Player "+str(xgrid[0][0])+" Wins", 1, (255,255,255))
            screen.blit(label, (0, 0))
            return True
        elif(xgrid[1][0] == xgrid[1][1] and xgrid[1][0] == xgrid[1][2] and xgrid[1][0] != 0):
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(0,0,300,30))
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("Player "+str(xgrid[1][0])+" Wins", 1, (255,255,255))
            screen.blit(label, (0, 0))
            return True
        elif(xgrid[2][0] == xgrid[2][1] and xgrid[2][0] == xgrid[2][2] and xgrid[2][0] != 0):
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(0,0,300,30))
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("Player "+str(xgrid[2][0])+" Wins", 1, (255,255,255))
            screen.blit(label, (0, 0))
            return True

        elif(xgrid[0][0] == xgrid[1][0] and xgrid[0][0] == xgrid[2][0] and xgrid[0][0] != 0):
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(0,0,300,30))
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("Player "+str(xgrid[0][0])+" Wins", 1, (255,255,255))
            screen.blit(label, (0, 0))
            return True
        elif(xgrid[0][1] == xgrid[1][1] and xgrid[0][1] == xgrid[2][1] and xgrid[0][1] != 0):
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(0,0,300,30))
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("Player "+str(xgrid[0][1])+" Wins", 1, (255,255,255))
            screen.blit(label, (0, 0))
            return True
        elif(xgrid[0][2] == xgrid[1][2] and xgrid[0][2] == xgrid[2][2] and xgrid[0][2] != 0):
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(0,0,300,30))
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("Player "+str(xgrid[0][2])+" Wins", 1, (255,255,255))
            screen.blit(label, (0, 0))
            return True
        elif(xgrid[0][0] == xgrid[1][1] and xgrid[0][0] == xgrid[2][2] and xgrid[0][0] != 0):
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(0,0,300,30))
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("Player "+str(xgrid[0][0])+" Wins", 1, (255,255,255))
            screen.blit(label, (0, 0))
            return True
        elif(xgrid[2][0] == xgrid[1][1] and xgrid[2][0] == xgrid[0][2] and xgrid[0][2] != 0):
            pygame.draw.rect(screen, (128,128,128), pygame.Rect(0,0,300,30))
            myfont = pygame.font.SysFont("monospace", 30)
            label = myfont.render("Player "+str(xgrid[0][2])+" Wins", 1, (255,255,255))
            screen.blit(label, (0, 0))
            return True
        else:
            return False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:done = True
    screen.fill((0, 0, 0))
    gvar.timer+=1
    gamef.grid_d()
    if(not gamef.check_winner()):gamef.keydet()
    else:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_r]:gvar.grid = [[0,0,0],[0,0,0],[0,0,0]]
    pygame.display.flip()
    clock.tick(100)
exit()

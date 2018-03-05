import pygame
import time

SQUARE_WIDTH = 10
SQUARE_HEIGHT = 20
SQUARE_SIZE = 20
SPEED = 1
FPS = 50

BLACK = (0,0,0)
WHITE = (255,255,255)

BLOCK_ORIENTATION = 0
BLOCK_FREE = ' '
BLOCK_TAKEN = 'X'
BLOCK_TEMP = 'T'

BOARD_STATE = [[BLOCK_FREE for i in range(SQUARE_WIDTH)] for j in range(SQUARE_HEIGHT)]

pygame.init()
gd = pygame.display.set_mode((SQUARE_WIDTH * SQUARE_SIZE, SQUARE_HEIGHT * SQUARE_SIZE))
clock = pygame.time.Clock()

def drawBlock(pos):
    pygame.draw.rect(gd,BLACK,(pos[0] * SQUARE_SIZE,pos[1] * SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE))
    
    
def drawBlocks(posList):
    [pygame.draw.rect(gd,BLACK,(pos[0] * SQUARE_SIZE,pos[1] * SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)) for pos in posList]
    

def drawPiece(piece, pos, orientation = 1):
    if piece == 'L':
        if   orientation == 0: drawBlocks([(pos[0],pos[1]-1),  pos,(pos[0],pos[1]+1), (pos[0]+1,pos[1]+1)])
        elif orientation == 1: drawBlocks([(pos[0]-1,pos[1]),  pos,(pos[0]+1,pos[1]), (pos[0]+1,pos[1]-1)])
        elif orientation == 2: drawBlocks([(pos[0]-1,pos[1]-1),(pos[0],pos[1]-1),pos, (pos[0],  pos[1]+1)])
        elif orientation == 3: drawBlocks([(pos[0]-1,pos[1]+1),(pos[0]-1,pos[1]),pos, (pos[0]+1,pos[1]  )])


BOARD_STATE[1][1] = 'X'
print(BOARD_STATE)
        

pos = (2,2)
last = time.time()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if   event.key == pygame.K_LEFT: pos = (pos[0] - 1, pos[1])
            elif event.key == pygame.K_RIGHT:pos = (pos[0] + 1, pos[1])
            elif event.key == pygame.K_UP:BLOCK_ORIENTATION += 1
            


    if time.time() - last > SPEED:
        pos = (pos[0],pos[1] + 1)
        last = time.time()
    
    gd.fill(WHITE)
    drawPiece('L',pos, BLOCK_ORIENTATION % 4)
    pygame.display.update()
    clock.tick(FPS)



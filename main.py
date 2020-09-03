import sys, pygame

pygame.init()

size = width, height = 640, 480
dx = 1
dy = 1
x= 163
y = 120
white = (255,255,255)
aqua = (0,128,128)

screen = pygame.display.set_mode(size)

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x += dx
    y += dy

    if x < 0 or x > width:   
        dx = -dx

    if y < 0 or y > height:
        dy = -dy

    screen.fill(white)

    pygame.draw.circle(screen, aqua, (x,y), 8)

    pygame.display.flip()
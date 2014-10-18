import pygame, sys
from pygame.locals import *

bgImgFile = "playmat.jpg"

mouseImgFile = "aromatisse.jpg"

pygame.init()
screen = pygame.display.set_mode((1024, 513), 0, 32) #size, ?, bit

background = pygame.image.load(bgImgFile).convert()
cursor = pygame.image.load(mouseImgFile).convert_alpha() #alpha means transparency

while(True):
	for event in pygame.event.get():
		if(event.type == QUIT):
			pygame.quit()
			sys.exit()
	screen.blit(background, (0, 0))

	x, y = pygame.mouse.get_pos()
	x -= cursor.get_width() / 2
	y -= cursor.get_height() / 2

	screen.blit(cursor, (x, y))
	#screen.fill(background)
	pygame.display.update()

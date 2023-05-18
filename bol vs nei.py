import pygame
import random

clock = pygame.time.Clock() 
 		

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption(("game neiro"))
icon = pygame.image.load('gn/1.png')
pygame.display.set_icon(icon)
#backgroud
bg=pygame.image.load('gn/bl1.jpg')

#4 brush
square1= pygame.Surface((900,10))
square1.fill('red')
square2=pygame.Surface((10,900))
square2.fill('red')
square3= pygame.Surface((900,10))
square3.fill('red')
square4=pygame.Surface((10,900))
square4.fill('red')

bg=pygame.image.load('gn/bl1.jpg')
#text
text = pygame.font.Font('gn/Intro.otf',40)
text_op=text.render('YOU LOSE',True,'blue')
restart=text.render('restart',False,'red')
restart_op=restart.get_rect(topleft=(350,300))

players1=[
pygame.image.load('gn/p3.png')
] 

bad=[pygame.image.load('gn/p1.png')]

run = True
bgx=0
px1=50
py1=400
pspeed=5
jamp1=10
isjamp1=False
jn1=0
n1=0
bx=random.randrange(50,850)
by=random.randrange(50,550)
a=10
b=10
n=1000
play=True
while run:
	if play:
		py1+=10
		screen.blit(bg, (bgx,0))
		screen.blit(bg, (bgx+900,0))
		screen.blit(square1, (1,1))
		screen.blit(square2, (1,1))
		screen.blit(square4, (890,1))
		screen.blit(square3, (1,590))
		screen.blit(players1[0], (px1,py1-50))
		screen.blit(bad[0], (bx,by))
		#kasania
		bl1=square1.get_rect(topleft=(1,1))
		bl2=square2.get_rect(topleft=(1,1))
		bl3=square4.get_rect(topleft=(890,1))
		bl4=square3.get_rect(topleft=(1,590))
		players=players1[0].get_rect(topleft=(px1,py1-50))
		bad1=bad[0].get_rect(topleft=(bx,by))

		#jol
		if bad1.colliderect(bl1):
			a=-a
		if bad1.colliderect(bl4):
			a=-a
		if bad1.colliderect(bl2):
			b=-b
		if bad1.colliderect(bl3):
			b=-b
		by+=a
		bx+=b
		#if
		if players.colliderect(bl1):
			py1=30      
			n1=1
		if players.colliderect(bl4):
			py1=590-56
			n1=1
		if players.colliderect(bad1):
			play=False

		

		key= pygame.key.get_pressed()

		if not isjamp1:
			if key[pygame.K_SPACE] and n1==1:
				isjamp1=True
		else:
			if jamp1 >= -10:
				if jamp1 >0:
					py1 -= jamp1**2/2
					py1-=10
				jamp1-=1
			else:
				isjamp1=False
				jamp1=10
				n2=0


		if key[pygame.K_RIGHT]:
			px1+=pspeed
		elif key[pygame.K_LEFT]:
			px1-=pspeed

		if px1>=850:
			px1=850
		if px1<=0:
			px1=0
		bgx-=1
		if bgx==-900:
			bgx=0

		n1=0
		clock.tick(60)/n
		n+=1
	
	else:

		screen.fill((87,88,89))
		screen.blit(restart,(restart_op))
		screen.blit(text_op,(350,200))
		mouse=pygame.mouse.get_pos()
        
		if restart_op.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
			play=True
			px1=50
			py1=400
			bx=random.randrange(50,850)
			by=random.randrange(50,550)
         




	for event in pygame.event.get():
		if event.type == pygame.QUIT:
	 		run= False
	 		pygame.quit()

	pygame.display.update()
	


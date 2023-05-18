import pygame

clock = pygame.time.Clock() 
 		

pygame.init()
screen = pygame.display.set_mode((900,600))
pygame.display.set_caption(("game neiro"))
icon = pygame.image.load('gn/1.png')
pygame.display.set_icon(icon)
#backgroud
bg=pygame.image.load('gn/bl1.jpg')

#4 brush
bh=5
bw=900
bw1=70
bw2=70
square= pygame.Surface((bw,bh))
square.fill('blue')
square1=pygame.Surface((bw1,bh))
square1.fill('red')
square2=pygame.Surface((bw2,bh))
square2.fill('red')
finish= pygame.Surface((20,50))
finish.fill('yellow')
#text
#text = pygame.font.Font(.render('Попытка номер', True, 'blue'))

players1=[
pygame.image.load('gn/p1.png')
] 
players2=[
pygame.image.load('gn/p1.png')
]
run = True
bgx=0
px1=20
py1=500
px2=860
py2=500

pspeed=5
jamp1=8
isjamp1=False
pspeed2=8
jamp2=8
isjamp2=False
jn1=0
jn2=0

while run:
	py1+=10
	py2+=10
	screen.blit(bg, (bgx,0))
	screen.blit(bg, (bgx+900,0))	
	screen.blit(players1[0], (px1,py1))
	screen.blit(players2[0], (px2,py2))
	screen.blit(square, (0,550))
	screen.blit(square1, (250,470))
	screen.blit(square2, (550,470))
	screen.blit(finish, (890,430))

	#kasania
	pk1=players1[0].get_rect(topleft=(px1,py1))
	pk2=players2[0].get_rect(topleft=(px2,py2))
	bl=square.get_rect(topleft=(0,550))
	bl1=square1.get_rect(topleft=(250,470))
	bl2=square2.get_rect(topleft=(550,470))
	f=finish.get_rect(topleft=(890,430))

	if pk1.colliderect(bl):
		py1=550-56
		n1=1
	if pk2.colliderect(bl):
		py2=550-56
		n2=1
	if pk1.colliderect(bl1) or pk1.colliderect(bl2):
		py1=470-56
		n1=1
	if pk2.colliderect(bl1) or pk2.colliderect(bl2):
		py2=470-56
		n2=1

	if pk1.colliderect(pk2):
		px1=450
		py1=0
	if pk1.colliderect(f):
		px2=860
		py2=500
		px1=20
		px=500

	key= pygame.key.get_pressed()

	if not isjamp1:
		if key[pygame.K_SPACE] and n2==1:
			isjamp1=True
	else:
		if jamp1 >= -12:
			if jamp1 >0:
				py2 -= jamp1**2/2
				py2-=12
			jamp1-=1
		else:
			isjamp1=False
			jamp1=12
			n2=0


	if key[pygame.K_d]:
		px1+=pspeed2
	elif key[pygame.K_a]:
		px1-=pspeed2


	if not isjamp2:
		if key[pygame.K_w] and n1==1:
			isjamp2=True
	else:
		if jamp2 >= -12:
			if jamp2 >0:
				py1 -= jamp2**2/2
				py1-=12
			jamp2-=1
		else:
			isjamp2=False
			jamp2=12
			n1=0

	if key[pygame.K_RIGHT]:
		px2+=pspeed
	elif key[pygame.K_LEFT]:
		px2-=pspeed

	if px1 >=850:
		px1=850 
	elif px1<0:
		px1=0
	if px2>=850:
		px2=850
	elif px2<0:
		px2=0


	pygame.display.update()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
	 		run= False
	 		pygame.quit()

	bgx-=1
	if bgx==-900:
		bgx=0
	
	clock.tick(30) / 1000
	



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
bh=5
bw=900
bw1=50
square= pygame.Surface((bw,bh))
square.fill('blue')
square1=pygame.Surface((bw1,bh))
square1.fill('red')


players1=[
pygame.image.load('gn/p1.png')
] 
#pula
pula=pygame.image.load('gn/ko/pula.png')

run = True
bgx=0
px1=20
py1=500

pspeed=8
jamp1=8
isjamp1=False
n=0
#timer
nn=2000
timebl=pygame.USEREVENT+1
pygame.time.set_timer(timebl,nn)


box_bl=[]

b=950

time_pula=pygame.USEREVENT+1
pygame.time.set_timer(time_pula,1500)

box_pu=[]
puy=0

#texе
text = pygame.font.Font('gn/Intro.otf',40)
text_op=text.render('YOU LOSE',False,'blue')
restart=text.render('restart',False,'red')
restart_op=restart.get_rect(topleft=(350,300))

pun=10
eln=10

gameplay=True

while run:
    if gameplay:

        py1+=10
        a=random.randrange(0,570)
        pux=random.randrange(0,900)
        
        screen.blit(text_op, (450,200))

        screen.blit(bg, (bgx,0))
        screen.blit(bg, (bgx+900,0))    
        screen.blit(players1[0], (px1,py1))
        screen.blit(square, (0,550))

        


        #kop element
        if box_bl:
            for (i, el) in enumerate(box_bl):
                screen.blit(square1, (el.x,el.y+7))
                el.x-=eln
                if pk1.colliderect(el):
                    py1=el.y-49
                    px1=el.x
                    n=1
                if el.x < -50:
                    box_bl.pop(i)
        #pula
        if box_pu:
            for (j, pu) in enumerate(box_pu):
                screen.blit(pula, (pu.x,pu.y))
                pu.y+=pun
                pun+=0.1
                if pk1.colliderect(pu):
                    gameplay=False
                if pu.y> 650:
                    box_pu.pop(j)
                

        #kasania
        pk1=players1[0].get_rect(topleft=(px1,py1))
        bl=square.get_rect(topleft=(0,550))
        bl2=square1.get_rect(topleft=(b,a))
        



        if pk1.colliderect(bl):
            py1=550-56
            n=1
         

        key= pygame.key.get_pressed()

        if not isjamp1:
            if key[pygame.K_SPACE] and n==1:
                isjamp1=True
        else:
            if jamp1 >= -8:
                if jamp1 >0:
                    py1 -= jamp1**2/2
                    py1-=8
                jamp1-=1
            else:
                isjamp1=False
                jamp1=8
                n=0


        if key[pygame.K_d]:
            px1+=pspeed
        elif key[pygame.K_a]:
            px1-=pspeed
        if px1>=850:
            px1=850
        if px1<=0:
            px1=0
        bgx-=1
        if bgx==-900:
            bgx=0
        
        
    else:
        nn=1500
        screen.fill((87,88,89))
        screen.blit(text_op,(350,200))
        screen.blit(restart,restart_op)

        mouse=pygame.mouse.get_pos()
        if restart_op.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay=True
            px1=20
            py1=500
            box_bl.clear()
            box_pu.clear()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False
            pygame.quit()
        if event.type == timebl:
            box_bl.append(square1.get_rect(topleft=(b,a)))
        if event.type== time_pula:
            box_pu.append(pula.get_rect(topleft=(pux,puy)))
  
    pygame.display.update() 
    clock.tick(60)/1000
    


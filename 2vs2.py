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


#pula
pula=pygame.image.load('gn/ko/pula.png')

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
n1=0
n2=0

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
text_op=text.render('WIN AIZERE',True,'blue')
text_op2=text.render('WIN ERASYl',True,'blue')
restart=text.render('restart',False,'red')
restart_op=restart.get_rect(topleft=(350,300))

pun=10
eln=10

gameplay=True
win1=0
win2=0
win11=1
win22=1
w=False
w2=False
ww1=0
ww2=0
while run:
    if gameplay:
        ww1=1
        ww2=1

        py1+=10
        py2+=10
        a=random.randrange(0,570)
        pux=random.randrange(0,900)
        
        screen.blit(text_op, (450,200))

        screen.blit(bg, (bgx,0))
        screen.blit(bg, (bgx+900,0))    
        screen.blit(players1[0], (px1,py1))
        screen.blit(square, (0,550))
        screen.blit(players2[0], (px2,py2))

        


        #kop element
        if box_bl:
            for (i, el) in enumerate(box_bl):
                screen.blit(square1, (el.x,el.y+7))
                el.x-=eln
                if pk1.colliderect(el):
                    py1=el.y-49
                    px1=el.x
                    n=1
                if pk2.colliderect(el):
                    py2=el.y-49
                    px2=el.x
                    n2=1
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
                    win1=1
                    px2=860
                    py2=500
                if pk2.colliderect(pu):
                    gameplay=False
                    win2=1
                    px2=860
                    py2=500
                if pu.y> 650:
                    box_pu.pop(j)
                

        #kasania
        pk1=players1[0].get_rect(topleft=(px1,py1))
        pk2=players2[0].get_rect(topleft=(px2,py2))
        bl=square.get_rect(topleft=(0,550))
        bl2=square1.get_rect(topleft=(b,a))
        
        if pk2.colliderect(bl):
            py2=550-56
            n2=1


        if pk1.colliderect(bl):
            py1=550-56
            n=1
         

        key= pygame.key.get_pressed()

        if not isjamp1:
            if key[pygame.K_w] and n==1:
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

        if not isjamp2:
            if key[pygame.K_SPACE] and n2==1:
                isjamp2=True
        else:
            if jamp2 >= -8:
                if jamp2 >0:
                    py2 -= jamp2**2/2
                    py2-=8
                jamp2-=1
            else:
                isjamp2=False
                jamp2=8
                n2=0


        if key[pygame.K_RIGHT]:
            px2+=pspeed2
        elif key[pygame.K_LEFT]:
            px2-=pspeed2

        if px2>=850:
            px2=850
        if px2<=0:
            px2=0


        bgx-=1
        if bgx==-900:
            bgx=0
        
        
    else:
        nn=1500
        screen.fill((87,88,89))
        if win1==1:
            screen.blit(text_op,(350,200))
            w=True
        elif win2==1:
            screen.blit(text_op2,(350,200))
            w2=True
        screen.blit(restart,restart_op)

        if w==True and ww1==1:
            win11+=1
            print("aixere",win11-1)
            print("Erasyl",win22-1)
            w=False
            ww1=0
        if w2==True and ww2==1:
            win22+=1
            print("Erasyl",win22-1)
            print("aixere",win11-1)
            w2=False
            ww2=0
        
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
    



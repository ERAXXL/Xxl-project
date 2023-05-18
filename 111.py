import pygame
import random
import numpy as np
import matplotlib.pyplot as plt



def sigmoid(x):
    return 1 / (1 + np.exp(-x))
	
input_size = 4
hidden_size = 6
output_size = 3
learning_rate = 0.1

# Инициализируем веса нейронной сети случайным образом
W1 = np.random.randn(input_size, hidden_size)
b1 =np.zeros((1, hidden_size))
W2 =np.random.randn(hidden_size, output_size)
b2 =np.zeros((1, output_size))



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
square2=pygame.Surface((10,900))
square3= pygame.Surface((900,10))
square4=pygame.Surface((10,900))



bg=pygame.image.load('gn/bl1.jpg')
#text
text = pygame.font.Font('gn/Intro.otf',40)
text_op=text.render('YOU LOSE',True,'blue')
restart=text.render('restart',False,'red')
restart_op=restart.get_rect(topleft=(350,300))

players1=[
pygame.image.load('gn/p1.png')
] 

bad=[pygame.image.load('gn/bad.png')]

#shag players
timer=pygame.USEREVENT+1
pygame.time.set_timer(timer,1000)

run = True
bgx=0
px1=50
py1=400
pspeed=5
jamp1=10
isjamp1=False
jn1=0
n1=0
bx=random.randrange(50,800)
by=random.randrange(50,500)
a=10
b=10
n=1000
play=True
#x=np.array([[px1,py1,bx,by]])
y=np.random.randint(0,input_size-1)

loss_srr=[]
num=400

while run:	
	if play:
		
		#c2=(bx**2+by**2)**(1/2)
		X=np.array([[px1,py1,bx,by]])
		for i in range(int(float(num))):
		# Прямой проход
			z1 = np.dot(X, W1) + b1
			a1 = sigmoid(z1)
			z2 = np.dot(a1, W2) + b2
			y_pred = sigmoid(z2)

    		# Вычисляем ошибку и градиенты
			error = y_pred - y
			dW2 = np.dot(a1.T, error * y_pred * (1 - y_pred))
			db2 = np.sum(error * y_pred * (1 - y_pred), axis=0)
			dW1 = np.dot(X.T, np.dot(error * y_pred * (1 - y_pred), W2.T) * a1 * (1 - a1))
			db1 = np.sum(np.dot(error * y_pred * (1 - y_pred), W2.T) * a1 * (1 - a1), axis=0)
			# Обновляем веса
			W1 -= learning_rate * dW1
			b1 -= learning_rate * db1
			W2 -= learning_rate * dW2
			b2 -= learning_rate * db2
			loss_srr.append(z2[0])

		# Предсказываем метки классов на тестовых данных
		
		z1 = np.dot(X, W1) + b1
		a1 = sigmoid(z1)
		z2 = np.dot(a1, W2) + b2
		#game
		print(z2)



		py1+=15
		screen.blit(bg, (bgx,0))
		screen.blit(bg, (bgx+900,0))
		screen.blit(square1, (1,1))
		screen.blit(square2, (1,1))
		screen.blit(square4, (890,1))
		screen.blit(square3, (1,590))
		screen.blit(players1[0], (px1,py1))
		screen.blit(bad[0], (bx,by))

		#kasania
		bl1=square1.get_rect(topleft=(1,1))
		bl2=square2.get_rect(topleft=(1,1))
		bl3=square4.get_rect(topleft=(890,1))
		bl4=square3.get_rect(topleft=(1,590))
		players=players1[0].get_rect(topleft=(px1,py1))
		bad1=bad[0].get_rect(topleft=(bx,by))

		#jol
		if bad1.colliderect(bl1):
			a=-a
			square1.fill('blue')
		if bad1.colliderect(bl4):
			learning_rate*=0.5
			a=-a
			square3.fill('blue')
		if bad1.colliderect(bl2):
			b=-b
			square2.fill('blue')
		if bad1.colliderect(bl3):
			b=-b
			square4.fill('blue')
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
			if z2[0][2]>z2[0][1] and z2[0][2]>z2[0][0] and n1==1:
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

		if key[pygame.K_p]:
			print("w1",W1,"b1",b1)
			print("w2",W2,"b2",b2)

		if key[pygame.K_o]:
			plt.plot(loss_srr)
			plt.show()

		if  z2[0][0]>z2[0][1] and z2[0][0]>z2[0][2] :
			px1+=pspeed
		elif z2[0][1]>z2[0][0] and z2[0][1]>z2[0][2] :
			px1-=pspeed

		if z2[0][0]==z2[0][2] and z2[0][0]>z2[0][1]:
			px1+=pspeed
			isjamp1=True
		elif z2[0][1]==z2[0][2] and z2[0][1]>z2[0][0]:
			px1-=pspeed
			isjamp1=True
			


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
		play=True
		px1=50
		py1=400
		bx=random.randrange(50,800)
		by=random.randrange(50,500)
		loss_srr.clear()
		learning_rate*=1
		
		





	for event in pygame.event.get():
		if event.type == pygame.QUIT:
	 		run= False
	 		pygame.quit()
	
		if event.type == timer:
	 		#x=np.array([[px1,bx,py1,by]])
	 		#y=np.random.randint(0,1)
	 		square1.fill('black')
	 		square2.fill('black')
	 		square3.fill('black')
	 		square4.fill('black')

	pygame.display.update()
	

#rethult
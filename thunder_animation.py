import pygame
import random
import time
 
#intiating pygame
pygame.init()

#setting hex values of colors use in code
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
YELLOW = [255,242,0]

#setting screen size
SIZE = [600, 600]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Thunder Animation")

rain_list = []

#for loop for rain
for i in range(50):
    x = random.randrange(0, 600)
    y = random.randrange(0, 600)
    rain_list.append([x, y])
#for loop ends here

clock = pygame.time.Clock()


change = 0      #this is for car motion
tyre1 = 0       #this is for tyre1
tyre2 = 15      #this is fro tyre2
thunder = 0     #this is for thunder

#For screen
done = False
while not done:
 
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True   
 
    
    screen.fill(BLACK)
 
    #for thunder
    for i in range(len(rain_list)):

        if thunder > 15:
            pass
        else:
            pygame.draw.line(screen, YELLOW,[250,50],[200,0],4)
            pygame.draw.line(screen, YELLOW,[250,50],[210,35], 4)
            pygame.draw.line(screen, YELLOW,[210,35],[250,90], 4)


        #for rain
        pygame.draw.circle(screen, WHITE, rain_list[i], 2)  #rain fall
 
        pygame.draw.line(screen, WHITE, [0, 480], [600, 480])   # road up
        pygame.draw.line(screen, WHITE, [0, 530], [600, 530])   # road down

        pygame.draw.line(screen, WHITE, [20, 510], [100, 510])  # road lines
        pygame.draw.line(screen, WHITE, [150, 510], [230, 510])
        pygame.draw.line(screen, WHITE, [280, 510], [360, 510])
        pygame.draw.line(screen, WHITE, [410, 510], [490, 510])

        if((40 + change) > 640):
            change = 0
        if tyre1 == 15:
            tyre1 = 0
        if tyre2 == 0:
            tyre2 = 15

        #for car
        pygame.draw.rect(screen, WHITE, [10 + change, 450, 160, 30], 3)  # body down part

        pygame.draw.rect(screen, WHITE, [40 + change, 400, 70, 50], 3)  #body upper sq

        pygame.draw.line(screen, WHITE, [150 + change, 450],[110 + change, 400], 3)  #angle line

        pygame.draw.circle(screen, WHITE, [40 + change, 490], 15, tyre1) # back tire

        pygame.draw.circle(screen, WHITE, [144 + change, 490], 15, tyre2) # front tire



        rain_list[i][1] += 1

        if rain_list[i][1] > 500:
            thunder = random.randrange(0, 20)
            change = change + 1
            tyre1 = tyre1 + 1
            tyre2 = tyre2 - 1
            
            y = random.randrange(-50, -10)
            rain_list[i][1] = y
            
            x = random.randrange(0, 600)
            rain_list[i][0] = x
 
    
    pygame.display.flip()
    clock.tick(400)
 

pygame.quit()
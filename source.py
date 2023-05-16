import pygame
pygame.init()
sc = pygame.display.set_mode((800,500))

sc.fill((255,255,255))#R G B
pygame.display.update()

up = pygame.image.load("C:\\mxcmaterials\\up-9957a6bc-dd75-4608-88ed-be22cb6e7e86.png")
clear = pygame.image.load("C:\\mxcmaterials\\clear-f53e02bb-e9b5-497a-875e-a55ebb454f69.png")
add = pygame.image.load("C:\\mxcmaterials\\add-94ef816b-a00e-4d22-ac7d-f5e0202cd2c6.png")
cut = pygame.image.load("C:\\mxcmaterials\\cut-33883cba-d353-425f-ac09-2ea2128661c4.png")
eraser = pygame.image.load("C:\\mxcmaterials\\eraser-4e43409e-9bdf-4824-9e81-10e5bfd633f7.png")
save = pygame.image.load("C:\\mxcmaterials\\save-c5212934-1c7e-4881-8539-dfe073d1e45d.png")

sc.blit(up,(0,0))
sc.blit(clear,(100,50))
sc.blit(add,(180,50))
sc.blit(cut,(260,50))
sc.blit(eraser,(340,50))
sc.blit(save,(420,50))

pygame.draw.rect(sc,(255 ,225 ,255),(520,30,40,40))
pygame.draw.rect(sc,(255, 250, 205),(580,30,40,40))
pygame.draw.rect(sc,(135, 206, 255),(640,30,40,40))

pygame.display.update()

pen_colour=(255, 225 ,255)
pen_size=10
line = False
while True:
    sc.blit(up,(0,0))
    sc.blit(clear,(100,50))
    sc.blit(add,(180,50))
    sc.blit(cut,(260,50))
    sc.blit(eraser,(340,50))
    sc.blit(save,(420,50))
    
    pygame.draw.rect(sc,(255, 225, 255),(520,30,40,40))
    pygame.draw.rect(sc,(255, 250, 205),(580,30,40,40))
    pygame.draw.rect(sc,(135, 206, 255),(640,30,40,40))
    pygame.display.update()
    
    for event in pygame.event.get():
        x,y=pygame.mouse.get_pos()
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            if 100<x<140 and 50 <y< 100:
                sc.fill((255,255,255))
            if 180<x<220 and 50<y<90:
                pen_size+=2
            if 260<x<300 and 50<y<90:
                pen_size-=2
                if pen_size<=0:
                    pen_size=1
            if 340<x<380 and 50<y<100:
                pen_colour=(255, 255, 255)
            if 520<x<560 and 30<y<70:
                pen_colour=(255, 225, 255)
            if 580<x<620 and 30<y<70:
                pen_colour=(255, 250, 205)
            if 640<x<680 and 30<y<70:
                pen_colour=(135, 206, 255)
            if 420<x<460 and 50<y<100:
                pygame.image.save(sc,r"C:\Users\hqr_c\Desktop\pic.png")
                print("saved successfully")
            pygame.draw.circle(sc,pen_colour,(x,y),pen_size)
            pygame.display.update()
            line= True   
        elif event.type==pygame.MOUSEMOTION:
            if line==True:
                pygame.draw.circle(sc,(pen_colour),(x,y),pen_size)
                pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            line= False
input()

import pygame
import random
import math

pygame.init()

size = length, width = 800, 600
screen = pygame.display.set_mode(size)

guy_with_mouth_open = pygame.image.load("C:\\Users\\mmura\\PycharmProjects\\pythonProject\\guy with mouth open.png")

crunch_sound = pygame.mixer.Sound("D:\\Eating Crunch Chips sound effect no copyright-[AudioTrimmer.com].mp3")

default_guy_size = (length//8, width//8)
image = pygame.transform.scale(guy_with_mouth_open, default_guy_size)
guy_mouth_rect = image.get_rect(center=(length//2, width//2))

guyclosed = pygame.image.load("D:\\image.png")
guyclosed = pygame.transform.scale(guyclosed, default_guy_size)
guyclose_rect = guyclosed.get_rect()

apple = pygame.image.load("D:\\apple.png")
apple = pygame.transform.scale(apple, default_guy_size)
apple_radius = min(length, width)//15
apple_pos = (random.randint(apple_radius, length - apple_radius), random.randint(apple_radius, width - apple_radius))

counter_font = pygame.font.Font(None, 100)
guy_speed = 1
counter = 0

def eat():
    crunch_sound.play()
    global counter
    counter+= 1
    screen.fill((0, 0, 0))
    screen.blit(guyclosed, guy_mouth_rect)
    pygame.display.update()
    pygame.time.wait(300)
    screen.fill((0, 0, 0))
    screen.blit(guyclosed, guy_mouth_rect)
    pygame.display.update()
    pygame.time.wait(300)
    screen.fill((0, 0, 0))
    screen.blit(image, guy_mouth_rect)
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    apple_pos = (apple_pos[0] + random.randint(-1, 1), apple_pos[1] + random.randint(-1, 1))
    apple_pos = (min(max(apple_radius, apple_pos[0]), length - apple_radius), min(max(apple_radius, apple_pos[1]), width - apple_radius))

    if math.sqrt((guy_mouth_rect.center[0]-apple_pos[0])**2+(guy_mouth_rect.center[1]-apple_pos[1])**2) <= apple_radius:
        eat()
        apple_pos = (random.randint(apple_radius, length - apple_radius), random.randint(apple_radius, width - apple_radius))



    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if guy_mouth_rect.top>=0:
            guy_mouth_rect.move_ip(0,-guy_speed)
    if keys[pygame.K_s]:
        if guy_mouth_rect.bottom<=width:
            guy_mouth_rect.move_ip(0, guy_speed)
    if keys[pygame.K_a]:
        if guy_mouth_rect.left>=0:
            guy_mouth_rect.move_ip(-guy_speed, 0)
    if keys[pygame.K_d]:
        if guy_mouth_rect.right<=length:
            guy_mouth_rect.move_ip(guy_speed, 0)




    screen.fill((0,0,0))
    screen.blit(image, guy_mouth_rect)
    screen.blit(apple, apple_pos)

    counter_text = f"{counter}"
    counter_surface = counter_font.render(counter_text, True, (255, 255, 255))
    counter_pos = counter_surface.get_rect(center=(length / 1.2, width/1.2))
    screen.blit(counter_surface, counter_pos)

    pygame.display.update()

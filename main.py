import pygame
from sys import exit
from random import randint
def spawn(list):
    if list:
        for enemy in list:
            enemy.x-=7
            if enemy.bottom==200:
                screen.blit(fly_surf,enemy)
            else:
                screen.blit(snail, enemy)

        list=[enemy for enemy in list if enemy.x>-100]
        return list
    else: return []
def display_score():
    current_time= pygame.time.get_ticks()-start_time
    score=int(current_time/100)
    score_surface = font.render(f'Score:{score}', True, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 100))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 100)
    screen.blit(score_surface, score_rect)
    return score
def collisions(player,obstacle):
    if obstacle:
        for enemy in obstacle:
            if player.colliderect(enemy):
                return False
        return True
    else: return True
def player_animation():
    global player_index,player_img
    if player_rect.bottom<300:
        player_img=player_jump
    else:
        player_index+=0.1
        if player_index>=len(player_walk):player_index=0
        player_img=player_walk[int(player_index)]

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('PYGAME')
clock = pygame.time.Clock()
font=pygame.font.Font('font/Pixeltype.ttf',50)
game_active=False
start_time=0
score=0

Sky_img= pygame.image.load('graphics/Sky.png').convert()
Ground_img=pygame.image.load('graphics/ground.png').convert()
lose_img=pygame.image.load('graphics/loser.jpeg').convert()


#enemy

snail=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
fly_surf=pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
enemy_list=[]

player_walk1=pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_walk2=pygame.image.load('graphics/Player/player_walk_2.png').convert_alpha()
player_jump=pygame.image.load('graphics/Player/jump.png').convert_alpha()
player_walk=[player_walk1,player_walk2]
player_index=0
player_img=player_walk[player_index]
player_rect=player_img.get_rect(midbottom=(80, 300))
player_gravity=0

# intro
player_stand=pygame.image.load('graphics/Player/player_stand.png')
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400,200))

title_surface=font.render("Dino game 2",True,(64,64,64))
title_surface=pygame.transform.scale2x(title_surface)
title_rect=title_surface.get_rect(center=(400,70))

text_surface=font.render("Press space to play",True,(64,64,64))
text_surface=pygame.transform.rotozoom(text_surface,0,1.5)
text_rect=text_surface.get_rect(center=(400,350))

# timer
obstacal_timer=pygame.USEREVENT+1
pygame.time.set_timer(obstacal_timer,1700)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type== pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom>=300:
                    player_gravity=-20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_active=True
                    start_time=pygame.time.get_ticks()
        if event.type== obstacal_timer and game_active:
            if randint(0,2):
                enemy_list.append(snail.get_rect(midbottom=(randint(900,1000),300)))
            else:
                enemy_list.append(fly_surf.get_rect(midbottom=(randint(900,1000),200)))


    if game_active:
        score = display_score()
        screen.blit(Sky_img,(0,0))
        screen.blit(Ground_img, (0,300))

        display_score()
        enemy_list=spawn(enemy_list)


        # player
        player_gravity+=1
        player_rect.bottom+=player_gravity
        player_animation()
        if player_rect.bottom>=300: player_rect.bottom=300
        screen.blit(player_img, player_rect)
        game_active=collisions(player_rect,enemy_list )

    else:
        score_surface=font.render(f'Your score: {score}',False,(64,64,64))
        score_surface_rect=score_surface.get_rect(center=(400,350))
        screen.fill((94,129,162))
        screen.blit(title_surface, title_rect)
        screen.blit(player_stand,player_stand_rect)
        enemy_list.clear()
        player_rect.midbottom=(80,300)
        player_gravity=0
        if score == 0 :
            screen.blit(text_surface, text_rect)
        else:
            screen.blit(score_surface,score_surface_rect)
    pygame.display.update()
    clock.tick(60)


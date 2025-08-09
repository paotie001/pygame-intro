import pygame
from sys import exit

def display_score():
    current_time= pygame.time.get_ticks()-start_time
    score=int(current_time/100)
    score_surface = font.render(f'Score:{score}', True, (64, 64, 64))
    score_rect = score_surface.get_rect(center=(400, 100))
    pygame.draw.rect(screen, '#c0e8ec', score_rect)
    pygame.draw.rect(screen, '#c0e8ec', score_rect, 100)
    screen.blit(score_surface, score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('PYGAME')
clock = pygame.time.Clock()
font=pygame.font.Font('font/Pixeltype.ttf',50)
game_active=True
start_time=0

Sky_img= pygame.image.load('graphics/Sky.png').convert()
Ground_img=pygame.image.load('graphics/ground.png').convert()
lose_img=pygame.image.load('graphics/loser.jpeg').convert()

text_surface=font.render("Press space to play",True,(64,64,64))
text_rect=text_surface.get_rect(center=(400,100))

snail=pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect=snail.get_rect(midbottom=(600,300))

player_img=pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect=player_img.get_rect(midbottom=(80,300))
player_gravity=0

# intro
player_stand=pygame.image.load('graphics/Player/player_stand.png')
player_stand=pygame.transform.scale2x(player_stand)
player_stand_rect=player_stand.get_rect(center=(400,200))
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
                    snail_rect.right=800
                    start_time=pygame.time.get_ticks()
    if game_active:
        screen.blit(Sky_img,(0,0))
        screen.blit(Ground_img, (0,300))

        display_score()

        snail_rect.right-=4
        if snail_rect.right<0: snail_rect.left=800
        screen.blit(snail, snail_rect)

        #player
        player_gravity+=1
        player_rect.bottom+=player_gravity
        if player_rect.bottom>=300: player_rect.bottom=300
        screen.blit(player_img,player_rect)
        #collison
        if snail_rect.colliderect(player_rect):
            game_active=False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)



    pygame.display.update()
    clock.tick(60)


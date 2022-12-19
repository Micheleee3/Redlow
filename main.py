import pygame, sys
import pytmx

SCREEN_SIZE = (1280,720)

pygame.init()

screen = pygame.display.set_mode(SCREEN_SIZE, pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE)
clock = pygame.time.Clock()
pygame.display.set_caption("Redlow")


player_location= [50, 50]
player_image = pygame.image.load("assets/player.png")
player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test = pygame.Rect(100, 100, 100, 50)
momentum = 0
moving_right = False
moving_left = False

bg = pygame.image.load("assets/sky.png")

gameMap = pytmx.load_pygame("levels/l1.tmx")

dimX, dimY = 32, 32

tile_collision = []

game_run = True
while game_run:

    screen.blit(bg, (0,0))
    for layer in gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = gameMap.get_tile_image_by_gid(gid)
                if(tile != None):
                    tile = pygame.transform.scale(tile, (dimX, dimY))
                    screen.blit(tile, (x * dimX, y * dimY))
                    tile_collision.append((pygame.Rect(x * dimX, y * dimY, dimX, dimY)))

    for tile_rect in tile_collision:
        if(player_rect.colliderect( tile_rect )):
            momentum = 0
        else:
            player_location[1] += 0.00001

    

    screen.blit(player_image, (player_location[0], player_location[1]))
    if player_rect.colliderect(test):
        print("collided")
        pygame.draw.rect(screen, (255, 0, 0), test)
    else:
        pygame.draw.rect(screen, (0, 0, 0), test)
        player_rect.x = player_location[0]
        player_rect.y = player_location[1]
    
    if moving_right == True:
        player_location[0] += 4

    if moving_left == True:
        player_location[0] -= 4

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
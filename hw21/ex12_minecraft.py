import pygame
from pathlib import Path

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Збір предметів та інвентар")

images_folder = Path(__file__).parent.joinpath("images/craft")

player_img_path = images_folder.joinpath("player.png")
player_img = pygame.image.load(player_img_path)
player_img = pygame.transform.scale(player_img, (100, 100))

pickaxe_img_path = images_folder.joinpath("pickaxe.png")
pickaxe_img = pygame.image.load(pickaxe_img_path)
pickaxe_img = pygame.transform.scale(pickaxe_img, (70, 70))

axe_img_path = images_folder.joinpath("axe.jpg")
axe_img = pygame.image.load(axe_img_path)
axe_img = pygame.transform.scale(axe_img, (70, 70))

wood_img_path = images_folder.joinpath("wood.png")
wood_img = pygame.image.load(wood_img_path)
wood_img = pygame.transform.scale(wood_img, (70, 70))

stone_img_path = images_folder.joinpath("stone.png")
stone_img = pygame.image.load(stone_img_path)
stone_img = pygame.transform.scale(stone_img, (70, 70))

chest_img_path = images_folder.joinpath("chest.png")
chest_img = pygame.image.load(chest_img_path)
chest_img = pygame.transform.scale(chest_img, (100, 100))



player = pygame.Rect(100, 100, 100, 100)
chest = pygame.Rect(100, 200, 100, 100)
pickaxe = pygame.Rect(600, 450, 70, 70)
axe = pygame.Rect(600, 100, 70, 70)
woods = [
    pygame.Rect(300, 400, 70, 70),
    pygame.Rect(500, 200, 70, 70)
]
stones = [
    pygame.Rect(500, 400, 70, 70),
    pygame.Rect(100, 500, 70, 70),
    pygame.Rect(300, 200, 70, 70)
]
inventory = {"Pickaxe": 0, "Axe": 0, "Wood": 0, "Stone": 0}

chest_opened = False
has_axe = False
has_pickaxe = False
items_collected = 0
items_goal = 200

clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
win_font = pygame.font.Font(None, 80)

running = True
you_win = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))

    if you_win:
        win_text = win_font.render("YOU WIN", True, (0, 0, 0))
        win_rect = win_text.get_rect()
        win_rect.center = (400, 300)
        screen.blit(win_text, win_rect)
        pygame.display.flip()
        continue
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    if pickaxe and player.colliderect(pickaxe):
        if keys[pygame.K_e]:
            has_pickaxe = True
            inventory["Pickaxe"] = 1
            pickaxe = None

    if axe and player.colliderect(axe):
        if keys[pygame.K_e]:
            has_axe = True
            inventory["Axe"] = 1
            axe = None

    if has_axe:
        for wood in woods[:]:
            if player.colliderect(wood):
                if keys[pygame.K_SPACE]:
                    inventory["Wood"] += 1

    if has_pickaxe:
        for stone in stones[:]:
            if player.colliderect(stone):
                if keys[pygame.K_SPACE]:
                    inventory["Stone"] += 1


    if inventory["Wood"] >= items_goal and player.colliderect(chest):
        you_win = True

    screen.blit(chest_img, chest)

    if pickaxe:
        screen.blit(pickaxe_img, pickaxe)

    if axe:
        screen.blit(axe_img, axe)

    for wood in woods:
        screen.blit(wood_img, wood)

    for stone in stones:
        screen.blit(stone_img, stone)        

    screen.blit(player_img, player)

    text = font.render(
        f"Wood: {inventory['Wood']}",
        True, (0, 0, 0)
    )
    screen.blit(text, (10, 10))

    text = font.render(
        f"Stone: {inventory["Stone"]}",
        True, (0, 0, 0)
    )
    screen.blit(text, (10, 40))

    if has_pickaxe:
        pickaxe_text = font.render("Pickaxe: Yes", True, (0, 0, 0))
    else:
        pickaxe_text = font.render("Pickaxe: No", True, (0, 0, 0))
    screen.blit(pickaxe_text, (10, 70))

    if has_axe:
        axe_text = font.render("Axe: Yes", True, (0, 0, 0))
    else:
        axe_text = font.render("Axe: No", True, (0, 0, 0))
    screen.blit(axe_text, (10, 100))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

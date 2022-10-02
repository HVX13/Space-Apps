import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("JWST Viewer")

BG_original_1 = pygame.image.load("assets/pia20027_updated.jpg")
BG_1 = pygame.transform.scale(BG_original_1, (1280, 720))

BG_original_2 = pygame.image.load("assets/pia17832.jpg")
BG_2 = pygame.transform.scale(BG_original_2, (1280, 720))

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/SPhanithFonterTouch-EzJ4.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG_2, (0,0))

        PLAY_TEXT = get_font(50).render("Choose A Level", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))

        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        LEVEL1_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(400, 370),
                             text_input="LEVEL 1", font=get_font(25), base_color="#f7f3f2", hovering_color="#13ed1a")


        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(35), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        LEVEL1_BUTTON.changeColor(PLAY_MOUSE_POS)
        LEVEL1_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if LEVEL1_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    LEVEL1()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def LEVEL1():
    while True:
        LEVEL1_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG_2, (0, 0))

        LEVEL1_TEXT = get_font(50).render("Guess which image was taken by the JWST", True, "White")
        LEVEL1_RECT = LEVEL1_TEXT.get_rect(center=(640, 100))

        SCREEN.blit(LEVEL1_TEXT, LEVEL1_RECT)

        LEVEL1_IMAGE1_original = pygame.image.load("assets/pia18848-wisefacepalm.jpg")
        LEVEL1_IMAGE1 = pygame.transform.scale(LEVEL1_IMAGE1_original, (300, 300))

        SCREEN.blit(LEVEL1_IMAGE1, (300, 200))

        LEVEL1_IMAGE2_original = pygame.image.load("assets/pia18848-wisefacepalm_blur.jpg")
        LEVEL1_IMAGE2= pygame.transform.scale(LEVEL1_IMAGE2_original, (300, 300))

        SCREEN.blit(LEVEL1_IMAGE2, (700, 200))



        LEVEL1_BACK = Button(image=None, pos=(640, 560),
                           text_input="BACK", font=get_font(35), base_color="White", hovering_color="Green")

        LEVEL1_BACK.changeColor(LEVEL1_MOUSE_POS)
        LEVEL1_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LEVEL1_BACK.checkForInput(LEVEL1_MOUSE_POS):
                    play()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG_1, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#dfed13")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(25), base_color="#f7f3f2", hovering_color="#13ed1a")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(25), base_color="#f7f3f2", hovering_color="#13ed1a")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(25), base_color="#f7f3f2", hovering_color="#13ed1a")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()
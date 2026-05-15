import pygame
import config
import objects

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
# Might actually change displays to be all platforms?

clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)
volume = 50
running = True
options_active = False
start_menu = True



# Button Rects
menu_rect = pygame.Rect(200, 150, 400, 300)
back_button = pygame.Rect(300, 350, 200, 50)
notes = []


Hitbox = pygame.Rect(440, 100, 400, 100)
Lane = pygame.Rect(442, 200, 100, 500)
Lane2 = pygame.Rect(542, 200, 100, 500)
Lane3 = pygame.Rect(642, 200, 100, 500)
Lane4 = pygame.Rect(741, 200, 100, 500)
# Box stuff v2

#Test note Spawned on the left 
test_note = [496, 700]  # [x, y]
notes.append(test_note)

while running:
    # poll for events
    # pygame.QUIT event means user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and options_active:
            if back_button.collidepoint(event.pos):
                options_active = False

    # fill the screen with a color to wipe away anything from last frame 
    screen.fill("purple")
    

    # RENDER YOUR GAME HERE
    #Maybe a start screen? then options, cause obviously we can make both a downscroll, and upscroll?
    
    
    #Downscroll would be the arrows go from the top of the screen to the bottom, and upscroll would be the opposite. Maybe we can have a toggle for that in the options menu?
    if start_menu == True:
        start_menu_color = (255, 0, 0)  # Red color for the start menu
        start_menu_rect = pygame.Rect(0, 0, 1280, 720)  # Full screen rectangle
        pygame.draw.rect(screen, start_menu_color, start_menu_rect)
        # Now the buttons..
        Start_button = pygame.Rect(540, 300, 200, 50) # Start button Goes middle..
        Options_button = pygame.Rect(540, 400, 200, 50) # Options button goes middle but lower than the start button
        pygame.draw.rect(screen, (0, 255, 0), Start_button) # Green color for the start button
        
        
        if Start_button.collidepoint(pygame.mouse.get_pos()):
            if event.type == pygame.MOUSEBUTTONDOWN:
                    start_menu = False
                    print("hi")
    if start_menu == False:
        pygame.draw.rect(screen, (0, 0, 0), Lane)
        pygame.draw.rect(screen, (0, 0, 0), Lane2)
        pygame.draw.rect(screen, (0, 0, 0), Lane3)
        pygame.draw.rect(screen, (0, 0, 0), Lane4)

        
        # 2. Draw moving notes (middle layer)
        for note in notes:
            pygame.draw.circle(screen, (255, 255, 255), (note[0], note[1]), 25)
            
        pygame.draw.rect(screen, (0, 0, 0), Hitbox)
        Arrows = pygame.draw.circle(screen, (255, 0, 0), (496, 150), 30)
        
        pygame.draw.circle(screen, (255, 0, 0), (496, 150), 30)   # Red - Left
        pygame.draw.circle(screen, (0, 0, 255), (592, 150), 30)   # Blue - Down
        pygame.draw.circle(screen, (0, 255, 0), (688, 150), 30)   # Green - Up 
        pygame.draw.circle(screen, (255, 255, 0), (784, 150), 30) # Yellow - Right
        
        
        
        # pygame.draw.circle(screen, (0, 0, 255), (592, 650), 30)
        # pygame.draw.circle(screen, (0, 0, 255), (592, 650), 30)
        # pygame.draw.circle(screen, (0, 255, 0), (688, 650), 30)
        # pygame.draw.circle(screen, (255, 255, 0), (784, 650), 30)
        
        
        
                
    
    
    # pygame.draw.rect(screen, (0, 0, 255), Options_button) # Blue color for the options button
    # pygame.draw.rect(screen, (255, 255, 0), (540, 500, 200, 50)) # Yellow color for the quit button
    # if Start_button.collidepoint(pygame.mouse.get_pos()):
    #          if event.type == pygame.MOUSEBUTTONDOWN:
    #              if event.button == 1:
    #                 print("Start button clicked!")
    #                 # Just move to game state.
    # if Options_button.collidepoint(pygame.mouse.get_pos()):
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         if event.button == 1:
    #             print("Options Clicked!")
    #             options_active = True
                
    # if options_active:
    #     # Semi-transparent Surface.. (Background!)
    #     overlay = pygame.Surface((800, 600))
    #     overlay.set_alpha(128)
    #     overlay.fill((0, 0, 0))
    #     screen.blit(overlay, (0, 0))
        
    #     # Draw Menu Box!! (Maybe i can use this as a Default..?)
    #     pygame.draw.rect(screen, (200, 200, 200), menu_rect)
    #     pygame.draw.rect(screen, (100, 100, 100), back_button)
        
        
    #     #Teeeext!!
    #     vol_text = font.render(f"Volume: {volume}", True, (0, 0, 0))
    #     back_text = font.render("Back", True, (255, 255, 255))
    #     screen.blit(vol_text, (250, 200))
    #     screen.blit(back_text, (350, 555))
    # This'll just be the judgement ine where the arrows fall down to
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    
pygame.quit()












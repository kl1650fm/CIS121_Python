'''
CIS121 Project: PuzzleWorld
Description:
    PuzzlyWorld - a simple 3x3 sliding puzzle game.
    Solve the puzzle to reveal a hidden message! 

Group Members : Tina Kim, Seonmin Kim, Kday Manecha Diomande
Date : 12052025

Hint: whoever is grading this, try to stop the shuffle early to see the hidden message quickly!
'''

import pygame, random

user_name = input("Welcome to PuzzlyWorld!\nWrite your name to begin:\n")

# Intro Screen and Greeting
class GameApp:
    def __init__(self, user_name):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300)) 
        self.user_name = user_name                         
        self.font = pygame.font.Font("Lilmarie.ttf", 40)
        self.small_font = pygame.font.Font("Lilmarie.ttf", 20)
        self.smaller_font = pygame.font.Font("Lilmarie.ttf", 15)

    # Draws the introduction screen
    def begin_screen(self):
        self.screen.fill((150, 107, 147))

        title = self.font.render(f"Hello {self.user_name}!", True, (99, 30, 96))
        message = self.small_font.render("GAME GUIDE:", True, (124, 65, 120))
        message2 = self.small_font.render("SPACE", True, (124, 65, 120))
        message3 = self.small_font.render("1.Begin 2.Shuffle 3.Stop", True, (124, 65, 120))
        message4 = self.smaller_font.render("**Solve the puzzle to see a hidden message**", True, (124, 65, 120))


        title_middle = title.get_rect(center=(self.screen.get_width() // 2, 100))
        message_middle = message.get_rect(center=(self.screen.get_width() // 2, 135))
        message2_middle = message2.get_rect(center=(self.screen.get_width()// 2, 150))
        message3_middle = message3.get_rect(center=(self.screen.get_width()// 2, 160))
        message4_middle = message4.get_rect(center=(self.screen.get_width()// 2, 280))

        space_width = 80
        space_height = 30
        space_x = (self.screen.get_width() - space_width) // 2 
        space_y = 180
        
        pygame.draw.rect(self.screen, (240, 220, 240), (space_x, space_y, space_width, space_height), border_radius=5)
        message2_middle = message2.get_rect(center=(space_x + space_width // 2, space_y + space_height // 2))

        self.screen.blit(title, title_middle)
        self.screen.blit(message, message_middle)
        self.screen.blit(message2, message2_middle)
        self.screen.blit(message3, message3_middle)
        self.screen.blit(message4, message4_middle)

    def show_hidden_message(self):
        with open("HiddenMessage.txt", "r+") as f:
            lines = f.readlines()

        if lines:
            lines[1] = lines[1].strip() + "Player:" + user_name

        screen.fill((150, 107, 147))
        font = pygame.font.Font("Lilmarie.ttf", 20)

        # 화면 중앙 기준
        center_x = screen.get_width() // 2

        # 전체 메시지 높이를 계산해서 "Y 중앙 배치"
        line_height = 40
        total_height = len(lines) * line_height
        start_y = (screen.get_height() - total_height) // 2

        for i, line in enumerate(lines):
            text = font.render(line.strip(), True, (99, 30, 96))

            # 가운데 정렬
            rect = text.get_rect(center=(center_x, start_y + i * line_height))
            screen.blit(text, rect)

        pygame.display.update()

    # Loop until SPACE is pressed, after space, the game starts
    def intro(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        running = False

            self.begin_screen()
            pygame.display.update()

app = GameApp(user_name)
app.intro()
            
# 1. Game reset
pygame.init()

# Import image
puzzleImage = pygame.image.load("puzzle.png")
puzzleSize = puzzleImage.get_size()
puzzleSize = (round(puzzleSize[0]*0.25), round(puzzleSize[1]*0.25))
puzzleImage = pygame.transform.smoothscale(puzzleImage, puzzleSize)

# Create a puzzleLlist
iNum = 3
jNum = 3
puzzleList = []
puzzleListInit = []
for i in range(iNum):
    tempList = []
    tempListInit = []
    for j in range(jNum):
        w = puzzleSize[0] // iNum
        h = puzzleSize[1] // jNum
        x = i*w
        y = j*h
        partImage = puzzleImage.subsurface((x,y,w,h))
        temp = {
            "num": j*jNum+i+1,
            "image": partImage,
            "position": (x,y)
        }
        tempList.append(temp)
        tempListInit.append(j*jNum+i+1)
    puzzleList.append(tempList)
    puzzleListInit.append(tempListInit)
puzzleList[-1][-1]["num"] = 0
puzzleListInit[-1][-1] = 0
black_screen = pygame.Surface((w,h))
black_screen.fill((0,0,0))
puzzleList[-1][-1]["image"] = black_screen

# 2. Game Options Setting
size = puzzleSize
screen = pygame.display.set_mode(size)
title = "puzzle"
pygame.display.set_caption(title)

# 3. Required In-Game Setting
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
direction = {
        "left":(-1,0), "right":(1,0),
        "up":(0,-1), "down":(0,1)
    }
keyPress = False
mix = False
gameOver = False
spaceNum = 0
exit = False

# 4. Main Event
while not exit:
    # 4-1. FPS
    clock.tick(60)
    # 4-2. Multiple Input Detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            keyName = pygame.key.name(event.key)
            if keyName == "space":
                mix = not mix
                spaceNum += 1
            for key in direction.keys():
                if key == keyName:
                    keyPress = True

    # 4-3. Input and Time-Based Changes
    # Find Blank
    for i in range(iNum):
        for j in range(jNum):
            if puzzleList[i][j]["num"] == 0:
                blank = (i,j)
    # Change
    if keyPress == True or mix == True:
        if mix == True:
            randomIndex = random.randrange(0,4)
            keyName = list(direction.keys())[randomIndex]
        i, j = blank
        ii, jj = direction[keyName]
        iNew, jNew = i+ii, j+jj
        if iNew>=0 and iNew<iNum and jNew >= 0 and jNew<jNum:
            puzzleList[i][j]["num"], puzzleList[iNew][jNew]["num"] = puzzleList[iNew][jNew]["num"], puzzleList[i][j]["num"]
            puzzleList[i][j]["image"], puzzleList[iNew][jNew]["image"] = puzzleList[iNew][jNew]["image"], puzzleList[i][j]["image"]
            # num, image, position
        keyPress = False
    # Game End Conditions
    if spaceNum >= 2:
        same = True
        for i in range(iNum):
            for j in range(jNum):
                if puzzleList[i][j]["num"] != puzzleListInit[i][j]:
                    same = False
        if same == True:
            gameOver = True

    # 4-4. Draw
    screen.fill(white)
    # Draw Puzzle
    for i in range(iNum):
        for j in range(jNum):
            image = puzzleList[i][j]["image"]
            position = puzzleList[i][j]["position"]
            screen.blit(image, position)
            x,y = position
            A = (x, y)
            B = (x+w, y)
            C = (x, y+h)
            D = (x+w, y+h)
            pygame.draw.line(screen, white, A, B, 3)
            pygame.draw.line(screen, white, A, C, 3)
            pygame.draw.line(screen, white, D, B, 3)
            pygame.draw.line(screen, white, D, C, 3)
    #if gameOver == True:
        #screen.blit(puzzleImage, (0,0))
    if gameOver == True:
        screen.blit(puzzleImage, (0,0))
        pygame.display.flip()    
        pygame.time.delay(1000) 

        app.show_hidden_message()

    # 메시지를 본 후 프로그램 종료
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit = True
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    exit = True
                    waiting = False
    # 4-5. Update
    pygame.display.flip()

#5. End Game
pygame.quit()
import pygame, sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Vanquish')
win = pygame.display.set_mode((1280, 700))
clock = pygame.time.Clock()


#Backgrounds
mainbg = pygame.image.load('Backgrounds/MainMenu.jpg')
settingsbg = pygame.image.load('Backgrounds/Settings.jpg')
controlsbg = pygame.image.load('Backgrounds/Controls.jpg')
pausebg = pygame.image.load('Backgrounds/Pause.jpg')
arcadebg = pygame.image.load('Backgrounds/Arcade.jpg')
storybg = pygame.image.load('Backgrounds/Story.jpg')
charselectbg = pygame.image.load('Backgrounds/CharacterSelection.jpg')
drawbg = pygame.image.load('Backgrounds/draw.jpg')
endlessbg = pygame.image.load('Backgrounds/endless.jpg')

#Win Backgrounds
c1Winbg = pygame.image.load('Backgrounds/c1_win.jpg')
c2Winbg = pygame.image.load('Backgrounds/c2_win.jpg')
c3Winbg = pygame.image.load('Backgrounds/c3_win.jpg')
c4Winbg = pygame.image.load('Backgrounds/c4_win.jpg')
c5Winbg = pygame.image.load('Backgrounds/c5_win.jpg')
c6Winbg = pygame.image.load('Backgrounds/c6_win.jpg')

#Character Summary Backgrounds
c1Summarybg = pygame.image.load('Backgrounds/c1_st.jpg')
c2Summarybg = pygame.image.load('Backgrounds/c2_st.jpg')
c3Summarybg = pygame.image.load('Backgrounds/c3_st.jpg')
c4Summarybg = pygame.image.load('Backgrounds/c4_st.jpg')
c5Summarybg = pygame.image.load('Backgrounds/c5_st.jpg')
c6Summarybg = pygame.image.load('Backgrounds/c6_st.jpg')

#Colours
white = (255,255,255) 
black = (0,0,0)
grey = (128,128,128)
yellow = (255,255,0)
blue = (0,0,255) 
red = (255,0,0) 
orange = (255,165,0)
green = (0,200,0)
brightgreen = (0,255,0)
whitesmoke = (245,245,245)

#Maps
def map_1():
    map1 = pygame.image.load('Maps/map1.gif')
    win.blit(map1, (0,0))
def map_2():
    map2 = pygame.image.load('Maps/map2.gif')
    win.blit(map2, (0,0))
def map_3():
    map3 = pygame.image.load('Maps/map3.gif')
    win.blit(map3, (0,0))
def map_4():
    map4 = pygame.image.load('Maps/map4.gif')
    win.blit(map4, (0,0))
def map_5():
    map5 = pygame.image.load('Maps/map5.gif')
    win.blit(map5, (0,0))
def map_6():
    map6 = pygame.image.load('Maps/map6.gif')
    win.blit(map6, (0,0))
def map_7():
    map7 = pygame.image.load('Maps/map7.gif')
    win.blit(map7, (0,0))
def map_8():
    map8 = pygame.image.load('Maps/map8.jpg')
    win.blit(map8, (0,0))
def map_9():
    map9 = pygame.image.load('Maps/map9.jpg')
    win.blit(map9, (0,0))
def map_10():
    map10 = pygame.image.load('Maps/map10.jpg')
    win.blit(map10, (0,0))

#Sound effects - Game
fight_SE = pygame.mixer.Sound('Sound/fight.wav')
KO_SE = pygame.mixer.Sound('Sound/ko.wav')
punch_SE = pygame.mixer.Sound('Sound/punch.wav')  
kick_SE = pygame.mixer.Sound('Sound/kick.wav')


#Draw Text
font = pygame.font.SysFont("Evil Empire",40)
font2 = pygame.font.SysFont("comicsansms",20)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


#Images of characters
c1_large_icon_load = pygame.image.load('Extras/Char1_image.png')
c2_large_icon_load = pygame.image.load('Extras/Char2_image.png')
c3_large_icon_load = pygame.image.load('Extras/Char3_image.png')
c4_large_icon_load = pygame.image.load('Extras/Char4_image.png')
c5_large_icon_load = pygame.image.load('Extras/Char5_image.png')
c6_large_icon_load = pygame.image.load('Extras/Char6_image.png')


#List for the characters
fighters = []

#Display Text
font = pygame.font.SysFont("Evil Empire",40)
def char1_name():
    C1_name = font.render("Kazuo Ishigami", True, red)
    win.blit(C1_name,(200,25))
    if len(fighters) < 2:
        fighters.append(char1)
def char2_name():
    C2_name = font.render("Kira Okita", True, blue)
    win.blit(C2_name,(900,25))
    if len(fighters) < 2:
        fighters.append(char2)
def char3_name():
    C3_name = font.render("Atlas Chrollo", True, red)
    win.blit(C3_name,(200,25))
    if len(fighters) < 2:
        fighters.append(char3)
def char4_name():
    C4_name = font.render("Amani Miyamisui", True, blue)
    win.blit(C4_name,(900,25))
    if len(fighters) < 2:
        fighters.append(char4)
def char5_name():
    C5_name = font.render("Hisoka Yasumoto", True, red)
    win.blit(C5_name,(200,25))
    if len(fighters) < 2:
        fighters.append(char5)
def char6_name():
    C6_name = font.render("Ajin Nakamura", True, blue)
    win.blit(C6_name,(900,25))
    if len(fighters) < 2:
        fighters.append(char6)



#Character 1
imageone_load = pygame.image.load('Character1/image1.png')
imageone = pygame.transform.scale(imageone_load, (60,60))

walkRight_load = pygame.image.load('Character1/R1.png')
walkRight = pygame.transform.scale(walkRight_load, (250,500))

walkLeft_load = pygame.image.load('Character1/L1.png')
walkLeft = pygame.transform.scale(walkLeft_load, (250,500))

charone_load = pygame.image.load('Character1/standing1.png')
charone = pygame.transform.scale(charone_load, (250,500))

atkPunch_load = pygame.image.load('Character1/P1.png')
atkPunch = pygame.transform.scale(atkPunch_load, (250,500))

atkKick_load = pygame.image.load('Character1/K1.png')
atkKick = pygame.transform.scale(atkKick_load, (200,500))

crouch_load = pygame.image.load('Character1/C1.png')
moveCrouch = pygame.transform.scale(crouch_load, (200,500))

damagetaken1_load = pygame.image.load('Character1/DT1.png')
damagetaken1 = pygame.transform.scale(damagetaken1_load, (250,500))

lose1_load = pygame.image.load('Character1/lose1.png')
lose1 = pygame.transform.scale(lose1_load, (250,500))


#Character 2
imagetwo_load = pygame.image.load('Character2/image2.png')
imagetwo = pygame.transform.scale(imagetwo_load, (50,50))

walkRight2_load1 = pygame.image.load('Character2/C2_R1.png')
walkRight2_load2 = pygame.image.load('Character2/C2_R2.png')
walkRight2_load3 = pygame.image.load('Character2/C2_R3.png')
walkRight2_load4 = pygame.image.load('Character2/C2_R4.png')
walkRight2_load5 = pygame.image.load('Character2/C2_R5.png')
walkRight2_load6 = pygame.image.load('Character2/C2_R6.png')
walkRight2_load7 = pygame.image.load('Character2/C2_R7.png')
walkRight2_load8 = pygame.image.load('Character2/C2_R8.png')
walkRight2_load9 = pygame.image.load('Character2/C2_R9.png')
walkRight2_size1 = pygame.transform.scale(walkRight2_load1, (200,400))
walkRight2_size2 = pygame.transform.scale(walkRight2_load2, (200,400))
walkRight2_size3 = pygame.transform.scale(walkRight2_load3, (200,400))
walkRight2_size4 = pygame.transform.scale(walkRight2_load4, (200,400))
walkRight2_size5 = pygame.transform.scale(walkRight2_load5, (200,400))
walkRight2_size6 = pygame.transform.scale(walkRight2_load6, (200,400))
walkRight2_size7 = pygame.transform.scale(walkRight2_load7, (200,400))
walkRight2_size8 = pygame.transform.scale(walkRight2_load8, (200,400))
walkRight2_size9 = pygame.transform.scale(walkRight2_load9, (200,400))
walkRight2 = [walkRight2_size1,walkRight2_size2,walkRight2_size3,walkRight2_size4,walkRight2_size5,walkRight2_size6,walkRight2_size7,walkRight2_size8,walkRight2_size9]


walkLeft2_load1 = pygame.image.load('Character2/C2_L1.png')
walkLeft2_load2 = pygame.image.load('Character2/C2_L2.png')
walkLeft2_load3 = pygame.image.load('Character2/C2_L3.png')
walkLeft2_load4 = pygame.image.load('Character2/C2_L4.png')
walkLeft2_load5 = pygame.image.load('Character2/C2_L5.png')
walkLeft2_load6 = pygame.image.load('Character2/C2_L6.png')
walkLeft2_load7 = pygame.image.load('Character2/C2_L7.png')
walkLeft2_load8 = pygame.image.load('Character2/C2_L8.png')
walkLeft2_load9 = pygame.image.load('Character2/C2_L9.png')
walkLeft2_size1 = pygame.transform.scale(walkLeft2_load1, (200,400))
walkLeft2_size2 = pygame.transform.scale(walkLeft2_load2, (200,400))
walkLeft2_size3 = pygame.transform.scale(walkLeft2_load3, (200,400))
walkLeft2_size4 = pygame.transform.scale(walkLeft2_load4, (200,400))
walkLeft2_size5 = pygame.transform.scale(walkLeft2_load5, (200,400))
walkLeft2_size6 = pygame.transform.scale(walkLeft2_load6, (200,400))
walkLeft2_size7 = pygame.transform.scale(walkLeft2_load7, (200,400))
walkLeft2_size8 = pygame.transform.scale(walkLeft2_load8, (200,400))
walkLeft2_size9 = pygame.transform.scale(walkLeft2_load9, (200,400))
walkLeft2 = [walkLeft2_size1,walkLeft2_size2,walkLeft2_size3,walkLeft2_size4,walkLeft2_size5,walkLeft2_size6,walkLeft2_size7,walkLeft2_size8,walkLeft2_size9]

chartwo_load = pygame.image.load('Character2/standing2.png')
chartwo = pygame.transform.scale(chartwo_load, (180,400))

atkPunch_load2 = pygame.image.load('Character2/P2.png')
atkPunch2 = pygame.transform.scale(atkPunch_load2, (300,400))

atkKick_load2 = pygame.image.load('Character2/K2.png')
atkKick2 = pygame.transform.scale(atkKick_load2, (300,400))

crouch_load2 = pygame.image.load('Character2/C2.png')
moveCrouch2 = pygame.transform.scale(crouch_load2, (300,350))

damagetaken2_load = pygame.image.load('Character2/DT2.png')
damagetaken2 = pygame.transform.scale(damagetaken2_load, (250,500))

lose2_load = pygame.image.load('Character2/lose2.png')
lose2 = pygame.transform.scale(lose2_load, (250,500))



#Character 3
imagethree_load = pygame.image.load('Character3/image3.png')
imagethree = pygame.transform.scale(imagethree_load, (50,50))

walkRight_load3 = pygame.image.load('Character3/C3_R1.png')
walkRight3 = pygame.transform.scale(walkRight_load3, (200,400))

walkLeft_load3 = pygame.image.load('Character3/C3_L1.png')
walkLeft3 = pygame.transform.scale(walkLeft_load3, (200,400))

charthree_load = pygame.image.load('Character3/standing3.png')
charthree = pygame.transform.scale(charthree_load, (220,410))

atkPunch_load3 = pygame.image.load('Character3/P3.png')
atkPunch3 = pygame.transform.scale(atkPunch_load3, (200,400))

atkKick_load3 = pygame.image.load('Character3/K3.png')
atkKick3 = pygame.transform.scale(atkKick_load3, (250,400))

crouch_load3 = pygame.image.load('Character3/C3.png')
moveCrouch3 = pygame.transform.scale(crouch_load3, (200,400))

damagetaken3_load = pygame.image.load('Character3/DT3.png')
damagetaken3 = pygame.transform.scale(damagetaken3_load, (250,500))

lose3_load = pygame.image.load('Character3/lose3.png')
lose3 = pygame.transform.scale(lose3_load, (250,500))


#Character 4
imagefour_load = pygame.image.load('Character4/image4.png')
imagefour = pygame.transform.scale(imagefour_load, (50,50))

walkRight_load4 = pygame.image.load('Character4/C4_R1.png')
walkRight4 = pygame.transform.scale(walkRight_load4, (175,425))

walkLeft_load4 = pygame.image.load('Character4/C4_L1.png')
walkLeft4 = pygame.transform.scale(walkLeft_load4, (175,425))

charfour_load = pygame.image.load('Character4/standing4.png')
charfour = pygame.transform.scale(charfour_load, (175,425))

atkPunch_load4 = pygame.image.load('Character4/P4.png')
atkPunch4 = pygame.transform.scale(atkPunch_load4, (200,425))

atkKick_load4 = pygame.image.load('Character4/K4.png')
atkKick4 = pygame.transform.scale(atkKick_load4, (200,425))

crouch_load4 = pygame.image.load('Character4/C4.png')
moveCrouch4 = pygame.transform.scale(crouch_load4, (250,425))

damagetaken4_load = pygame.image.load('Character4/DT4.png')
damagetaken4 = pygame.transform.scale(damagetaken4_load, (250,500))

lose4_load = pygame.image.load('Character4/lose4.png')
lose4 = pygame.transform.scale(lose4_load, (250,500))


#Character 5
imagefive_load = pygame.image.load('Character5/image5.png')
imagefive = pygame.transform.scale(imagefive_load, (75,50))

walkRight5_load1 = pygame.image.load('Character5/C5_R1.png')
walkRight5_load2 = pygame.image.load('Character5/C5_R2.png')
walkRight5_load3 = pygame.image.load('Character5/C5_R3.png')
walkRight5_load4 = pygame.image.load('Character5/C5_R4.png')
walkRight5_load5 = pygame.image.load('Character5/C5_R5.png')
walkRight5_load6 = pygame.image.load('Character5/C5_R6.png')
walkRight5_load7 = pygame.image.load('Character5/C5_R7.png')
walkRight5_load8 = pygame.image.load('Character5/C5_R8.png')
walkRight5_load9 = pygame.image.load('Character5/C5_R9.png')
walkRight5_size1 = pygame.transform.scale(walkRight5_load1, (200,400))
walkRight5_size2 = pygame.transform.scale(walkRight5_load2, (200,400))
walkRight5_size3 = pygame.transform.scale(walkRight5_load3, (200,400))
walkRight5_size4 = pygame.transform.scale(walkRight5_load4, (200,400))
walkRight5_size5 = pygame.transform.scale(walkRight5_load5, (200,400))
walkRight5_size6 = pygame.transform.scale(walkRight5_load6, (200,400))
walkRight5_size7 = pygame.transform.scale(walkRight5_load7, (200,400))
walkRight5_size8 = pygame.transform.scale(walkRight5_load8, (200,400))
walkRight5_size9 = pygame.transform.scale(walkRight5_load9, (200,400))
walkRight5 = [walkRight5_size1,walkRight5_size2,walkRight5_size3,walkRight5_size4,walkRight5_size5,walkRight5_size6,walkRight5_size7,walkRight5_size8,walkRight5_size9]


walkLeft5_load1 = pygame.image.load('Character5/C5_L1.png')
walkLeft5_load2 = pygame.image.load('Character5/C5_L2.png')
walkLeft5_load3 = pygame.image.load('Character5/C5_L3.png')
walkLeft5_load4 = pygame.image.load('Character5/C5_L4.png')
walkLeft5_load5 = pygame.image.load('Character5/C5_L5.png')
walkLeft5_load6 = pygame.image.load('Character5/C5_L6.png')
walkLeft5_load7 = pygame.image.load('Character5/C5_L7.png')
walkLeft5_load8 = pygame.image.load('Character5/C5_L8.png')
walkLeft5_load9 = pygame.image.load('Character5/C5_L9.png')
walkLeft5_size1 = pygame.transform.scale(walkLeft5_load1, (200,400))
walkLeft5_size2 = pygame.transform.scale(walkLeft5_load2, (200,400))
walkLeft5_size3 = pygame.transform.scale(walkLeft5_load3, (200,400))
walkLeft5_size4 = pygame.transform.scale(walkLeft5_load4, (200,400))
walkLeft5_size5 = pygame.transform.scale(walkLeft5_load5, (200,400))
walkLeft5_size6 = pygame.transform.scale(walkLeft5_load6, (200,400))
walkLeft5_size7 = pygame.transform.scale(walkLeft5_load7, (200,400))
walkLeft5_size8 = pygame.transform.scale(walkLeft5_load8, (200,400))
walkLeft5_size9 = pygame.transform.scale(walkLeft5_load9, (200,400))
walkLeft5 = [walkLeft5_size1,walkLeft5_size2,walkLeft5_size3,walkLeft5_size4,walkLeft5_size5,walkLeft5_size6,walkLeft5_size7,walkLeft5_size8,walkLeft5_size9]

charfive_load = pygame.image.load('Character5/standing5.png')
charfive = pygame.transform.scale(charfive_load, (200,400))

atkPunch_load5 = pygame.image.load('Character5/P5.png')
atkPunch5 = pygame.transform.scale(atkPunch_load5, (250,400))

atkKick_load5 = pygame.image.load('Character5/K5.png')
atkKick5 = pygame.transform.scale(atkKick_load5, (200,400))

crouch_load5 = pygame.image.load('Character5/C5.png')
moveCrouch5 = pygame.transform.scale(crouch_load5, (200,400))

damagetaken5_load = pygame.image.load('Character5/DT5.png')
damagetaken5 = pygame.transform.scale(damagetaken5_load, (250,500))

lose5_load = pygame.image.load('Character5/lose5.png')
lose5 = pygame.transform.scale(lose5_load, (250,500))


#Character 6
imagesix_load = pygame.image.load('Character6/image6.png')
imagesix = pygame.transform.scale(imagesix_load, (50,50))

walkRight_load6 = pygame.image.load('Character6/C6_R1.png')
walkRight6 = pygame.transform.scale(walkRight_load6, (200,375))

walkLeft_load6 = pygame.image.load('Character6/C6_L1.png')
walkLeft6 = pygame.transform.scale(walkLeft_load6, (200,375))

charsix_load = pygame.image.load('Character6/standing6.png')
charsix = pygame.transform.scale(charsix_load, (200,400))

atkPunch_load6 = pygame.image.load('Character6/P6.png')
atkPunch6 = pygame.transform.scale(atkPunch_load6, (200,400))

atkKick_load6 = pygame.image.load('Character6/K6.png')
atkKick6 = pygame.transform.scale(atkKick_load6, (250,400))

crouch_load6 = pygame.image.load('Character6/C6.png')
moveCrouch6 = pygame.transform.scale(crouch_load6, (200,400))

damagetaken6_load = pygame.image.load('Character6/DT6.png')
damagetaken6 = pygame.transform.scale(damagetaken6_load, (250,500))

lose6_load = pygame.image.load('Character6/lose6.png')
lose6 = pygame.transform.scale(lose6_load, (250,500))



#Creating Character 1
class character_one():
    
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 10, self.y + 120, 190, 360)
        self.health = 10
        self.punch = True 
        self.kick = True 
        self.crouch = True
        self.lose = False
        self.hits = False
        
    def draw(self, win):       
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft, (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight, (self.x,self.y))
            self.walkCount +=1
        elif self.punch: 
            win.blit(atkPunch, (self.x,self.y))
        elif self.kick: 
            win.blit(atkKick, (self.x,self.y))
        elif self.crouch: 
            win.blit(moveCrouch, (self.x,self.y))
        elif self.lose:
            win.blit(lose1, (self.x,self.y))
        elif self.hits:
            win.blit(damagetaken1, (self.x,self.y))
        else:
            win.blit(charone, (self.x,self.y))

        pygame.draw.rect(win, red, (40,70,500,20)) 
        pygame.draw.rect(win, green, (40,70,500 - (50 * (10 - self.health)), 20))

        self.hitbox = (self.x + 10, self.y + 120, 190, 360)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self): 
        if self.health > 0:
            self.health -= 0.1
            if char1.x > char1.vel:
                char1.x -= char1.vel 
        else:
            return game_end(char1)
            
                    

#Creating Character 2
class character_two():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 10, self.y + 20, 165, 360)
        self.health = 10 
        self.punch = True 
        self.kick = True 
        self.crouch = True
        self.lose = False
        self.hits = False

    def draw(self, win):      
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft2[self.walkCount//5], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight2[self.walkCount//5], (self.x,self.y))
            self.walkCount +=1 
        elif self.punch: 
            win.blit(atkPunch2, (self.x,self.y))
        elif self.kick: 
            win.blit(atkKick2, (self.x,self.y))
        elif self.crouch: 
            win.blit(moveCrouch2, (self.x,self.y))
        elif self.lose:
            win.blit(lose2, (self.x,self.y))
        elif self.hits:
            win.blit(damagetaken2, (self.x,self.y))
        else:
            win.blit(chartwo, (self.x,self.y))
            
        pygame.draw.rect(win, red, (725,70,500,20)) 
        pygame.draw.rect(win, green, (725,70,500 - (50 * (10 - self.health)), 20)) 

        self.hitbox = (self.x + 10, self.y + 20, 165, 360)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)            

    def hit(self): 
        if self.health > 0:
            self.health -= 0.1
            if char2.x > char2.vel:
                char2.x += char2.vel 
        else:
            return game_end(char2)


#Creating Character3
class character_three():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 10, self.y + 10, 125, 285)
        self.health = 10 
        self.punch = True 
        self.kick = True 
        self.crouch = True
        self.lose = False
        self.hits = False

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft3, (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight3, (self.x,self.y))
            self.walkCount +=1 
        elif self.punch: 
            win.blit(atkPunch3, (self.x,self.y))
        elif self.kick: 
            win.blit(atkKick3, (self.x,self.y))
        elif self.crouch: 
            win.blit(moveCrouch3, (self.x,self.y))
        elif self.lose:
            win.blit(lose3, (self.x,self.y))
        elif self.hits:
            win.blit(damagetaken3, (self.x,self.y))
        else:
            win.blit(charthree, (self.x,self.y))

        pygame.draw.rect(win, red, (40,70,500,20)) 
        pygame.draw.rect(win, green, (40,70,500 - (50 * (10 - self.health)), 20))

        self.hitbox = (self.x + 10, self.y + 10, 125, 285)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self): 
        if self.health > 0:
            self.health -= 0.1
            if char3.x > char3.vel:
                char3.x -= char3.vel 
        else:
            return game_end(char3)
            


#Creating Character4
class character_four():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 0, self.y + 45, 140, 250)
        self.health = 10 
        self.punch = True 
        self.kick = True 
        self.crouch = True
        self.lose = False
        self.hits = False

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft4, (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight4, (self.x,self.y))
            self.walkCount +=1 
        elif self.punch: 
            win.blit(atkPunch4, (self.x,self.y))
        elif self.kick: 
            win.blit(atkKick4, (self.x,self.y))
        elif self.crouch: 
            win.blit(moveCrouch4, (self.x,self.y))
        elif self.lose:
            win.blit(lose4, (self.x,self.y))
        elif self.hits:
            win.blit(damagetaken4, (self.x,self.y))
        else:
            win.blit(charfour, (self.x,self.y))
            
        pygame.draw.rect(win, red, (725,70,500,20)) 
        pygame.draw.rect(win, green, (725,70,500 - (50 * (10 - self.health)), 20)) 

        self.hitbox = (self.x + 0, self.y + 45, 140, 250)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self): 
        if self.health > 0:
            self.health -= 0.1
            if char4.x > char4.vel:
                char4.x += char4.vel 
        else:
            return game_end(char4)



#Creating Character 5
class character_five():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 10, self.y + 20, 165, 360)
        self.health = 10 
        self.punch = True 
        self.kick = True 
        self.crouch = True
        self.lose = False
        self.hits = False

    def draw(self, win):      
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft5[self.walkCount//9], (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight5[self.walkCount//9], (self.x,self.y))
            self.walkCount +=1 
        elif self.punch: 
            win.blit(atkPunch5, (self.x,self.y))
        elif self.kick: 
            win.blit(atkKick5, (self.x,self.y))
        elif self.crouch: 
            win.blit(moveCrouch5, (self.x,self.y))
        elif self.lose:
            win.blit(lose5, (self.x,self.y))
        elif self.hits:
            win.blit(damagetaken5, (self.x,self.y))
        else:
            win.blit(charfive, (self.x,self.y))
            
        pygame.draw.rect(win, red, (40,70,500,20)) 
        pygame.draw.rect(win, green, (40,70,500 - (50 * (10 - self.health)), 20)) 

        self.hitbox = (self.x + 10, self.y + 20, 165, 360)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)            

    def hit(self): 
        if self.health > 0:
            self.health -= 0.1
            if char5.x > char5.vel:
                char5.x -= char5.vel 
        else:
            return game_end(char5)
  

#Creating Character 6
class character_six():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 10, self.y + 20, 50, 325)
        self.health = 10
        self.punch = True 
        self.kick = True 
        self.crouch = True
        self.lose = False
        self.hits = False

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft6, (self.x,self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight6, (self.x,self.y))
            self.walkCount +=1 
        elif self.punch: 
            win.blit(atkPunch6, (self.x,self.y))
        elif self.kick: 
            win.blit(atkKick6, (self.x,self.y))
        elif self.crouch: 
            win.blit(moveCrouch6, (self.x,self.y))
        elif self.lose:
            win.blit(lose6, (self.x,self.y))
        elif self.hits:
            win.blit(damagetaken6, (self.x,self.y))
        else:
            win.blit(charsix, (self.x,self.y))
            
        pygame.draw.rect(win, red, (725,70,500,20)) 
        pygame.draw.rect(win, green, (725,70,500 - (50 * (10 - self.health)), 20)) 

        self.hitbox = (self.x + 10, self.y + 20, 140, 325)
        #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self): 
        if self.health > 0:
            self.health -= 0.1
            if char6.x > char6.vel:
                char6.x += char6.vel 
        else:
            return game_end(char6)


#Function for displaying characters
def show_character1():
    char1.draw(win)
    win.blit(imageone, (80,15))
    char1_name()
    
def show_character2():
    char2.draw(win)
    win.blit(imagetwo, (800,15))
    char2_name()

def show_character3():
    char3.draw(win)
    win.blit(imagethree, (80,15))
    char3_name()

def show_character4():
    char4.draw(win)
    win.blit(imagefour, (800,15))
    char4_name()

def show_character5():
    char5.draw(win)
    win.blit(imagefive, (80,15))
    char5_name()

def show_character6():
    char6.draw(win)
    win.blit(imagesix, (800,15))
    char6_name()


#Drawing characters
char1 = character_one(200,200,64,64)
char2 = character_two(1000,300,64,64)
char3 = character_three(200,290,64,64)
char4 = character_four(1000,275,64,64)
char5 = character_five(200,300,64,64)
char6 = character_six(1000,300,64,64)

#Colisions
def collisions(damage_dealer, victim):

    char_atk = damage_dealer
    char_dam = victim
    if char_atk.hitbox[1] < char_dam.hitbox[1] + char_dam.hitbox[3] and char_atk.hitbox[1] + char_atk.hitbox[3] > char_dam.hitbox[1]:
        if char_atk.hitbox[0] > char_dam.hitbox[0] and char_atk.hitbox[0] < char_dam.hitbox[0] + char_dam.hitbox[2]:
            char_dam.hit()

def game_end(loser):
    for fighter in fighters:
        if fighter != loser:
            winner = fighter

    if winner == char1:
        c1_win()
    if winner == char2:
        c2_win()
    if winner == char3:
        c3_win()
    if winner == char4:
        c4_win()
    if winner == char5:
        c5_win()
    if winner == char6:
        c6_win()
    
#Movement of character 1
def character1():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and char1.x > char1.vel:
        char1.x -= char1.vel
        char1.left = True
        char1.right = False
        char1.punch = False
        char1.kick = False
        char1.crouch = False
        
    elif keys[pygame.K_d] and char1.x < 1200 - char1.width - char1.vel:
        char1.x += char1.vel
        char1.right = True
        char1.left = False
        char1.punch = False
        char1.kick = False
        char1.crouch = False
        
    elif keys[pygame.K_v]:
        char1.punch = True
        char1.right = False
        char1.left = False
        char1.kick = False
        char1.crouch = False
        for fighter in fighters:
            if fighter != char1:
                victim = fighter
            
        collisions(char1, victim)
        punch_SE.play() 
        
    elif keys[pygame.K_s]:
        char1.crouch = True
        char1.kick = False
        char1.punch = False
        char1.right = False
        char1.left = False
        
    elif keys[pygame.K_b]:
        char1.kick = True
        char1.crouch = False
        char1.punch = False
        char1.right = False
        char1.left = False
        for fighter in fighters:
            if fighter != char1:
                victim = fighter
            
        collisions(char1, victim)
        kick_SE.play() 
        
    else:
        char1.right = False
        char1.left = False
        char1.punch = False
        char1.kick = False
        char1.crouch = False
        char1.walkCount = 0

    
    if not(char1.isJump):
        if keys[pygame.K_w]:
            char1.isJump = True
            char1.right = False
            char1.left = False
            char1.punch = False
            char1.kick = False
            char1.crouch = False
            char1.walkCount = 0
    else:
        if char1.jumpCount >= -10:
            neg = 1
            if char1.jumpCount < 0:
                neg = -1
            char1.y -= (char1.jumpCount ** 2) * 0.5 * neg
            char1.jumpCount -= 1
        else:
            char1.isJump = False
            char1.jumpCount = 10

            

#Movement of character 2
def character2():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and char2.x > char2.vel:
        char2.x -= char2.vel
        char2.left = True
        char2.right = False
        char2.punch = False
        char2.kick = False
        char2.crouch = False
        
    elif keys[pygame.K_RIGHT] and char2.x < 1200 - char2.width - char2.vel:
        char2.x += char2.vel
        char2.right = True
        char2.left = False
        char2.punch = False
        char2.kick = False
        char2.crouch = False
        
    elif keys[pygame.K_COMMA]:
        char2.punch = True
        char2.right = False
        char2.left = False
        char2.kick = False
        char2.crouch = False
        
        for fighter in fighters:
            if fighter != char2:
                victim = fighter
            
        collisions(char2, victim)
        punch_SE.play() 
        
    elif keys[pygame.K_DOWN]:
        char2.crouch = True
        char2.kick = False
        char2.punch = False
        char2.right = False
        char2.left = False
        
    elif keys[pygame.K_PERIOD]:
        char2.kick = True
        char2.crouch = False
        char2.punch = False
        char2.right = False
        char2.left = False
        
        for fighter in fighters:
            if fighter != char2:
                victim = fighter
            
        collisions(char2, victim)
        kick_SE.play() 
        
    else:
        char2.right = False
        char2.left = False
        char2.punch = False
        char2.kick = False
        char2.crouch = False
        char2.walkCount = 0
        
    if not(char2.isJump):
        if keys[pygame.K_UP]:
            char2.isJump = True
            char2.right = False
            char2.left = False
            char2.punch = False
            char2.kick = False
            char2.crouch = False
            char2.walkCount = 0
    else:
        if char2.jumpCount >= -10:
            neg = 1
            if char2.jumpCount < 0:
                neg = -1
            char2.y -= (char2.jumpCount ** 2) * 0.5 * neg
            char2.jumpCount -= 1
        else:
            char2.isJump = False
            char2.jumpCount = 10


#Movement of character 3
def character3():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and char3.x > char3.vel:
        char3.x -= char1.vel
        char3.left = True
        char3.right = False
        char3.punch = False
        char3.kick = False
        char3.crouch = False
        
    elif keys[pygame.K_d] and char3.x < 1200 - char3.width - char3.vel:
        char3.x += char3.vel
        char3.right = True
        char3.left = False
        char3.punch = False
        char3.kick = False
        char3.crouch = False
        
    elif keys[pygame.K_v]:
        char3.punch = True
        char3.right = False
        char3.left = False
        char3.kick = False
        char3.crouch = False
        for fighter in fighters:
            if fighter != char3:
                victim = fighter
        collisions(char3, victim)
        punch_SE.play() 
        
    elif keys[pygame.K_s]:
        char3.crouch = True
        char3.kick = False
        char3.punch = False
        char3.right = False
        char3.left = False
        
    elif keys[pygame.K_b]:
        char3.kick = True
        char3.crouch = False
        char3.punch = False
        char3.right = False
        char3.left = False
        for fighter in fighters:
            if fighter != char3:
                victim = fighter
            
        collisions(char3, victim)
        kick_SE.play() 
        
    else:
        char3.right = False
        char3.left = False
        char3.punch = False
        char3.kick = False
        char3.crouch = False
        char3.walkCount = 0

    
    if not(char3.isJump):
        if keys[pygame.K_w]:
            char3.isJump = True
            char3.right = False
            char3.left = False
            char3.punch = False
            char3.kick = False
            char3.crouch = False
            char3.walkCount = 0
    else:
        if char3.jumpCount >= -10:
            neg = 1
            if char3.jumpCount < 0:
                neg = -1
            char3.y -= (char3.jumpCount ** 2) * 0.5 * neg
            char3.jumpCount -= 1
        else:
            char3.isJump = False
            char3.jumpCount = 10


#Movement of character 4
def character4():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and char4.x > char4.vel:
        char4.x -= char4.vel
        char4.left = True
        char4.right = False
        char4.punch = False
        char4.kick = False
        char4.crouch = False
        
    elif keys[pygame.K_RIGHT] and char4.x < 1200 - char4.width - char4.vel:
        char4.x += char4.vel
        char4.right = True
        char4.left = False
        char4.punch = False
        char4.kick = False
        char4.crouch = False
        
    elif keys[pygame.K_COMMA]:
        char4.punch = True
        char4.right = False
        char4.left = False
        char4.kick = False
        char4.crouch = False
        for fighter in fighters:
            if fighter != char4:
                victim = fighter
            
        collisions(char4, victim)
        punch_SE.play() 
        
    elif keys[pygame.K_DOWN]:
        char4.crouch = True
        char4.kick = False
        char4.punch = False
        char4.right = False
        char4.left = False
        
    elif keys[pygame.K_PERIOD]:
        char4.kick = True
        char4.crouch = False
        char4.punch = False
        char4.right = False
        char4.left = False
        for fighter in fighters:
            if fighter != char4:
                victim = fighter
            
        collisions(char4, victim)
        kick_SE.play() 
        
    else:
        char4.right = False
        char4.left = False
        char4.punch = False
        char4.kick = False
        char4.crouch = False
        char4.walkCount = 0
        
    if not(char4.isJump):
        if keys[pygame.K_UP]:
            char4.isJump = True
            char4.right = False
            char4.left = False
            char4.punch = False
            char4.kick = False
            char4.crouch = False
            char4.walkCount = 0
    else:
        if char4.jumpCount >= -10:
            neg = 1
            if char4.jumpCount < 0:
                neg = -1
            char4.y -= (char4.jumpCount ** 2) * 0.5 * neg
            char4.jumpCount -= 1
        else:
            char4.isJump = False
            char4.jumpCount = 10


#Movement of character 5
def character5():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and char5.x > char5.vel:
        char5.x -= char5.vel
        char5.left = True
        char5.right = False
        char5.punch = False
        char5.kick = False
        char5.crouch = False
        
    elif keys[pygame.K_d] and char5.x < 1200 - char5.width - char5.vel:
        char5.x += char5.vel
        char5.right = True
        char5.left = False
        char5.punch = False
        char5.kick = False
        char5.crouch = False
        
    elif keys[pygame.K_v]:
        char5.punch = True
        char5.right = False
        char5.left = False
        char5.kick = False
        char5.crouch = False
        for fighter in fighters:
            if fighter != char5:
                victim = fighter
            
        collisions(char5, victim)
        punch_SE.play() 
        
    elif keys[pygame.K_s]:
        char5.crouch = True
        char5.kick = False
        char5.punch = False
        char5.right = False
        char5.left = False
        
    elif keys[pygame.K_b]:
        char5.kick = True
        char5.crouch = False
        char5.punch = False
        char5.right = False
        char5.left = False
        for fighter in fighters:
            if fighter != char5:
                victim = fighter
            
        collisions(char5, victim)
        kick_SE.play() 
        
    else:
        char5.right = False
        char5.left = False
        char5.punch = False
        char5.kick = False
        char5.crouch = False
        char5.walkCount = 0

    
    if not(char5.isJump):
        if keys[pygame.K_w]:
            char5.isJump = True
            char5.right = False
            char5.left = False
            char5.punch = False
            char5.kick = False
            char5.crouch = False
            char5.walkCount = 0
    else:
        if char5.jumpCount >= -10:
            neg = 1
            if char5.jumpCount < 0:
                neg = -1
            char5.y -= (char5.jumpCount ** 2) * 0.5 * neg
            char5.jumpCount -= 1
        else:
            char5.isJump = False
            char5.jumpCount = 10


#Movement of character 6
def character6():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and char6.x > char6.vel:
        char6.x -= char6.vel
        char6.left = True
        char6.right = False
        char6.punch = False
        char6.kick = False
        char6.crouch = False
        
    elif keys[pygame.K_RIGHT] and char6.x < 1200 - char6.width - char6.vel:
        char6.x += char4.vel
        char6.right = True
        char6.left = False
        char6.punch = False
        char6.kick = False
        char6.crouch = False
        
    elif keys[pygame.K_COMMA]:
        char6.punch = True
        char6.right = False
        char6.left = False
        char6.kick = False
        char6.crouch = False
        for fighter in fighters:
            if fighter != char6:
                victim = fighter
            
        collisions(char6, victim)
        punch_SE.play() 
        
    elif keys[pygame.K_DOWN]:
        char6.crouch = True
        char6.kick = False
        char6.punch = False
        char6.right = False
        char6.left = False
        
    elif keys[pygame.K_PERIOD]:
        char6.kick = True
        char6.crouch = False
        char6.punch = False
        char6.right = False
        char6.left = False
        for fighter in fighters:
            if fighter != char6:
                victim = fighter
            
        collisions(char6, victim)
        kick_SE.play() 
        
    else:
        char6.right = False
        char6.left = False
        char6.punch = False
        char6.kick = False
        char6.crouch = False
        char6.walkCount = 0
        
    if not(char6.isJump):
        if keys[pygame.K_UP]:
            char6.isJump = True
            char6.right = False
            char6.left = False
            char6.punch = False
            char6.kick = False
            char6.crouch = False
            char6.walkCount = 0
    else: 
       if char6.jumpCount >= -10:
            neg = 1
            if char6.jumpCount < 0:
                neg = -1
            char6.y -= (char6.jumpCount ** 2) * 0.5 * neg
            char6.jumpCount -= 1
       else:
            char6.isJump = False
            char6.jumpCount = 10


#-------------Interface--------------------------------#

#Check For Click
click = False


#Function for main menu
def main_menu():
    
    pygame.mixer.music.stop()  
    music = pygame.mixer.music.load("music.mp3") 
    pygame.mixer.music.play(-1)
    
    while True:

        win.blit(mainbg, (0,0))

        mx, my = pygame.mouse.get_pos()

        arcadebutton = pygame.Rect(45,245,260,50)
        char_descriptionbutton = pygame.Rect(45,320,230,50)
        settingsbutton = pygame.Rect(45,390,175,50)
        controlsbutton = pygame.Rect(45,460,175,50)
        exitbutton = pygame.Rect(45,530,100,50)

        pygame.draw.rect(win, (whitesmoke), arcadebutton)
        draw_text('Arcade Mode', font, black, win, 70, 250)
        pygame.draw.rect(win, black, (45, 245, 260, 50), 3)
        
        pygame.draw.rect(win, (whitesmoke), char_descriptionbutton)
        draw_text('Characters', font, black, win, 70, 325)
        pygame.draw.rect(win, black, (45, 320, 230, 50), 3)
        
        pygame.draw.rect(win, (whitesmoke), settingsbutton)
        draw_text('Settings', font, black, win, 70, 395)
        pygame.draw.rect(win, black, (45, 390, 175, 50), 3)
        
        pygame.draw.rect(win, (whitesmoke), controlsbutton)
        draw_text('Controls', font, black, win, 70, 465)
        pygame.draw.rect(win, black, (45, 460, 175, 50), 3)
        
        pygame.draw.rect(win, (whitesmoke), exitbutton)
        draw_text('Exit', font, black, win, 90, 535)
        pygame.draw.rect(win, black, (45, 530, 175, 50), 3)
        
        if arcadebutton.collidepoint((mx, my)):
            if click:
                arcade()
                
        if char_descriptionbutton.collidepoint((mx, my)):
            if click:
                char_description()
                
        if settingsbutton.collidepoint((mx, my)):
            if click:
                settings()

        if controlsbutton.collidepoint((mx, my)):
            if click:
                controls()

        if exitbutton.collidepoint((mx, my)):
            if click:
                pygame.quit()
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)

def arcade():
    running = True
    while running:
        win.blit(arcadebg, (0,0))

        mx, my = pygame.mouse.get_pos()

        onevsonebutton = pygame.Rect(45,310,230,40)
        endlessbutton = pygame.Rect(45,370,230,40)
        tutorialbutton = pygame.Rect(45,430,230,40)
        mainmenubutton = pygame.Rect(150,560,200,50)
        
        pygame.draw.rect(win, (whitesmoke), onevsonebutton)
        draw_text('1vs1', font, black, win, 70, 310)
        pygame.draw.rect(win, black, (45,310,230,40), 3)
        
        pygame.draw.rect(win, (whitesmoke), endlessbutton)
        draw_text('Endless', font, black, win, 70, 370)
        pygame.draw.rect(win, black, (45,370,230,40), 3)
        
        pygame.draw.rect(win, (whitesmoke), tutorialbutton)
        draw_text('Tutorial', font, black, win, 70, 430)
        pygame.draw.rect(win, black, (45,430,230,40), 3)

        pygame.draw.rect(win, (whitesmoke), mainmenubutton)
        draw_text('Main Menu', font, black, win, 160, 565)
        pygame.draw.rect(win, black, (150,560,200,50), 3)

        if mainmenubutton.collidepoint((mx, my)):
            if click:
                main_menu()

        if onevsonebutton.collidepoint((mx, my)):
            if click:
                character_Select_P1()
        if endlessbutton.collidepoint((mx, my)):
            if click:
                endless()
        if tutorialbutton.collidepoint((mx, my)):
            if click:
                tutorial()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        
        pygame.display.update()
        clock.tick(60)


def character_Select_P1():
    running = True
    while running:
        win.blit(charselectbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        c1_button = pygame.Rect(595,240,70,80)
        c3_button = pygame.Rect(560,340,70,80)
        c5_button = pygame.Rect(640,340,70,80)
        
        icon1 = pygame.transform.scale(imageone_load, (120,120))
        icon2 = pygame.transform.scale(imagetwo_load, (80,75))
        icon3 = pygame.transform.scale(imagethree_load, (110,120))
        icon4 = pygame.transform.scale(imagefour_load, (90,90))
        icon5 = pygame.transform.scale(imagefive_load, (80,75))
        icon6 = pygame.transform.scale(imagesix_load, (110,100))
        win.blit(icon1, (570,240))
        win.blit(icon2, (590,440))
        win.blit(icon3, (540,330))
        win.blit(icon4, (485,435))
        win.blit(icon5, (640,350))
        win.blit(icon6, (680,430))

        c1_large_icon = pygame.transform.scale(c1_large_icon_load, (400,400))
        c3_large_icon = pygame.transform.scale(c3_large_icon_load, (370,450))
        c5_large_icon = pygame.transform.scale(c5_large_icon_load, (350,400))

        nameboxP1 = pygame.Rect(50,600,400,40)
        nameboxP2 = pygame.Rect(800,600,400,40)

        pygame.draw.rect(win, (whitesmoke), nameboxP1)
        pygame.draw.rect(win, red, (50,600,400,40), 3)
        pygame.draw.rect(win, (whitesmoke), nameboxP2)
        pygame.draw.rect(win, blue, (800,600,400,40), 3)

        if 595+70 > mx > 595 and 240+80 > my > 240:
            win.blit(c1_large_icon, (50, 200))
            draw_text('Kazuo Ishigami', font, black, win, 125, 600)
            
        if 560+70 > mx > 560 and 340+80 > my > 340:
            win.blit(c3_large_icon, (50, 150))
            draw_text('Atlas Chrollo', font, black, win, 125, 600)
            
        if 640+70 > mx > 640 and 340+80 > my > 340:
            win.blit(c5_large_icon, (50, 200))
            draw_text('Hisoka Yasumoto', font, black, win, 110, 600)

        if c1_button.collidepoint((mx, my)):
            if click:
                character_Select_P2_vs_C1()
        if c3_button.collidepoint((mx, my)):
            if click:
                character_Select_P2_vs_C3()
        if c5_button.collidepoint((mx, my)):
            if click:
                character_Select_P2_vs_C5()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        pygame.display.update()
        clock.tick(60)
    

def character_Select_P2_vs_C1():
    running = True
    while running:
        win.blit(charselectbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        c2_button = pygame.Rect(595,440,70,80)
        c4_button = pygame.Rect(485,435,70,80)
        c6_button = pygame.Rect(680,430,70,80)
        
        icon1 = pygame.transform.scale(imageone_load, (120,120))
        icon2 = pygame.transform.scale(imagetwo_load, (80,75))
        icon3 = pygame.transform.scale(imagethree_load, (110,120))
        icon4 = pygame.transform.scale(imagefour_load, (90,90))
        icon5 = pygame.transform.scale(imagefive_load, (80,75))
        icon6 = pygame.transform.scale(imagesix_load, (110,100))
        win.blit(icon1, (570,240))
        win.blit(icon2, (590,440))
        win.blit(icon3, (540,330))
        win.blit(icon4, (485,435))
        win.blit(icon5, (640,350))
        win.blit(icon6, (680,430))

        c1_large_icon = pygame.transform.scale(c1_large_icon_load, (400,400))
        c2_large_icon = pygame.transform.scale(c2_large_icon_load, (400,400))
        c4_large_icon = pygame.transform.scale(c4_large_icon_load, (400,400))
        c6_large_icon = pygame.transform.scale(c6_large_icon_load, (400,400))
        
        nameboxP1 = pygame.Rect(50,600,400,40)
        nameboxP2 = pygame.Rect(800,600,400,40)

        pygame.draw.rect(win, (whitesmoke), nameboxP1)
        pygame.draw.rect(win, red, (50,600,400,40), 3)
        pygame.draw.rect(win, (whitesmoke), nameboxP2)
        pygame.draw.rect(win, blue, (800,600,400,40), 3)

        win.blit(c1_large_icon, (50, 200))
        draw_text('Kazuo Ishigami', font, black, win, 125, 600)

        if 595+70 > mx > 595 and 440+80 > my > 440:
            win.blit(c2_large_icon, (800, 200))
            draw_text('Kira Okita ', font, black, win, 880, 600)
        if 485+70 > mx > 485 and 435+80 > my > 435:
            win.blit(c4_large_icon, (800, 200))
            draw_text('Amani Miyamisui', font, black, win, 860, 600)
        if 680+70 > mx > 680 and 430+80 > my > 430:
            win.blit(c6_large_icon, (800, 200))
            draw_text('Ajin Nakamura', font, black, win, 880, 600)


        if c2_button.collidepoint((mx, my)):
            if click:
                c1_vs_c2()
        if c4_button.collidepoint((mx, my)):
            if click:
                c1_vs_c4()
        if c6_button.collidepoint((mx, my)):
            if click:
                c1_vs_c6()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        pygame.display.update()
        clock.tick(60)


def character_Select_P2_vs_C3():
    running = True
    while running:
        win.blit(charselectbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        c2_button = pygame.Rect(595,440,70,80)
        c4_button = pygame.Rect(485,435,70,80)
        c6_button = pygame.Rect(680,430,70,80)
        
        icon1 = pygame.transform.scale(imageone_load, (120,120))
        icon2 = pygame.transform.scale(imagetwo_load, (80,75))
        icon3 = pygame.transform.scale(imagethree_load, (110,120))
        icon4 = pygame.transform.scale(imagefour_load, (90,90))
        icon5 = pygame.transform.scale(imagefive_load, (80,75))
        icon6 = pygame.transform.scale(imagesix_load, (110,100))
        win.blit(icon1, (570,240))
        win.blit(icon2, (590,440))
        win.blit(icon3, (540,330))
        win.blit(icon4, (485,435))
        win.blit(icon5, (640,350))
        win.blit(icon6, (680,430))

        c3_large_icon = pygame.transform.scale(c3_large_icon_load, (370,450))
        c2_large_icon = pygame.transform.scale(c2_large_icon_load, (400,400))
        c4_large_icon = pygame.transform.scale(c4_large_icon_load, (400,400))
        c6_large_icon = pygame.transform.scale(c6_large_icon_load, (400,400))
        
        nameboxP1 = pygame.Rect(50,600,400,40)
        nameboxP2 = pygame.Rect(800,600,400,40)

        pygame.draw.rect(win, (whitesmoke), nameboxP1)
        pygame.draw.rect(win, red, (50,600,400,40), 3)
        pygame.draw.rect(win, (whitesmoke), nameboxP2)
        pygame.draw.rect(win, blue, (800,600,400,40), 3)

        win.blit(c3_large_icon, (50, 150))
        draw_text('Atlas Chrollo', font, black, win, 125, 600)

        if 595+70 > mx > 595 and 440+80 > my > 440:
            win.blit(c2_large_icon, (800, 200))
            draw_text('Kira Okita ', font, black, win, 880, 600)
        if 485+70 > mx > 485 and 435+80 > my > 435:
            win.blit(c4_large_icon, (800, 200))
            draw_text('Amani Miyamisui', font, black, win, 860, 600)
        if 680+70 > mx > 680 and 430+80 > my > 430:
            win.blit(c6_large_icon, (800, 200))
            draw_text('Ajin Nakamura', font, black, win, 880, 600)


        if c2_button.collidepoint((mx, my)):
            if click:
                c3_vs_c2()
        if c4_button.collidepoint((mx, my)):
            if click:
                c3_vs_c4()
        if c6_button.collidepoint((mx, my)):
            if click:
                c3_vs_c6()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        pygame.display.update()
        clock.tick(60)



def character_Select_P2_vs_C5():
    running = True
    while running:
        win.blit(charselectbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        c2_button = pygame.Rect(595,440,70,80)
        c4_button = pygame.Rect(485,435,70,80)
        c6_button = pygame.Rect(680,430,70,80)
        
        icon1 = pygame.transform.scale(imageone_load, (120,120))
        icon2 = pygame.transform.scale(imagetwo_load, (80,75))
        icon3 = pygame.transform.scale(imagethree_load, (110,120))
        icon4 = pygame.transform.scale(imagefour_load, (90,90))
        icon5 = pygame.transform.scale(imagefive_load, (80,75))
        icon6 = pygame.transform.scale(imagesix_load, (110,100))
        win.blit(icon1, (570,240))
        win.blit(icon2, (590,440))
        win.blit(icon3, (540,330))
        win.blit(icon4, (485,435))
        win.blit(icon5, (640,350))
        win.blit(icon6, (680,430))

        c5_large_icon = pygame.transform.scale(c5_large_icon_load, (350,400))
        c2_large_icon = pygame.transform.scale(c2_large_icon_load, (400,400))
        c4_large_icon = pygame.transform.scale(c4_large_icon_load, (400,400))
        c6_large_icon = pygame.transform.scale(c6_large_icon_load, (400,400))
        
        nameboxP1 = pygame.Rect(50,600,400,40)
        nameboxP2 = pygame.Rect(800,600,400,40)

        pygame.draw.rect(win, (whitesmoke), nameboxP1)
        pygame.draw.rect(win, red, (50,600,400,40), 3)
        pygame.draw.rect(win, (whitesmoke), nameboxP2)
        pygame.draw.rect(win, blue, (800,600,400,40), 3)

        win.blit(c5_large_icon, (50, 200))
        draw_text('Hisoka Yasumoto', font, black, win, 110, 600)

        if 595+70 > mx > 595 and 440+80 > my > 440:
            win.blit(c2_large_icon, (800, 200))
            draw_text('Kira Okita ', font, black, win, 880, 600)
        if 485+70 > mx > 485 and 435+80 > my > 435:
            win.blit(c4_large_icon, (800, 200))
            draw_text('Amani Miyamisui', font, black, win, 860, 600)
        if 680+70 > mx > 680 and 430+80 > my > 430:
            win.blit(c6_large_icon, (800, 200))
            draw_text('Ajin Nakamura', font, black, win, 880, 600)


        if c2_button.collidepoint((mx, my)):
            if click:
                c5_vs_c2()
        if c4_button.collidepoint((mx, my)):
            if click:
                c5_vs_c4()
        if c6_button.collidepoint((mx, my)):
            if click:
                c5_vs_c6()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        pygame.display.update()
        clock.tick(60)



def c1_vs_c2():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Evil Empire', 80)
    
    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else draw()
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (595, 40))
            pygame.display.flip()
            

        keys = pygame.key.get_pressed()
    
        character1()
        character2()

        map_2()

        show_character1()
        show_character2()
                    
        pygame.display.update()
        clock.tick(60)


def c1_vs_c4():
    pygame.mixer.music.stop()    
    music8 = pygame.mixer.music.load("Sound/soundtrack8.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Evil Empire', 80)
    
    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else draw()
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (595, 40))
            pygame.display.flip()

        keys = pygame.key.get_pressed()
    
        character1()
        character4()

        map_4()
        show_character1()
        show_character4()
            
        pygame.display.update()
        clock.tick(60)



    
def c1_vs_c6():
    pygame.mixer.music.stop()    
    music4 = pygame.mixer.music.load("Sound/soundtrack4.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Evil Empire', 80)
    
    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else draw()
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (595, 40))
            pygame.display.flip()

        keys = pygame.key.get_pressed()
    
        character1()
        character6()

        map_3()
        show_character1()
        show_character6()
            
        pygame.display.update()
        clock.tick(60)


def c3_vs_c2():
    pygame.mixer.music.stop()    
    music9 = pygame.mixer.music.load("Sound/soundtrack9.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Evil Empire', 80)
    
    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else draw()
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (595, 40))
            pygame.display.flip()

        keys = pygame.key.get_pressed()
    
        character2()
        character3()

        map_7()
        show_character2()
        show_character3()
            
        pygame.display.update()
        clock.tick(60)
    



def c3_vs_c4():
    pygame.mixer.music.stop()    
    music1 = pygame.mixer.music.load("Sound/soundtrack1.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Evil Empire', 80)
    
    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else draw()
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (595, 40))
            pygame.display.flip()

        keys = pygame.key.get_pressed()
    
        character4()
        character3()

        map_8()
        show_character4()
        show_character3()
            
        pygame.display.update()
        clock.tick(60)


def c3_vs_c6():
    pygame.mixer.music.stop()    
    music7 = pygame.mixer.music.load("Sound/soundtrack7.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Evil Empire', 80)
    
    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else draw()
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (595, 40))
            pygame.display.flip()

        keys = pygame.key.get_pressed()
    
        character6()
        character3()

        map_1()
        show_character6()
        show_character3()
            
        pygame.display.update()
        clock.tick(60)



def c5_vs_c2():
    pygame.mixer.music.stop()    
    music3 = pygame.mixer.music.load("Sound/soundtrack3.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Evil Empire', 80)
    
    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else draw()
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (595, 40))
            pygame.display.flip()

        keys = pygame.key.get_pressed()
    
        character2()
        character5()

        map_6()
        show_character2()
        show_character5()
            
        pygame.display.update()
        clock.tick(60)


def c5_vs_c4():
    pygame.mixer.music.stop()    
    music5 = pygame.mixer.music.load("Sound/soundtrack5.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Evil Empire', 80)    
    
    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else draw()
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (595, 40))
            pygame.display.flip()
                    

        keys = pygame.key.get_pressed()
    
        character4()
        character5()

        map_9()
        show_character4()
        show_character5()
            
        pygame.display.update()
        clock.tick(60)

    
def c5_vs_c6():
    pygame.mixer.music.stop()    
    music6 = pygame.mixer.music.load("Sound/soundtrack6.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    counter, text = 120, '120'.rjust(3)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Evil Empire', 80)
    
    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == pygame.USEREVENT: 
                counter -= 1
                text = str(counter).rjust(3) if counter > 0 else draw()
        else:
            win.blit(font.render(text, True, (0, 0, 0)), (595, 40))
            pygame.display.flip()

        keys = pygame.key.get_pressed()
    
        character6()
        character5()

        map_5()
        show_character6()
        show_character5()
            
        pygame.display.update()
        clock.tick(60)


def tutorial():
    pygame.mixer.music.stop()    
    music10 = pygame.mixer.music.load("Sound/soundtrack10.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
        rectangle1 = pygame.Rect(150,100,310,140)
        rectangle2 = pygame.Rect(770,100,410,140)
        
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        keys = pygame.key.get_pressed()

        character1()
        character2()

        map_10()

        pygame.draw.rect(win, (whitesmoke), rectangle1)
        draw_text('Use WASD to move', font, black, win, 160, 100)
        draw_text('Use V to punch', font, black, win, 160, 140)
        draw_text('Use B to kick', font, black, win, 160, 180)
        pygame.draw.rect(win, black, (150,100,310,140), 3)

        pygame.draw.rect(win, (whitesmoke), rectangle2)
        draw_text('Use Arrow Keys to move', font, black, win, 780, 100)
        draw_text('Use Comma to punch', font, black, win, 780, 140)
        draw_text('Use Point to kick', font, black, win, 780, 180)
        pygame.draw.rect(win, black, (770,100,410,140), 3)

        show_character1()
        show_character2()
            
        pygame.display.update()
        clock.tick(60)
            

def char_description():
    running = True
    while running:
        win.blit(storybg, (0,0))

        mx, my = pygame.mouse.get_pos()

        backbutton = pygame.Rect(540,10,200,50)

        c1_summary = pygame.Rect(150,10,310,340)
        c6_summary = pygame.Rect(830,10,310,340)
        c4_summary = pygame.Rect(1000,370,263,310)
        c2_summary = pygame.Rect(700,370,263,310)
        c5_summary = pygame.Rect(350,370,290,310)
        c3_summary = pygame.Rect(25,370,295,310)

        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Main Menu', font, black, win, 550, 10)
        pygame.draw.rect(win, black, (540,10,200,50), 3)

        if backbutton.collidepoint((mx, my)):
            if click:
                running = False
        if c1_summary.collidepoint((mx, my)):
            if click:
                char1_summary_page()

        if c2_summary.collidepoint((mx, my)):
            if click:
                char2_summary_page()

        if c3_summary.collidepoint((mx, my)):
            if click:
                char3_summary_page()

        if c4_summary.collidepoint((mx, my)):
            if click:
                char4_summary_page()

        if c5_summary.collidepoint((mx, my)):
            if click:
                char5_summary_page()

        if c6_summary.collidepoint((mx, my)):
            if click:
                char6_summary_page()
                

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True        
        
        pygame.display.update()
        clock.tick(60)

        

def char1_summary_page():
    running = True
    while running:
        win.blit(c1Summarybg, (0,0))

        mx, my = pygame.mouse.get_pos()

        backbutton = pygame.Rect(540,630,200,40)

        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Back', font, black, win, 600, 630)
        pygame.draw.rect(win, black, (540,630,200,40), 3)

        if backbutton.collidepoint((mx, my)):
            if click:
                running = False
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True        
        
        pygame.display.update()
        clock.tick(60)


def char2_summary_page():
    running = True
    while running:
        win.blit(c2Summarybg, (0,0))

        mx, my = pygame.mouse.get_pos()

        backbutton = pygame.Rect(540,630,200,40)

        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Back', font, black, win, 600, 630)
        pygame.draw.rect(win, black, (540,630,200,40), 3)

        if backbutton.collidepoint((mx, my)):
            if click:
                running = False
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True        
        
        pygame.display.update()
        clock.tick(60)


def char3_summary_page():
    running = True
    while running:
        win.blit(c3Summarybg, (0,0))

        mx, my = pygame.mouse.get_pos()

        backbutton = pygame.Rect(540,630,200,40)

        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Back', font, black, win, 600, 630)
        pygame.draw.rect(win, black, (540,630,200,40), 3)

        if backbutton.collidepoint((mx, my)):
            if click:
                running = False
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True        
        
        pygame.display.update()
        clock.tick(60)

def char4_summary_page():
    running = True
    while running:
        win.blit(c4Summarybg, (0,0))

        mx, my = pygame.mouse.get_pos()

        backbutton = pygame.Rect(540,630,200,40)

        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Back', font, black, win, 600, 630)
        pygame.draw.rect(win, black, (540,630,200,40), 3)

        if backbutton.collidepoint((mx, my)):
            if click:
                running = False
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True        
        
        pygame.display.update()
        clock.tick(60)

def char5_summary_page():
    running = True
    while running:
        win.blit(c5Summarybg, (0,0))

        mx, my = pygame.mouse.get_pos()

        backbutton = pygame.Rect(540,630,200,40)

        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Back', font, black, win, 600, 630)
        pygame.draw.rect(win, black, (540,630,200,40), 3)

        if backbutton.collidepoint((mx, my)):
            if click:
                running = False
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True        
        
        pygame.display.update()
        clock.tick(60)


def char6_summary_page():
    running = True
    while running:
        win.blit(c6Summarybg, (0,0))

        mx, my = pygame.mouse.get_pos()

        backbutton = pygame.Rect(540,630,200,40)

        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Back', font, black, win, 600, 630)
        pygame.draw.rect(win, black, (540,630,200,40), 3)

        if backbutton.collidepoint((mx, my)):
            if click:
                running = False
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True        
        
        pygame.display.update()
        clock.tick(60)

    


def settings():
    running = True
    while running:
        win.blit(settingsbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        music_vol1 = pygame.Rect(150,340,50,40)
        music_vol2 = pygame.Rect(200,340,50,40)
        music_vol3 = pygame.Rect(245,340,50,40)
        music_vol4 = pygame.Rect(290,340,50,40)
        music_vol5 = pygame.Rect(335,340,50,40)
        soundeffects_vol1 = pygame.Rect(150,440,50,40)
        soundeffects_vol2 = pygame.Rect(200,440,50,40)
        soundeffects_vol3 = pygame.Rect(245,440,50,40)
        soundeffects_vol4 = pygame.Rect(290,440,50,40)
        soundeffects_vol5 = pygame.Rect(335,440,50,40)
        backbutton = pygame.Rect(150,560,200,50)

        pygame.draw.rect(win, white, music_vol1)
        draw_text('0%', font2, black, win, 155, 340)
        pygame.draw.rect(win, black, (150,340,50,40), 3)

        pygame.draw.rect(win, white, music_vol2)
        draw_text('25%', font2, black, win, 202, 340)
        pygame.draw.rect(win, black, (200,340,50,40), 3)

        pygame.draw.rect(win, white, music_vol3)
        draw_text('50%', font2, black, win, 247, 340)
        pygame.draw.rect(win, black, (245,340,50,40), 3)
        
        pygame.draw.rect(win, white, music_vol4)
        draw_text('75%', font2, black, win, 292, 340)
        pygame.draw.rect(win, black, (290,340,50,40), 3)

        pygame.draw.rect(win, white, music_vol5)
        draw_text('100%', font2, black, win, 335, 340)
        pygame.draw.rect(win, black, (335,340,50,40), 3)

        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Back', font, black, win, 160, 565)
        pygame.draw.rect(win, black, (150,560,200,50), 3)
        
        pygame.draw.rect(win, white, soundeffects_vol1)
        draw_text('0%', font2, black, win, 155, 440)
        pygame.draw.rect(win, black, (150,440,50,40), 3)

        pygame.draw.rect(win, white, soundeffects_vol2)
        draw_text('25%', font2, black, win, 202, 440)
        pygame.draw.rect(win, black, (200,440,50,40), 3)

        pygame.draw.rect(win, white, soundeffects_vol3)
        draw_text('50%', font2, black, win, 247, 440)
        pygame.draw.rect(win, black, (245,440,50,40), 3)
        
        pygame.draw.rect(win, white, soundeffects_vol4)
        draw_text('75%', font2, black, win, 292, 440)
        pygame.draw.rect(win, black, (290,440,50,40), 3)

        pygame.draw.rect(win, white, soundeffects_vol5)
        draw_text('100%', font2, black, win, 335, 440)
        pygame.draw.rect(win, black, (335,440,50,40), 3)

        if backbutton.collidepoint((mx, my)):
            if click:
                running = False
        if music_vol1.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.set_volume(0)                
        if music_vol2.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.set_volume(0.25)
        if music_vol3.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.set_volume(0.5)
        if music_vol4.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.set_volume(0.75)
        if music_vol5.collidepoint((mx, my)):
            if click:
                pygame.mixer.music.set_volume(1)
        if soundeffects_vol1.collidepoint((mx, my)):
            if click:
                fight_SE.set_volume(0)
                punch_SE.set_volume(0)
                kick_SE.set_volume(0)
                KO_SE.set_volume(0)                
        if soundeffects_vol2.collidepoint((mx, my)):
            if click:
                fight_SE.set_volume(0.25)
                punch_SE.set_volume(0.25)
                kick_SE.set_volume(0.25)
                KO_SE.set_volume(0.25)
        if soundeffects_vol3.collidepoint((mx, my)):
            if click:
                fight_SE.set_volume(0.5)
                punch_SE.set_volume(0.5)
                kick_SE.set_volume(0.5)
                KO_SE.set_volume(0.5)
        if soundeffects_vol4.collidepoint((mx, my)):
            if click:
                fight_SE.set_volume(0.75)
                punch_SE.set_volume(0.75)
                kick_SE.set_volume(0.75)
                KO_SE.set_volume(0.75)
        if soundeffects_vol5.collidepoint((mx, my)):
            if click:
                fight_SE.set_volume(1)
                punch_SE.set_volume(1)
                kick_SE.set_volume(1)
                KO_SE.set_volume(1)
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        pygame.display.update()
        clock.tick(60)


def controls():
    running = True
    while running:
        win.blit(controlsbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        backbutton = pygame.Rect(150,560,200,50)
        
        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Back', font, black, win, 160, 565)
        pygame.draw.rect(win, black, (150,560,200,50), 3)

        if backbutton.collidepoint((mx, my)):
            if click:
                running = False
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        
        pygame.display.update()
        clock.tick(60)




def pause():
    running = True
    while running:
        win.blit(pausebg, (0,0))

        mx, my = pygame.mouse.get_pos()

        continuebutton = pygame.Rect(45,315,230,40)
        settingsbutton = pygame.Rect(45,375,230,40)
        controlsbutton = pygame.Rect(45,436,230,40)
        mainmenubutton = pygame.Rect(150,560,200,50)

        pygame.draw.rect(win, (whitesmoke), continuebutton)
        draw_text('Continue', font, black, win, 70, 315)
        pygame.draw.rect(win, black, (45,315,230,40), 3)

        pygame.draw.rect(win, (whitesmoke), settingsbutton)
        draw_text('Settings', font, black, win, 70, 375)
        pygame.draw.rect(win, black, (45,375,230,40), 3)
        
        pygame.draw.rect(win, (whitesmoke), controlsbutton)
        draw_text('Controls', font, black, win, 70, 436)
        pygame.draw.rect(win, black, (45,436,230,40), 3)

        pygame.draw.rect(win, (whitesmoke), mainmenubutton)
        draw_text('Main Menu', font, black, win, 160, 565)
        pygame.draw.rect(win, black, (150,560,200,50), 3)

        if continuebutton.collidepoint((mx, my)):
            if click:
                running = False
        if settingsbutton.collidepoint((mx, my)):
            if click:
                settings()
        if controlsbutton.collidepoint((mx, my)):
            if click:
                controls()
        if mainmenubutton.collidepoint((mx, my)):
            if click:
                main_menu()
        
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        
        pygame.display.update()
        clock.tick(60)
        

def reset():
    char1.health += 1
    char2.health += 1
    char3.health += 1
    char4.health += 1
    char5.health += 1
    char6.health += 1
    
def c1_win():
    running = True
    while running:
        KO_SE.play()
        win.blit(c1Winbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        mainmenubutton = pygame.Rect(530,15,270,40)
        settingsbutton = pygame.Rect(230,15,270,40)
        newmatchbutton = pygame.Rect(830,15,270,40)
        
        pygame.draw.rect(win, (whitesmoke), mainmenubutton)
        draw_text('Main Menu', font, black, win, 535, 15)
        pygame.draw.rect(win, black, (530,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), settingsbutton)
        draw_text('Settings', font, black, win, 235, 15)
        pygame.draw.rect(win, black, (230,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), newmatchbutton)
        draw_text('New Match', font, black, win, 835, 15)
        pygame.draw.rect(win, black, (830,15,270,40), 3)

        reset()

        if mainmenubutton.collidepoint((mx, my)):
            if click:
                main_menu()
        if settingsbutton.collidepoint((mx, my)):
            if click:
                settings()
        if newmatchbutton.collidepoint((mx, my)):
            if click:
                character_Select_P1()
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
             
        pygame.display.update()
        clock.tick(60)

def c2_win():
    running = True
    while running:
        KO_SE.play()
        win.blit(c2Winbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        mainmenubutton = pygame.Rect(530,15,270,40)
        settingsbutton = pygame.Rect(230,15,270,40)
        newmatchbutton = pygame.Rect(830,15,270,40)
        
        pygame.draw.rect(win, (whitesmoke), mainmenubutton)
        draw_text('Main Menu', font, black, win, 535, 15)
        pygame.draw.rect(win, black, (530,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), settingsbutton)
        draw_text('Settings', font, black, win, 235, 15)
        pygame.draw.rect(win, black, (230,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), newmatchbutton)
        draw_text('New Match', font, black, win, 835, 15)
        pygame.draw.rect(win, black, (830,15,270,40), 3)

        reset()

        if mainmenubutton.collidepoint((mx, my)):
            if click:
                main_menu()
        if settingsbutton.collidepoint((mx, my)):
            if click:
                settings()
        if newmatchbutton.collidepoint((mx, my)):
            if click:
                character_Select_P1()
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
             
        pygame.display.update()
        clock.tick(60)


def c3_win():
    running = True
    while running:
        KO_SE.play()
        win.blit(c3Winbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        mainmenubutton = pygame.Rect(530,15,270,40)
        settingsbutton = pygame.Rect(230,15,270,40)
        newmatchbutton = pygame.Rect(830,15,270,40)
        
        pygame.draw.rect(win, (whitesmoke), mainmenubutton)
        draw_text('Main Menu', font, black, win, 535, 15)
        pygame.draw.rect(win, black, (530,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), settingsbutton)
        draw_text('Settings', font, black, win, 235, 15)
        pygame.draw.rect(win, black, (230,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), newmatchbutton)
        draw_text('New Match', font, black, win, 835, 15)
        pygame.draw.rect(win, black, (830,15,270,40), 3)

        reset()

        if mainmenubutton.collidepoint((mx, my)):
            if click:
                main_menu()
        if settingsbutton.collidepoint((mx, my)):
            if click:
                settings()
        if newmatchbutton.collidepoint((mx, my)):
            if click:
                character_Select_P1()
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
             
        pygame.display.update()
        clock.tick(60)
        

def c4_win():
    running = True
    while running:
        KO_SE.play()
        win.blit(c4Winbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        mainmenubutton = pygame.Rect(530,15,270,40)
        settingsbutton = pygame.Rect(230,15,270,40)
        newmatchbutton = pygame.Rect(830,15,270,40)
        
        pygame.draw.rect(win, (whitesmoke), mainmenubutton)
        draw_text('Main Menu', font, black, win, 535, 15)
        pygame.draw.rect(win, black, (530,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), settingsbutton)
        draw_text('Settings', font, black, win, 235, 15)
        pygame.draw.rect(win, black, (230,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), newmatchbutton)
        draw_text('New Match', font, black, win, 835, 15)
        pygame.draw.rect(win, black, (830,15,270,40), 3)

        reset()
        
        if mainmenubutton.collidepoint((mx, my)):
            if click:
                main_menu()
        if settingsbutton.collidepoint((mx, my)):
            if click:
                settings()
        if newmatchbutton.collidepoint((mx, my)):
            if click:
                character_Select_P1()
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
             
        pygame.display.update()
        clock.tick(60)


def c5_win():
    running = True
    while running:
        KO_SE.play()
        win.blit(c5Winbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        mainmenubutton = pygame.Rect(530,15,270,40)
        settingsbutton = pygame.Rect(230,15,270,40)
        newmatchbutton = pygame.Rect(830,15,270,40)
        
        pygame.draw.rect(win, (whitesmoke), mainmenubutton)
        draw_text('Main Menu', font, black, win, 535, 15)
        pygame.draw.rect(win, black, (530,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), settingsbutton)
        draw_text('Settings', font, black, win, 235, 15)
        pygame.draw.rect(win, black, (230,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), newmatchbutton)
        draw_text('New Match', font, black, win, 835, 15)
        pygame.draw.rect(win, black, (830,15,270,40), 3)

        reset()
        
        if mainmenubutton.collidepoint((mx, my)):
            if click:
                main_menu()
        if settingsbutton.collidepoint((mx, my)):
            if click:
                settings()
        if newmatchbutton.collidepoint((mx, my)):
            if click:
                character_Select_P1()
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
             
        pygame.display.update()
        clock.tick(60)


def c6_win():
    running = True
    while running:
        KO_SE.play()
        win.blit(c6Winbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        mainmenubutton = pygame.Rect(530,15,270,40)
        settingsbutton = pygame.Rect(230,15,270,40)
        newmatchbutton = pygame.Rect(830,15,270,40)
        
        pygame.draw.rect(win, (whitesmoke), mainmenubutton)
        draw_text('Main Menu', font, black, win, 535, 15)
        pygame.draw.rect(win, black, (530,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), settingsbutton)
        draw_text('Settings', font, black, win, 235, 15)
        pygame.draw.rect(win, black, (230,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), newmatchbutton)
        draw_text('New Match', font, black, win, 835, 15)
        pygame.draw.rect(win, black, (830,15,270,40), 3)

        reset()

        if mainmenubutton.collidepoint((mx, my)):
            if click:
                main_menu()
        if settingsbutton.collidepoint((mx, my)):
            if click:
                settings()
        if newmatchbutton.collidepoint((mx, my)):
            if click:
                character_Select_P1()
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
             
        pygame.display.update()
        clock.tick(60)

def draw():
    running = True
    while running:
        win.blit(drawbg, (0,0))
        
        mx, my = pygame.mouse.get_pos()

        mainmenubutton = pygame.Rect(530,15,270,40)
        settingsbutton = pygame.Rect(230,15,270,40)
        newmatchbutton = pygame.Rect(830,15,270,40)
        
        pygame.draw.rect(win, (whitesmoke), mainmenubutton)
        draw_text('Main Menu', font, black, win, 535, 15)
        pygame.draw.rect(win, black, (530,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), settingsbutton)
        draw_text('Settings', font, black, win, 235, 15)
        pygame.draw.rect(win, black, (230,15,270,40), 3)

        pygame.draw.rect(win, (whitesmoke), newmatchbutton)
        draw_text('New Match', font, black, win, 835, 15)
        pygame.draw.rect(win, black, (830,15,270,40), 3)

        reset()

        if mainmenubutton.collidepoint((mx, my)):
            if click:
                main_menu()
        if settingsbutton.collidepoint((mx, my)):
            if click:
                settings()
        if newmatchbutton.collidepoint((mx, my)):
            if click:
                character_Select_P1()
                
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
             
        pygame.display.update()
        clock.tick(60)


def endless():
    running = True
    while running:
        win.blit(endlessbg, (0,0))

        mx, my = pygame.mouse.get_pos()

        c1vsc2button = pygame.Rect(340,200,200,80)
        c1vsc4button = pygame.Rect(340,300,200,80)
        c1vsc6button = pygame.Rect(340,400,200,80)
        c3vsc2button = pygame.Rect(740,200,200,80)
        c3vsc4button = pygame.Rect(740,300,200,80)
        c3vsc6button = pygame.Rect(740,400,200,80)
        c5vsc2button = pygame.Rect(240,550,200,80)
        c5vsc4button = pygame.Rect(540,550,200,80)
        c5vsc6button = pygame.Rect(840,550,200,80)
        backbutton = pygame.Rect(540,100,200,50)

        icon1 = pygame.transform.scale(imageone_load, (120,105))
        icon2 = pygame.transform.scale(imagetwo_load, (60,70))
        icon3 = pygame.transform.scale(imagethree_load, (95,105))
        icon4 = pygame.transform.scale(imagefour_load, (80,80))
        icon5 = pygame.transform.scale(imagefive_load, (70,68))
        icon6 = pygame.transform.scale(imagesix_load, (100,95))

        #Character 1 matchups
        pygame.draw.rect(win, (whitesmoke), c1vsc2button)
        win.blit(icon1, (320,190))
        draw_text('vs', font, black, win, 420, 215)
        win.blit(icon2, (470,205))
        pygame.draw.rect(win, black, c1vsc2button, 3)

        pygame.draw.rect(win, (whitesmoke), c1vsc4button)
        win.blit(icon1, (320,290))
        draw_text('vs', font, black, win, 420, 315)
        win.blit(icon4, (460,300))
        pygame.draw.rect(win, black, c1vsc4button, 3)

        pygame.draw.rect(win, (whitesmoke), c1vsc6button)
        win.blit(icon1, (320,390))
        draw_text('vs', font, black, win, 420, 415)
        win.blit(icon6, (450,395))
        pygame.draw.rect(win, black, c1vsc6button, 3)
        
        #Character 3 matchups
        pygame.draw.rect(win, (whitesmoke), c3vsc2button)
        win.blit(icon3, (735,190))
        draw_text('vs', font, black, win, 820, 215)
        win.blit(icon2, (870,205))
        pygame.draw.rect(win, black, c3vsc2button, 3)

        pygame.draw.rect(win, (whitesmoke), c3vsc4button)
        win.blit(icon3, (735,290))
        draw_text('vs', font, black, win, 820, 315)
        win.blit(icon4, (860,300))
        pygame.draw.rect(win, black, c3vsc4button, 3)

        pygame.draw.rect(win, (whitesmoke), c3vsc6button)
        win.blit(icon3, (735,390))
        draw_text('vs', font, black, win, 820, 415)
        win.blit(icon6, (855,395))
        pygame.draw.rect(win, black, c3vsc6button, 3)

        #Character 5 matchups
        pygame.draw.rect(win, (whitesmoke), c5vsc2button)
        win.blit(icon5, (250,555))
        draw_text('vs', font, black, win, 325, 570)
        win.blit(icon2, (373,555))
        pygame.draw.rect(win, black, c5vsc2button, 3)

        pygame.draw.rect(win, (whitesmoke), c5vsc4button)
        win.blit(icon5, (550,555))
        draw_text('vs', font, black, win, 625, 570)
        win.blit(icon4, (660,550))
        pygame.draw.rect(win, black, c5vsc4button, 3)

        pygame.draw.rect(win, (whitesmoke), c5vsc6button)
        win.blit(icon5, (850,555))
        draw_text('vs', font, black, win, 925, 570)
        win.blit(icon6, (950,545))
        pygame.draw.rect(win, black, c5vsc6button, 3)

        #back
        pygame.draw.rect(win, (whitesmoke), backbutton)
        draw_text('Back', font, black, win, 600, 100)
        pygame.draw.rect(win, black, backbutton, 3)


        if backbutton.collidepoint((mx, my)):
            if click:
                arcade()
        if c1vsc2button.collidepoint((mx, my)):
            if click:
                endless_c1vsc2()
        if c1vsc4button.collidepoint((mx, my)):
            if click:
                endless_c1vsc4()
        if c1vsc6button.collidepoint((mx, my)):
            if click:
                endless_c1vsc6()
        if c3vsc2button.collidepoint((mx, my)):
            if click:
                endless_c3vsc2()
        if c3vsc4button.collidepoint((mx, my)):
            if click:
                endless_c3vsc4()
        if c3vsc6button.collidepoint((mx, my)):
            if click:
                endless_c3vsc6()
        if c5vsc2button.collidepoint((mx, my)):
            if click:
                endless_c5vsc2()
        if c5vsc4button.collidepoint((mx, my)):
            if click:
                endless_c5vsc4()
        if c5vsc6button.collidepoint((mx, my)):
            if click:
                endless_c5vsc6()


        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True        
        
        pygame.display.update()
        clock.tick(60)


#Movement of character 1 (Endless)
def character1_endless():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and char1.x > char1.vel:
        char1.x -= char1.vel
        char1.left = True
        char1.right = False
        char1.punch = False
        char1.kick = False
        char1.crouch = False
        
    elif keys[pygame.K_d] and char1.x < 1200 - char1.width - char1.vel:
        char1.x += char1.vel
        char1.right = True
        char1.left = False
        char1.punch = False
        char1.kick = False
        char1.crouch = False
        
    elif keys[pygame.K_v]:
        char1.punch = True
        char1.right = False
        char1.left = False
        char1.kick = False
        char1.crouch = False
        punch_SE.play() 
        
    elif keys[pygame.K_s]:
        char1.crouch = True
        char1.kick = False
        char1.punch = False
        char1.right = False
        char1.left = False
        
    elif keys[pygame.K_b]:
        char1.kick = True
        char1.crouch = False
        char1.punch = False
        char1.right = False
        char1.left = False
        kick_SE.play() 
        
    else:
        char1.right = False
        char1.left = False
        char1.punch = False
        char1.kick = False
        char1.crouch = False
        char1.walkCount = 0

    
    if not(char1.isJump):
        if keys[pygame.K_w]:
            char1.isJump = True
            char1.right = False
            char1.left = False
            char1.punch = False
            char1.kick = False
            char1.crouch = False
            char1.walkCount = 0
    else:
        if char1.jumpCount >= -10:
            neg = 1
            if char1.jumpCount < 0:
                neg = -1
            char1.y -= (char1.jumpCount ** 2) * 0.5 * neg
            char1.jumpCount -= 1
        else:
            char1.isJump = False
            char1.jumpCount = 10

            

#Movement of character 2 (endless)
def character2_endless():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and char2.x > char2.vel:
        char2.x -= char2.vel
        char2.left = True
        char2.right = False
        char2.punch = False
        char2.kick = False
        char2.crouch = False
        
    elif keys[pygame.K_RIGHT] and char2.x < 1200 - char2.width - char2.vel:
        char2.x += char2.vel
        char2.right = True
        char2.left = False
        char2.punch = False
        char2.kick = False
        char2.crouch = False
        
    elif keys[pygame.K_COMMA]:
        char2.punch = True
        char2.right = False
        char2.left = False
        char2.kick = False
        char2.crouch = False            
        punch_SE.play() 
        
    elif keys[pygame.K_DOWN]:
        char2.crouch = True
        char2.kick = False
        char2.punch = False
        char2.right = False
        char2.left = False
        
    elif keys[pygame.K_PERIOD]:
        char2.kick = True
        char2.crouch = False
        char2.punch = False
        char2.right = False
        char2.left = False
        kick_SE.play() 
        
    else:
        char2.right = False
        char2.left = False
        char2.punch = False
        char2.kick = False
        char2.crouch = False
        char2.walkCount = 0
        
    if not(char2.isJump):
        if keys[pygame.K_UP]:
            char2.isJump = True
            char2.right = False
            char2.left = False
            char2.punch = False
            char2.kick = False
            char2.crouch = False
            char2.walkCount = 0
    else:
        if char2.jumpCount >= -10:
            neg = 1
            if char2.jumpCount < 0:
                neg = -1
            char2.y -= (char2.jumpCount ** 2) * 0.5 * neg
            char2.jumpCount -= 1
        else:
            char2.isJump = False
            char2.jumpCount = 10


#Movement of character 3 (endless)
def character3_endless():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and char3.x > char3.vel:
        char3.x -= char1.vel
        char3.left = True
        char3.right = False
        char3.punch = False
        char3.kick = False
        char3.crouch = False
        
    elif keys[pygame.K_d] and char3.x < 1200 - char3.width - char3.vel:
        char3.x += char3.vel
        char3.right = True
        char3.left = False
        char3.punch = False
        char3.kick = False
        char3.crouch = False
        
    elif keys[pygame.K_v]:
        char3.punch = True
        char3.right = False
        char3.left = False
        char3.kick = False
        char3.crouch = False
        punch_SE.play() 
        
    elif keys[pygame.K_s]:
        char3.crouch = True
        char3.kick = False
        char3.punch = False
        char3.right = False
        char3.left = False
        
    elif keys[pygame.K_b]:
        char3.kick = True
        char3.crouch = False
        char3.punch = False
        char3.right = False
        char3.left = False
        kick_SE.play() 
        
    else:
        char3.right = False
        char3.left = False
        char3.punch = False
        char3.kick = False
        char3.crouch = False
        char3.walkCount = 0

    
    if not(char3.isJump):
        if keys[pygame.K_w]:
            char3.isJump = True
            char3.right = False
            char3.left = False
            char3.punch = False
            char3.kick = False
            char3.crouch = False
            char3.walkCount = 0
    else:
        if char3.jumpCount >= -10:
            neg = 1
            if char3.jumpCount < 0:
                neg = -1
            char3.y -= (char3.jumpCount ** 2) * 0.5 * neg
            char3.jumpCount -= 1
        else:
            char3.isJump = False
            char3.jumpCount = 10


#Movement of character 4
def character4_endless():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and char4.x > char4.vel:
        char4.x -= char4.vel
        char4.left = True
        char4.right = False
        char4.punch = False
        char4.kick = False
        char4.crouch = False
        
    elif keys[pygame.K_RIGHT] and char4.x < 1200 - char4.width - char4.vel:
        char4.x += char4.vel
        char4.right = True
        char4.left = False
        char4.punch = False
        char4.kick = False
        char4.crouch = False
        
    elif keys[pygame.K_COMMA]:
        char4.punch = True
        char4.right = False
        char4.left = False
        char4.kick = False
        char4.crouch = False           
        punch_SE.play() 
        
    elif keys[pygame.K_DOWN]:
        char4.crouch = True
        char4.kick = False
        char4.punch = False
        char4.right = False
        char4.left = False
        
    elif keys[pygame.K_PERIOD]:
        char4.kick = True
        char4.crouch = False
        char4.punch = False
        char4.right = False
        char4.left = False
        kick_SE.play() 
        
    else:
        char4.right = False
        char4.left = False
        char4.punch = False
        char4.kick = False
        char4.crouch = False
        char4.walkCount = 0
        
    if not(char4.isJump):
        if keys[pygame.K_UP]:
            char4.isJump = True
            char4.right = False
            char4.left = False
            char4.punch = False
            char4.kick = False
            char4.crouch = False
            char4.walkCount = 0
    else:
        if char4.jumpCount >= -10:
            neg = 1
            if char4.jumpCount < 0:
                neg = -1
            char4.y -= (char4.jumpCount ** 2) * 0.5 * neg
            char4.jumpCount -= 1
        else:
            char4.isJump = False
            char4.jumpCount = 10


#Movement of character 5
def character5_endless():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and char5.x > char5.vel:
        char5.x -= char5.vel
        char5.left = True
        char5.right = False
        char5.punch = False
        char5.kick = False
        char5.crouch = False
        
    elif keys[pygame.K_d] and char5.x < 1200 - char5.width - char5.vel:
        char5.x += char5.vel
        char5.right = True
        char5.left = False
        char5.punch = False
        char5.kick = False
        char5.crouch = False
        
    elif keys[pygame.K_v]:
        char5.punch = True
        char5.right = False
        char5.left = False
        char5.kick = False
        char5.crouch = False           
        punch_SE.play() 
        
    elif keys[pygame.K_s]:
        char5.crouch = True
        char5.kick = False
        char5.punch = False
        char5.right = False
        char5.left = False
        
    elif keys[pygame.K_b]:
        char5.kick = True
        char5.crouch = False
        char5.punch = False
        char5.right = False
        char5.left = False
        kick_SE.play() 
        
    else:
        char5.right = False
        char5.left = False
        char5.punch = False
        char5.kick = False
        char5.crouch = False
        char5.walkCount = 0

    
    if not(char5.isJump):
        if keys[pygame.K_w]:
            char5.isJump = True
            char5.right = False
            char5.left = False
            char5.punch = False
            char5.kick = False
            char5.crouch = False
            char5.walkCount = 0
    else:
        if char5.jumpCount >= -10:
            neg = 1
            if char5.jumpCount < 0:
                neg = -1
            char5.y -= (char5.jumpCount ** 2) * 0.5 * neg
            char5.jumpCount -= 1
        else:
            char5.isJump = False
            char5.jumpCount = 10


#Movement of character 6
def character6_endless():
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and char6.x > char6.vel:
        char6.x -= char6.vel
        char6.left = True
        char6.right = False
        char6.punch = False
        char6.kick = False
        char6.crouch = False
        
    elif keys[pygame.K_RIGHT] and char6.x < 1200 - char6.width - char6.vel:
        char6.x += char4.vel
        char6.right = True
        char6.left = False
        char6.punch = False
        char6.kick = False
        char6.crouch = False
        
    elif keys[pygame.K_COMMA]:
        char6.punch = True
        char6.right = False
        char6.left = False
        char6.kick = False
        char6.crouch = False
        punch_SE.play() 
        
    elif keys[pygame.K_DOWN]:
        char6.crouch = True
        char6.kick = False
        char6.punch = False
        char6.right = False
        char6.left = False
        
    elif keys[pygame.K_PERIOD]:
        char6.kick = True
        char6.crouch = False
        char6.punch = False
        char6.right = False
        char6.left = False
        kick_SE.play() 
        
    else:
        char6.right = False
        char6.left = False
        char6.punch = False
        char6.kick = False
        char6.crouch = False
        char6.walkCount = 0
        
    if not(char6.isJump):
        if keys[pygame.K_UP]:
            char6.isJump = True
            char6.right = False
            char6.left = False
            char6.punch = False
            char6.kick = False
            char6.crouch = False
            char6.walkCount = 0
    else: 
       if char6.jumpCount >= -10:
            neg = 1
            if char6.jumpCount < 0:
                neg = -1
            char6.y -= (char6.jumpCount ** 2) * 0.5 * neg
            char6.jumpCount -= 1
       else:
            char6.isJump = False
            char6.jumpCount = 10


def endless_c1vsc2():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        keys = pygame.key.get_pressed()
    
        character1_endless()
        character2_endless()

        map_2()

        show_character1()
        show_character2()
                    
        pygame.display.update()
        clock.tick(60)

def endless_c1vsc4():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        keys = pygame.key.get_pressed()
    
        character1_endless()
        character4_endless()

        map_4()

        show_character1()
        show_character4()
                    
        pygame.display.update()
        clock.tick(60)

def endless_c1vsc6():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        keys = pygame.key.get_pressed()
    
        character1_endless()
        character6_endless()

        map_3()

        show_character1()
        show_character6()
                    
        pygame.display.update()
        clock.tick(60)

def endless_c3vsc2():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        keys = pygame.key.get_pressed()
    
        character3_endless()
        character2_endless()

        map_7()

        show_character3()
        show_character2()
                    
        pygame.display.update()
        clock.tick(60)

def endless_c3vsc4():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        keys = pygame.key.get_pressed()
    
        character3_endless()
        character4_endless()

        map_8()

        show_character3()
        show_character4()
                    
        pygame.display.update()
        clock.tick(60)

def endless_c3vsc6():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        keys = pygame.key.get_pressed()
    
        character3_endless()
        character6_endless()

        map_1()

        show_character3()
        show_character6()
                    
        pygame.display.update()
        clock.tick(60)
        

def endless_c5vsc2():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        keys = pygame.key.get_pressed()
    
        character5_endless()
        character2_endless()

        map_6()

        show_character5()
        show_character2()
                    
        pygame.display.update()
        clock.tick(60)

def endless_c5vsc4():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        keys = pygame.key.get_pressed()
    
        character5_endless()
        character4_endless()

        map_9()

        show_character5()
        show_character4()
                    
        pygame.display.update()
        clock.tick(60)

def endless_c5vsc6():
    pygame.mixer.music.stop()    
    music2 = pygame.mixer.music.load("Sound/soundtrack2.mp3")
    pygame.mixer.music.play(-1)
    fight_SE.play()

    running = True
    while running:
        
        mx, my = pygame.mouse.get_pos()
          
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            
        keys = pygame.key.get_pressed()
    
        character5_endless()
        character6_endless()

        map_5()

        show_character5()
        show_character6()
                    
        pygame.display.update()
        clock.tick(60)

main_menu()
    



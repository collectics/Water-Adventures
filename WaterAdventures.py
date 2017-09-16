

import pygame,sys,random,time
pygame.init()
pygame.mixer.pre_init(44110,16,2,4096)
pygame.display.set_caption("Water Adventures ~ 'The clean water crisis needs your help.'")

def imagesCollide(pic1,p1x,p1y,pic2,p2x,p2y):
    aRect = pic1.get_rect(center=[p1x,p1y])
    bRect = pic2.get_rect(center=[p2x,p2y])  
    
    if aRect.colliderect(bRect):
        return True
    else: 
        return False

def popUpMessage(m,size,t,c):
    font = pygame.font.SysFont("Calibri",size,True,False)
    text = font.render(m,True,c)
    text_width = text.get_width()
    text_height = text.get_height()    
    screen.blit(text,[screenWidth/2-.5*text_width,screenHeight/2-.5*text_height])
    pygame.display.update()
    pygame.time.delay(t*2500)

pygame.key.set_repeat(100,30)

# screenWidth and screenHeight
screenWidth = 1300
screenHeight =  650
screen = pygame.display.set_mode([screenWidth,screenHeight])

# Misc stuff
clock = pygame.time.Clock()
clock.tick(60)

# ------------LOADING STUFF

# Color Variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLD = (255, 200, 25)
GOLDRED = (255, 150, 25)
GREEN = (0, 255, 0)

# Loading Images and Sounds -- this is a lot.
grasslands  = pygame.image.load("images//grassland.jpg").convert()
grasslands = pygame.transform.scale(grasslands, (1700, 800))
startingscreen = pygame.image.load("images//starting.jpg").convert()
startingscreen  = pygame.transform.scale(startingscreen, (1700, 800))
forestmagic = pygame.image.load("images//forestmagic.jpg").convert()
forestmagic = pygame.transform.scale(forestmagic, (1700, 800))
portal = pygame.image.load("images//portal.jpg").convert()
portal  = pygame.transform.scale(portal, (1700, 800))
level6 = pygame.image.load("images//castle.jpg").convert()
level6 = pygame.transform.scale(level6, (1400, 800))
water = pygame.image.load("images//lake.png").convert()
water = pygame.transform.scale(water, (1700, 800))
anotherforest = pygame.image.load("images//anotherforest.jpg").convert()
anotherforest = pygame.transform.scale(anotherforest, (1700, 800))
pig = pygame.image.load("images//piggy.png").convert_alpha() 
cow = pygame.image.load("images//cow.png").convert_alpha()
moremoney= pygame.image.load("images//money.png").convert_alpha() 
money= pygame.image.load("images//money.png").convert_alpha() 
powerupgreen= pygame.image.load("images//powerupgreen.png").convert_alpha() 
wasd= pygame.image.load("images//wasdarrows.png").convert() 
forest = pygame.image.load("images//forest.jpg").convert()
forest = pygame.transform.scale(forest, (1700, 800))
logo = pygame.image.load("images//wateradventures.png").convert_alpha()
moosound = pygame.mixer.Sound("sounds//moo.wav")
kazoo = pygame.mixer.Sound("sounds//kazoo.wav")
transition = pygame.mixer.Sound("sounds//transition.wav")
teleporter = pygame.mixer.Sound("sounds//teleporter.wav")
imapig = pygame.mixer.Sound("sounds//imapig.wav")
nyancat = pygame.mixer.Sound("sounds//nyancat.wav")
oinksound = pygame.mixer.Sound("sounds//oink.wav")
teleport = pygame.mixer.Sound("sounds//teleport.wav")
moon = pygame.image.load("images//moon.jpg").convert()
moon  = pygame.transform.scale(moon, (1700, 800))
watchdog = pygame.image.load("images//watchdog.png").convert_alpha()
horizwatchdog = pygame.image.load("images//horizwatchdog.png").convert_alpha()

imapig.play() # opening sound

#load fonts
smallFont = pygame.font.SysFont("Calibri",12,True,False)
mediumFont = pygame.font.SysFont("Calibri",18,True,False)
largeFont   = pygame.font.SysFont("Times New Roman",24,True,False)
extraLargeFont   = pygame.font.SysFont("Times New Roman",34,True,False)
extraExtraLargeFont   = pygame.font.SysFont("Times New Roman",45,True,False)
extraExtraExtraLargeFont = pygame.font.SysFont("Times New Roman",72,True,False)
extraExtraExtraExtraLargeFont   = pygame.font.SysFont("Times New Roman",96,True,False)


#initialize variables
background = water
easterscore = 0
easteregg = False
level = 1
moneypig = 0
moneycow = 0
dogcowtimer = 120
dogpigtimer = 120
pigx = 500
pigy = 475
cowx = 700
cowy = 475
moremoneyx = 20
moremoneyy = -25
background2timer = 0
background3timer = 0
background4timer = 0
background5timer = 0
background6timer = 0
teleportingtimer = 0
watchdogx = 5200
watchdogy = 5200
watchdogtimer = 1
horizwatchdogx = 5200
horizwatchdogy = 5200
piggypresx = 5200
piggypresy = 5200
powerupgreenx = 5200
powerupgreeny = 5200
powerupgreenspeed = 0.1
powerupgreencowtimer = 1000
powerupgreenpigtimer = 1000
moremoneyspeed = 5
moneyspeed = 2.5
watchdogspeed = 2
horizwatchdogspeed = 1
powerupgreentimer = 0
horizwatchdogtimer = 0
moneyx = 600
moneyy = -25
powerupspeedpig = 0
powerupspeedcow = 0
finalbosstimer = 0

horizwatchdogSpawn = False
done = False
watchdogSpawn = False
teleporting = False
watchdogTeleportCow = False
watchdogTeleportPig = False
kazoopig = False
kazoocow = False
watchdogdiagonal = True
horizwatchdogleft = False
easteregg = False

# ---------INTRO SCREEN
screen.blit(startingscreen,[0,0])
screen.blit(logo,[100,50])
text = extraLargeFont.render("A clean water crisis impacts Hypixelville. Cute Piggy and Ugly Cow are fighting for money.", True,GOLDRED)
screen.blit(text,[0,410])
text = extraLargeFont.render("The PIG wants money to donate to Charity: Water. The COW wants money for himself.", True,GOLDRED)
screen.blit(text,[15,435])
text = extraLargeFont.render("Choose a character and COLLECT MONEY for your goal...", True,GOLD)
screen.blit(text,[265,460])
text = extraLargeFont.render("By Collectics", True,GOLD)
screen.blit(text,[600,265])
text = extraExtraExtraLargeFont.render("PIG:", True,GOLDRED)
screen.blit(text,[300,500])
text = extraExtraExtraLargeFont.render("COW:", True,GOLDRED)
screen.blit(text,[750,500])
screen.blit(wasd,[450,500])
pygame.mixer.music.load('sounds//background.wav')
pygame.mixer.music.set_volume(0.85)
pygame.mixer.music.play(-1)
pygame.display.update()

pygame.time.delay(16000)
 
# -------- Main Program

while not done :

    screen.fill(WHITE)
    screen.blit(background,[0,0])
    text = extraExtraExtraLargeFont.render("Pig: $" + str(moneypig), False, GOLD)
    screen.blit(text, (0,0))
    text = extraExtraExtraLargeFont.render("Cow: $" + str(moneycow), False, GOLD)
    screen.blit(text, (925,0))
    dogcowtimer = dogcowtimer + 0.5
    dogpigtimer = dogpigtimer + 0.5  
  
# ---------Movement, Keypress Input, and Screen blit

    screen.blit(pig,  (pigx,pigy)   )
    screen.blit(cow,  (cowx,cowy)   ) 
    screen.blit(money,  (moneyx,moneyy)   )
    screen.blit(moremoney,  (moremoneyx,moremoneyy)   )   
    screen.blit(watchdog,  (watchdogx,watchdogy)   ) 
    screen.blit(horizwatchdog,  (horizwatchdogx,horizwatchdogy)   ) 
    screen.blit(powerupgreen,  (powerupgreenx,powerupgreeny)   ) 
    pygame.display.update()
    
    if pigx < -100  :
        pigx = 1200
        teleport.play()
    if pigx > 1200 :
        pigx = 0
        teleport.play()
    if cowx < -145 :
        cowx = 1200
        teleport.play()
    if cowx > 1200 :
        cowx = 0
        teleport.play()
        
# Movement! Fun fact: I discovered the else statement here. It was really, really useful for this section.
    keys_pressed = pygame.key.get_pressed()  
    if keys_pressed[pygame.K_LEFT]:
        if level >= 5:
            cowx -= 9 + powerupspeedcow
        else:
            cowx -= 5 + powerupspeedcow
    if keys_pressed[pygame.K_RIGHT]:
        if level >= 5:
            cowx += 9 + powerupspeedcow
        else:
            cowx += 5 + powerupspeedcow
    if keys_pressed[pygame.K_a]:
        if level >= 5:
            pigx -= 9 + powerupspeedpig
        else:
            pigx -= 5 + powerupspeedpig
    if keys_pressed[pygame.K_d]:
        if level >= 5:
            pigx += 9 + powerupspeedpig
        else:
            pigx += 5 + powerupspeedpig

#----------FALLING MONEY

    moneyy = moneyy + moneyspeed
    if moneyy > screenHeight :
        moneyx = random.randrange(0,screenWidth)
        moneyy = -25     
        
    if imagesCollide(pig,pigx,pigy,money,moneyx,moneyy) :
        if watchdogTeleportPig == False:
            moneyx = random.randrange(0,screenWidth)
            moneyy = -25    
            moneypig = moneypig + 1         
            oinksound.play()        

    if imagesCollide(cow,cowx,cowy,money,moneyx,moneyy) :
        if watchdogTeleportCow == False:
            moneyx = random.randrange(0,screenWidth)
            moneyy = -25         
            moneycow = moneycow + 1
            moosound.play()    
    
    moremoneyy = moremoneyy + moremoneyspeed
    if moremoneyy > screenHeight :
        moremoneyx = random.randrange(0,screenWidth)
        moremoneyy = -25    
        
    if imagesCollide(pig,pigx,pigy,moremoney,moremoneyx,moremoneyy) :
        if watchdogTeleportPig == False:
            moremoneyx = random.randrange(0,screenWidth)
            moremoneyy = -25         
            moneypig = moneypig + 1     
            oinksound.play()
              
    if imagesCollide(cow,cowx,cowy,moremoney,moremoneyx,moremoneyy) :
        if watchdogTeleportCow == False:
            moremoneyx = random.randrange(0,screenWidth)
            moremoneyy = -25         
            moneycow = moneycow + 1
            moosound.play()  
        
    # prevent negatives
    if moneycow < 0 :
        moneycow = 0
       
    if moneypig < 0 :
        moneypig = 0 
            
# --------POWERUPS
    
    powerupgreeny = powerupgreeny + powerupgreenspeed
    if powerupgreeny > screenHeight :
        powerupgreenx = random.randrange(0,screenWidth)
        powerupgreeny = -25     
    if watchdogTeleportPig == False:
        if kazoopig == False:
            if imagesCollide(pig,pigx,pigy,powerupgreen,powerupgreenx,powerupgreeny) :
                powerupgreenx = random.randrange(0,screenWidth)
                powerupgreeny = -25           
                oinksound.play() 
                powerupgreenpigtimer = 0
                kazoo.play()
                kazoopig = True
    if watchdogTeleportCow == False:
        if kazoocow == False:
            if imagesCollide(cow,cowx,cowy,powerupgreen,powerupgreenx,powerupgreeny) :
                powerupgreenx = random.randrange(0,screenWidth)
                powerupgreeny = -25      
                moosound.play()
                powerupgreencowtimer = 0
                kazoo.play()
                kazoocow = True
        
    powerupgreencowtimer = powerupgreencowtimer + 1
    powerupgreenpigtimer = powerupgreenpigtimer + 1
    if powerupgreencowtimer < 500 :
        powerupspeedcow = 50
    if powerupgreencowtimer > 500:
        powerupspeedcow = 0
        kazoocow = False
    if powerupgreenpigtimer < 500 :
        powerupspeedpig = 50
    if powerupgreenpigtimer > 500:
        powerupspeedpig = 0 
        kazoopig = False
    if powerupgreenpigtimer == 300:
        powerupgreenpigtimer = 301
    if powerupgreencowtimer == 300:
        powerupgreencowtimer = 301

    if watchdogSpawn == True:
        watchdogy = watchdogy + watchdogspeed
        if watchdogy > screenHeight :
            watchdogx = random.randrange(150,1050)
            watchdogy = -25
        if watchdogTeleportPig == False: 
            if powerupspeedpig != 50:
                if dogpigtimer > 130:
                    if level != 5:
                        if imagesCollide(pig,pigx,pigy,watchdog,watchdogx,watchdogy) :
                            watchdogx = random.randrange(0,screenWidth)
                            watchdogy = -25         
                            oinksound.play()
                            moneypig = moneypig - 3
                            dogpigtimer = 30
                            watchdogSpawn = False
        if watchdogTeleportCow == False:
            if powerupspeedcow != 50:
                if level != 5:
                    if dogcowtimer > 130:
                        if imagesCollide(cow,cowx,cowy,watchdog,watchdogx,watchdogy) :
                            watchdogx = random.randrange(0,screenWidth)
                            watchdogy = -25  
                            moosound.play()
                            moneycow = moneycow - 3
                            dogcowtimer = 30
                            watchdogSpawn = False    
                        
    if horizwatchdogSpawn == True:
        if horizwatchdogleft == True:
            horizwatchdogx = horizwatchdogx - horizwatchdogspeed
        else:
            horizwatchdogx = horizwatchdogx + horizwatchdogspeed
        if horizwatchdogx > screenWidth :
            horizwatchdogy = 375
            horizwatchdogx = 0 
        if horizwatchdogx < 0 :
            horizwatchdogy = 375
            horizwatchdogx = screenWidth          
        if watchdogTeleportPig == False:
            if powerupspeedpig != 50:
                if dogpigtimer > 130:
                    if imagesCollide(pig,pigx,pigy,horizwatchdog,horizwatchdogx,horizwatchdogy) :
                        horizwatchdogy = 375
                        horizwatchdogx = -150        
                        oinksound.play()
                        dogpigtimer = 30
                        horizwatchdogSpawn = False
                        moneypig = moneypig - 3
        if watchdogTeleportCow == False:
            if powerupspeedcow != 50:
                if dogcowtimer > 130:
                    if imagesCollide(cow,cowx,cowy,horizwatchdog,horizwatchdogx,horizwatchdogy) :
                        horizwatchdogy = 375
                        horizwatchdogx = -150 
                        moosound.play()
                        moneycow = moneycow - 3
                        dogcowtimer = 30
                        horizwatchdogSpawn = False
# Teleporting        
    if dogcowtimer == 30 :
        watchdogTeleportCow = True
        
    if watchdogTeleportCow == True:
        cowx = random.randrange(200,1000)
        cowy = random.randrange(200,400)  
        teleport.play()
            
    if dogcowtimer == 90 :
        cowx = random.randrange(200,1000)
        cowy = 475
        watchdogSpawn = True
        horizwatchdogSpawn = True
        watchdogTeleportCow = False
        
    if dogpigtimer == 30:
        watchdogTeleportPig = True
        
    if watchdogTeleportPig == True:
        pigx = random.randrange(200,1000)
        pigy = random.randrange(200,400)  
        teleport.play()
        
    if dogpigtimer == 90 :
        pigx = random.randrange(200,1000)
        pigy = 475
        watchdogSpawn = True
        horizwatchdogSpawn = True
        watchdogTeleportPig = False
        
#Spawning
    
    if watchdogSpawn == False :
        watchdogx = 5200
        watchdogy = 5200
        
    if horizwatchdogSpawn == False:
        horizwatchdogx = 5200
        horizwatchdogy = 5200
# Diagonal Movement and Left/Right HorizontalWatchdog
    if level >= 3:
        if watchdogtimer > 35:
            watchdogdiagonal = True
        if watchdogtimer < -35:
            watchdogdiagonal = False
            
        if watchdogdiagonal == True:
            if level == 3:
                watchdogx += 2.5
            else:
                watchdogx += 3.5
                horizwatchdogy -= 4
            watchdogtimer = watchdogtimer - 1
        if watchdogdiagonal == False:
            if level == 3:
                watchdogx -= 2.5
            else:
                watchdogx -= 3.5
                horizwatchdogy += 4
            watchdogtimer = watchdogtimer + 1
            
        if level == 6:
            if horizwatchdogleft == True:
                horizwatchdogtimer = horizwatchdogtimer + 1
            else:
                horizwatchdogtimer = horizwatchdogtimer - 1
                
            if horizwatchdogtimer > 300:
                horizwatchdogleft = False
            
            if horizwatchdogtimer < 0:
                horizwatchdogleft = True
                
                
#Watchdog done. Finally. Moving on:

# ---------Background Music
    if background2timer == 1 :
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds//energy.wav')
        pygame.mixer.music.set_volume(0.85)
        pygame.mixer.music.play(-1) 
        
    if background3timer == 1 :
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds//sweet.wav')
        pygame.mixer.music.set_volume(0.95)
        pygame.mixer.music.play(-1)     
    
    if background4timer == 1:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds//waltz.wav')
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.play(-1)    
        
    if background5timer == 1:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds//itvara.wav')
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1) 
        
    if background6timer == 1:
        pygame.mixer.music.stop()
        pygame.mixer.music.load('sounds//rocktronik.wav')
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1) 
        background = level6        
        
# ---------------leveling system... the meat of the game!

    if level == 1:
        pygame.display.set_caption("Water Adventures - 'FACT: One in ten people lack access to CLEAN WATER.'")
        moremoneyx = 5200
        moremoneyy = 5200
        watchdogSpawn = False
        horizwatchdogSpawn = False
        powerupgreenx = 5200
        powerupgreeny = 5200        
                
        if moneypig == 10 :
            level = 1.5
        
        if moneycow == 10 :
            level = 1.5
            
    if level == 1.5:
        teleporting = True
        
    if level == 2: 
        pygame.display.set_caption("Water Adventures - 'FACT: One in three people lack access to a toilet. In fact...'")
        background = forest
        moneyspeed = 10
        moremoneyx = 5200
        moremoneyy = 5200
        powerupgreenx = 9909
        powerupgreeny = 234587
        horizwatchdogSpawn = False 
        watchdogSpawn = True
        background2timer = background2timer + 1
        if moneypig == 30 :
            level = 2.5
            
        if moneycow == 30 :
            level = 2.5
            
    if level == 2.5:
        teleporting = True
                
    if level == 3:
        pygame.display.set_caption("Water Adventures - 'FACT: More people have a mobile phone than a toilet.'")
        moneyspeed = 15
        powerupgreenx = 5200
        powerupgreeny = 5200 
        background3timer = background3timer + 1
        background = grasslands
        horizwatchdogSpawn = False            
        if moneypig == 60:
            level = 3.5
        
        if moneycow == 60:
            level = 3.5
            
    if level == 3.5:
        teleporting = True
        
    if level == 4:
        pygame.display.set_caption("Water Adventures - 'FACT: Twice the population of the United States lives without access to clean water.'")
        background = forestmagic
        background4timer = background4timer + 1
        horizwatchdogSpawn = False          
        if moneypig == 100:
            level = 4.5
        
        if moneycow == 100:
            level = 4.5
            
    if level == 4.5:
        teleporting = True
                
    if level == 5:
        pygame.display.set_caption("Water Adventures - 'FACT: That is 663,000,000 PEOPLE. That's insane.'")
        horizwatchdogSpawn = True
        background = anotherforest
        background5timer = background5timer + 1
        watchdogspeed = 6
        watchdogSpawn = False
        if moneypig == 130 :
            level = 5.5
        
        if moneycow == 130 :
            level = 5.5      
            
    if level == 5.5:
        teleporting = True
        
    if level == 6:
        pygame.display.set_caption("Water Adventures - 'FACT: YOU can help...''")   
        background6timer = background6timer + 1
        watchdogspeed = 2
        horizwatchdogspeed = 2
        watchdogSpawn = True
        if moneycow == 155:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds//victory.wav')
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(1) 
            moneycow = 0
            text = extraExtraLargeFont.render("Ugly Cow kept all the money for himself.", True,BLACK)
            screen.blit(text,[300,115])
            text = extraLargeFont.render("Hypixelville died as no one could drink clean water.", True,BLACK) 
            screen.blit(text,[250,165])    
            text = extraExtraLargeFont.render("Donate to Charity: Water at https://my.charitywater.org/donate/", True,BLACK) 
            screen.blit(text,[30,65])             
            popUpMessage("Ugly Cow wins. :(", 150, 100, GOLD) 
            
        if moneypig == 155:
            pygame.mixer.music.stop()
            pygame.mixer.music.load('sounds//victory.wav')
            pygame.mixer.music.set_volume(0.7)
            pygame.mixer.music.play(1)
            moneycow = 0
            text = extraExtraLargeFont.render("Cute Piggy was able to donate to charity.", True,BLACK)
            screen.blit(text,[200,115])
            text = extraLargeFont.render("Because of his actions, engineers can cure the clean water crisis!", True,BLACK) 
            screen.blit(text,[150,165])    
            text = extraExtraLargeFont.render("Donate to Charity: Water at https://my.charitywater.org/donate/", True,BLACK) 
            screen.blit(text,[30,65])
            popUpMessage("Cute Piggy wins! :D", 150, 100, GOLD)          
            
#------TELEPORTATION TO NEXT LEVELS

    if teleporting == True :
        transition.play()
        teleporter.play()
        background = portal
        watchdogx = 5200
        watchdogy = 5200
        horizwatchdogx = 5200
        horizwatchdogy = 5200
        moneyx = 5200
        moneyy = 5200
        moremoneyx = 5200
        moremoneyy = 5200
        powerupgreenx = 5200
        powerupgreeny = 5200
        teleportingtimer = teleportingtimer + 1
        pygame.display.set_caption("Water Adventures - 'Teleporting...'")
        pigx = 300
        pigy = 475
        cowx = 700
        cowy = 475        
        
    if teleportingtimer > 150 :
        level = level + 0.5
        teleporting = False
        teleportingtimer = 0
        # ---------EASTER EGGS/SUGGESTED INSANO FEATURES
        # ....send cute piggy into space :D

    if keys_pressed[pygame.K_SPACE]:
        easterscore = easterscore + 1

    if easterscore > 350:
        level = 0
        background = moon
        moremoneyx = 5200
        moremoneyy = 5200
        watchdogSpawn = False
        horizwatchdogSpawn = False
        moneyx = 5000
        moneyy = 5000
        powerupgreenx = 5200
        powerupgreeny = 5200
        pygame.mixer.music.stop()
        easteregg = True
        pygame.display.set_caption("space piggy :D")
        if easterscore == 351:
            nyancat.play()
        if easteregg == True:
            pigy = pigy - 0.3
            text = extraExtraLargeFont.render("cute piggy is now president of the moon. the end", True, GOLD)
            moneypig += 1
            screen.blit(text, (250, 400))
            pygame.display.update()

                    #----ABORTING GAME
    if keys_pressed[pygame.K_x]:
        pygame.quit()
        sys.exit() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
pygame.quit()
sys.exit()

#------------ CREDITS
#Thank you to:
# Music: bensound.com and freesound.com
# "Waltz of the Carnies" and "Cyborg Ninja" Kevin MacLeod (incompetech.com)
# Licensed under Creative Commons: By Attribution 3.0 License
 # http://creativecommons.org/licenses/by/3.0/
#Monstercat: 
#Fractal - Itvara
#Facebook: http://facebook.com/fractalmusic
#Twitter: http://twitter.com/officialfractal
#Soundcloud: https://soundcloud.com/officialfractal
#Youtube: http://youtube.com/officialfractal
#Link To Itvara: https://www.youtube.com/watch?v=Q1Y_AZ8fJD0

#Pegboard Nerds - Rocktronik
#Soundcloud: http://www.soundcloud.com/pegboardnerds
#Facebook: http://www.facebook.com/PegboardNerds
#Twitter: http://www.twitter.com/PegboardNerds
#Youtube: http://www.youtube.com/PegboardNerds
#Bookings & Management : http://www.zooproduction.dk
# Link: https://www.youtube.com/watch?v=CzQkLV6QdYc

# Final Fantasy VII - Victory Fanfare
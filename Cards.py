"""
Name    : Shrivatsa Mishra
Roll no.: 2019335
Section : B
"""

import pygame
from random import *

pygame.init()

#Set of Suits
Suits=["Spades","Clubs","Hearts","Diamonds"]

#Set of all values of card
vals=[2,3,4,5,6,7,8,9,10,11,12,13,14]

#Class for card
class Card:
    def __init__(self, val, suit):
        self.val = val
        self.Suit = suit
        #Sets the image of card
        if(self.Suit==("Clubs")):
            if(self.val==(14)):
                self.image=pygame.image.load("C1.png")
            if(self.val==(2)):
                self.image=pygame.image.load("C2.png")
            if(self.val==(3)):
                self.image=pygame.image.load("C3.png")
            if(self.val==(4)):
                self.image=pygame.image.load("C4.png")
            if(self.val==(5)):
                self.image=pygame.image.load("C5.png")
            if(self.val==(6)):
                self.image=pygame.image.load("C6.png")
            if(self.val==(7)):
                self.image=pygame.image.load("C7.png")
            if(self.val==(8)):
                self.image=pygame.image.load("C8.png")
            if(self.val==(9)):
                self.image=pygame.image.load("C9.png")
            if(self.val==(10)):
                self.image=pygame.image.load("C10.png")
            if(self.val==(11)):
                self.image=pygame.image.load("C11.png")
            if(self.val==(12)):
                self.image=pygame.image.load("C12.png")
            if(self.val==(13)):
                self.image=pygame.image.load("C13.png")
        if(self.Suit==("Diamonds")):
            if(self.val==(14)):
                self.image=pygame.image.load("D1.png")
            if(self.val==(2)):
                self.image=pygame.image.load("D2.png")
            if(self.val==(3)):
                self.image=pygame.image.load("D3.png")
            if(self.val==(4)):
                self.image=pygame.image.load("D4.png")
            if(self.val==(5)):
                self.image=pygame.image.load("D5.png")
            if(self.val==(6)):
                self.image=pygame.image.load("D6.png")
            if(self.val==(7)):
                self.image=pygame.image.load("D7.png")
            if(self.val==(8)):
                self.image=pygame.image.load("D8.png")
            if(self.val==(9)):
                self.image=pygame.image.load("D9.png")
            if(self.val==(10)):
                self.image=pygame.image.load("D10.png")
            if(self.val==(11)):
                self.image=pygame.image.load("D11.png")
            if(self.val==(12)):
                self.image=pygame.image.load("D12.png")
            if(self.val==(13)):
                self.image=pygame.image.load("D13.png")
        if(self.Suit==("Spades")):
            if(self.val==(14)):
                self.image=pygame.image.load("S1.png")
            if(self.val==(2)):
                self.image=pygame.image.load("/S2.png")
            if(self.val==(3)):
                self.image=pygame.image.load("/S3.png")
            if(self.val==(4)):
                self.image=pygame.image.load("S4.png")
            if(self.val==(5)):
                self.image=pygame.image.load("S5.png")
            if(self.val==(6)):
                self.image=pygame.image.load("S6.png")
            if(self.val==(7)):
                self.image=pygame.image.load("S7.png")
            if(self.val==(8)):
                self.image=pygame.image.load("S8.png")
            if(self.val==(9)):
                self.image=pygame.image.load("S9.png")
            if(self.val==(10)):
                self.image=pygame.image.load("S10.png")
            if(self.val==(11)):
                self.image=pygame.image.load("S11.png")
            if(self.val==(12)):
                self.image=pygame.image.load("S12.png")
            if(self.val==(13)):
                self.image=pygame.image.load("S13.png")
        if(self.Suit==("Hearts")):
            if(self.val==(14)):
                self.image=pygame.image.load("H1.png")
            if(self.val==(2)):
                self.image=pygame.image.load("H2.png")
            if(self.val==(3)):
                self.image=pygame.image.load("H3.png")
            if(self.val==(4)):
                self.image=pygame.image.load("H4.png")
            if(self.val==(5)):
                self.image=pygame.image.load("H5.png")
            if(self.val==(6)):
                self.image=pygame.image.load("H6.png")
            if(self.val==(7)):
                self.image=pygame.image.load("H7.png")
            if(self.val==(8)):
                self.image=pygame.image.load("H8.png")
            if(self.val==(9)):
                self.image=pygame.image.load("H9.png")
            if(self.val==(10)):
                self.image=pygame.image.load("H10.png")
            if(self.val==(11)):
                self.image=pygame.image.load("H11.png")
            if(self.val==(12)):
                self.image=pygame.image.load("H12.png")
            if(self.val==(13)):
                self.image=pygame.image.load("H13.png")
        self.image=pygame.transform.scale(self.image,(75,100))

#These are the decks

#Full deck is used to reset Use deck evergy game
full_Deck=[]

#Use deck is reset in ever game
use_Deck=[]

#Player Deck is the deck available to player
player_Deck=[]

#Com deck is the deck available to the computer
com_Deck=[]



#This sets the full deck
def Create_Deck():
    for suit in Suits:
        for val in vals:
            full_Deck.append(Card((val),(suit)))
    return full_Deck

#This draws a card randomly from the deck given
def Draw_card(deck):
    Rno = randint(0,len(deck)-1)
    return deck.pop(Rno)

#This divides the card b/w the pllayer and the computer
def Divide_cards():
    global player_Deck,com_Deck
    for i in range(0,11):
        player_Deck.append(Draw_card(use_Deck))
    for i in range(0,10):
        com_Deck.append(Draw_card(use_Deck))

#Partition a deck of card
def partition(nums, low, high):
    pivot = nums[(low + high) // 2].val
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i].val < pivot:
            i += 1
        j -= 1
        while nums[j].val > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]

#Sorts the vals of cards in deck
def quick_sort(nums):
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

#Sorts the given deck by suits and val
def Sort(deck):
    l=len(deck)
    dk=[[],[],[],[]]
    for i in range(l):
        if(deck[i].Suit=="Spades"):
            dk[0].append(deck[i])
        elif(deck[i].Suit=="Clubs"):
            dk[1].append(deck[i])
        elif(deck[i].Suit=="Diamonds"):
            dk[2].append(deck[i])
        elif(deck[i].Suit=="Hearts"):
            dk[3].append(deck[i])
    for i in range(4):
        quick_sort(dk[i])
    nDeck=dk[0]+dk[1]+dk[2]+dk[3]
    return nDeck

#This checks the location of mouse click
def check_Click(x,y):
    global take
    if(y>360):
        return ((x-50)//80)
    elif(y>200 and y<300):
        if(x>400 and x<475):
            take=1
        elif(x>500 and x<575):
            take=2
    return -1

#This exchanges the open card with selected card
def Take_open(i,j):
    global use_Deck,Open_Card,player_Deck
    temp_Card=Open_Card
    if(j==0):
        Open_Card=player_Deck[i]
        player_Deck.pop(i)
        player_Deck.append(temp_Card)
        Sort(player_Deck)
    else:
        Open_Card=com_Deck[i]
        com_Deck.pop(i)
        com_Deck.append(temp_Card)
        Sort(com_Deck)
    print(len(use_Deck))

#This exchanges the closed card with selected card
def Take_closed(i,j=0):
    global use_Deck,Open_Card,player_Deck
    if(j==0):
        Open_Card=player_Deck[i]
        player_Deck.pop(i)
        player_Deck.append(Draw_card(use_Deck))
        Sort(player_Deck)
    else:
        Open_Card=com_Deck[i]
        com_Deck.pop(i)
        com_Deck.append(Draw_card(use_Deck))
        Sort(com_Deck)
    print(len(use_Deck))

#This swaps player cards
def Swap(i,j,k=0):
    global player_Deck,com_Deck
    if(k==0):
        player_Deck[i],player_Deck[j]=player_Deck[j],player_Deck[i]
    else:
        com_Deck[i],com_Deck[j]=com_Deck[j],com_Deck[i]

#This decides computers move
def com_Move():
    global com_Deck,Open_Card
    com_Deck.append(Open_Card)
    com_Deck=Sort(com_Deck)
    per_Deck=[]
    fluid_Deck=[]
    for i in range(len(com_Deck)-2):
        if(com_Deck[i+1].val-com_Deck[i].val==1):
            if(com_Deck[i+2].val-com_Deck[i+1].val==1):
                per_Deck.append(com_Deck[i])
                per_Deck.append(com_Deck[i+1])
                per_Deck.append(com_Deck[i+2])
            else:
                fluid_Deck.append(com_Deck[i])
        else:
            fluid_Deck.append(com_Deck[i])
    if(len(com_Deck)-(len(per_Deck)+len(fluid_Deck))==2):
        fluid_Deck.append(com_Deck[len(com_Deck)-2])
        fluid_Deck.append(com_Deck[len(com_Deck)-1])
    elif(len(com_Deck)-(len(per_Deck)+len(fluid_Deck))==1):
        fluid_Deck.append(com_Deck[len(com_Deck)-1])
    if(Open_Card in per_Deck):
        com_Deck.remove(Open_Card)
        i=randint(0,len(com_Deck)-1)
        Take_open(i,1)
    else:
        com_Deck.remove(Open_Card)
        i=randint(0,len(com_Deck)-1)
        Take_open(i,1)


#This checks the end of the game
def End():
    global player_Deck,com_Deck,use_Deck,Points
    Points=0
    a=0
    b=0
    c=[]
    for i in range(len(player_Deck)):
        c.append(player_Deck[i].val)
    for i in range(len(player_Deck)-2):
        s=0
        for j in range(i+1,len(player_Deck)):
            if(c[i]==c[j]):
                s+=1
        if(s==2):
            Points+=3*(c[i])
            a+=1
    player_Deck=Sort(player_Deck)
    com_Deck=Sort(com_Deck)
    if(len(use_Deck)==0):
        return 1
    for i in range(len(player_Deck)-3):
        if(player_Deck[i+1].val-player_Deck[i].val==1):
            if(player_Deck[i+2].val-player_Deck[i+1].val==1):
                a+=1
                Points+=player_Deck[i].val
                Points+=player_Deck[i+1].val
                Points+=player_Deck[i+2].val
                if(player_Deck[i+2].val-player_Deck[i+3].val==1):
                    Points+=player_Deck[i+3].val
                    b+=1
                    a-=1
    if(a>=2 and b>=1):
        return 2
    a=0
    b=0
    c=[]
    for i in range(len(com_Deck)):
        c.append(com_Deck[i].val)
    for i in range(len(com_Deck)-2):
        s=0
        for j in range(i+1,len(com_Deck)):
            if(c[i]==c[j]):
                s+=1
        if(s==2):
            Points+=3*(c[i])
            a+=1
    if(len(use_Deck)==0):
        return 1
    for i in range(len(com_Deck)-3):
        if(com_Deck[i+1].val-com_Deck[i].val==1):
            if(com_Deck[i+2].val-com_Deck[i+1].val==1):
                a+=1
                Points+=com_Deck[i].val
                Points+=com_Deck[i+1].val
                Points+=com_Deck[i+2].val
                if(com_Deck[i+2].val-com_Deck[i+3].val==1):
                    Points+=com_Deck[i+3].val
                    b+=1
                    a-=1
    if(a>=2 and b>=1):
        return 3
    return 0

Create_Deck()
use_Deck=list(full_Deck)
Closed_card=pygame.image.load("Backside.png")
Closed_card=pygame.transform.scale(Closed_card,(75,100))

#This variable decides whether to take open card or closed card
take=0

#this variable decides the menu
menu=0

#This shows wthe nos of wins and losses
wins=0
losses=0

size=500
win = pygame.display.set_mode((2*size,size))

run=True
new_Game=True
take=0
no=0
Points=0
TPoints=0

pygame.display.set_caption("Rummy")

#Sets the font
font1 = pygame.font.Font('freesansbold.ttf', 32)

#Sets the texts
text1 = font1.render('New Game', True,(0,255,0),(255,0,0))
text1_box = text1.get_rect()
text1_box.center=(500,150)
text2 = font1.render('Load Game', True,(0,255,0),(255,0,0))
text2_box = text2.get_rect()
text2_box.center=(500,350)
text3 = font1.render('You Win', True,(0,0,255),(0,255,100))
text3_box = text3.get_rect()
text3_box.center=(500,250)
text4 = font1.render('You have : '+str(TPoints)+' points.', True,(255,0,0),(0,255,100))
text4_box = text4.get_rect()
text4_box.center=(500,250)
text5 = font1.render('You Loose', True,(0,0,255),(0,255,100))
text5_box = text5.get_rect()
text5_box.center=(500,250)


while run:
    pygame.time.delay(100)
    if(wins+losses==3):
        if(Points>=0):
            win.fill((0,255,100))
            win.blit(text3,text3_box)
        else:
            win.fill((0,255,100))
            win.blit(text5,text5_box)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
    elif(menu==0):
        win.fill((0,255,100))
        pygame.draw.rect(win,(255,0,0),(250,100,500,100))
        win.blit(text1,text1_box)
        pygame.draw.rect(win,(255,0,0),(250,300,500,100))
        win.blit(text2,text2_box)
        win.blit(text4,text4_box)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
            elif(event.type == pygame.MOUSEBUTTONUP):
                if(pygame.mouse.get_pos()[0]>250 and pygame.mouse.get_pos()[0]<750):
                    if(pygame.mouse.get_pos()[1]>100 and pygame.mouse.get_pos()[1]<200):
                        menu=1
                        new_Game=True
                    elif(pygame.mouse.get_pos()[1]>300 and pygame.mouse.get_pos()[1]<400):
                        menu=1
    elif(menu==1):
        win.fill((0,255,100))
        if new_Game:
            Points=0
            use_Deck=list(full_Deck)
            player_Deck=[]
            com_Deck=[]
            Open_Card=Draw_card(use_Deck)
            Divide_cards()
            new_Game=False
        player_Deck=Sort(player_Deck)
        pygame.draw.rect(win,(255,0,0),(0,250,100,50))
        pygame.draw.rect(win,(255,255,255),(20,265,50,20))
        pygame.draw.polygon(win,(255,255,255),((20,260),(20,290),(5,275)))
        for i in range(len(player_Deck)):
            win.blit(player_Deck[i].image,((80*i)+50,360))
        for i in range(len(com_Deck)):
            win.blit(Closed_card,((80*i)+50,80))
        win.blit(Open_Card.image,(400,200))
        win.blit(Closed_card,(500,200))


        for event in pygame.event.get():
            if(event.type == pygame.MOUSEBUTTONUP):
                c=check_Click(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                if(pygame.mouse.get_pos()[0]<100):
                    if(pygame.mouse.get_pos()[1]>250 and pygame.mouse.get_pos()[1]<300):
                        menu=0
                if(c!=-1 and c<len(player_Deck)):
                    c=check_Click(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                    if(take==1):
                        take=0
                        Take_open(c,0)
                    elif(take==2):
                        take=0
                        Take_closed(c)
                    pygame.display.update()
                    pygame.time.delay(1000)
                    com_Move()
                    pygame.display.update()
                    print(len(use_Deck))

            if event.type == pygame.QUIT:
                run=False
        if(End()==1):
            menu=0
        elif(End()==2):
            win.fill((0,255,100))
            win.blit(text3,text3_box)
            pygame.time.delay(2000)
            wins+=1
            TPoints+=Points
            menu=0
        elif(End()==3):
            win.fill((0,255,100))
            win.blit(text5,text5_box)
            pygame.time.delay(2000)
            losses+=1
            TPoints-=Points
            menu=0


    pygame.display.update()

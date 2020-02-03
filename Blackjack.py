import random

class Deck():
    def __init__(self):
        self.Suits=['Hearts','Spades','Diamonds','Clubs']
        self.Ranks={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10,'Ace':10}
        self.Cards=[]
        self.Myhand=0
        self.PChand=0
        for i in self.Suits:
            for x in self.Ranks:
                self.Cards.append(x+' of '+i)
        random.shuffle(self.Cards)
        self.ThisCard=self.Cards[0].split()
        self.PChand+=self.Ranks[self.ThisCard[0]]
        print('PC drew '+self.Cards[0])
        self.Cards.pop(0)
        self.Wincheck2()

    def Wincheck1(self):
        if self.Myhand>21:
            print('Bust')
            quit()

    def Wincheck2(self):
        if self.PChand>21:
            print('Bust')
            quit()

    def Hit(self):
        self.ThisCard=self.Cards[0].split()
        self.Myhand+=self.Ranks[self.ThisCard[0]]
        print('You drew '+self.Cards[0])
        self.Cards.pop(0)
        self.Wincheck1()

    def Draw(self):
        while self.PChand<=16:
            self.ThisCard=self.Cards[0].split()
            self.PChand+=self.Ranks[self.ThisCard[0]]
            print(self.Cards[0])
            self.Cards.pop(0)
            self.Wincheck2()

    def Wincheck(self):
        if self.PChand>self.Myhand:
            print('You Lost')
            quit()
        elif self.Myhand>self.PChand:
            print('You won')
            quit()
        else:
            print('Draw')
            quit()

    def Gameplay(self):
        while True:
            Choice=input('What will you do?\n1.Hit 2.Stand')
            if Choice=='1':
                self.Hit()
            elif Choice=='2':
                self.Draw()
                self.Wincheck()

Deck=Deck()
Deck.Gameplay()
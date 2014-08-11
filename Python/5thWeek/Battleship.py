'''Battleship game'''
from random import randint

ch_coord = {}
for i in range(0,10):
    ch_coord[chr(i+ord('A'))] = i + 1
    ch_coord[chr(i+ord('a'))] = i + 1
        
class Battlefield:
    def empty_field():
        field=[]                                            # Empty array will fills for battlefield
        for x in range(0,10):                               # First just zeros
            field.append(['0' for i in range(10)])
        field.insert(0,[i for i in range(11)])              # Number coordinates
        for char in range(ord('A'),ord('K')):               # Character coordinates
            field[char-ord('A')+1].insert(0, chr(char))
        field[0][0]=' '
        return(field)
    def show(field):
        for i in range(len(field)):                         # Prints nice looking battlefield
            print('')
            for j in field[i]:
                print(j,end=' ')
    def check(coordinates):                                 # Are coordinates valid?
        if len(coordinates) != 2:                           # Looks ugly, need to improve
            print('Wrong coordinates')
            return False
        x, y = coordinates[0], coordinates[1]
        if x.isalpha() and y.isdigit():
            y = int(y)
            if 0<y<11 and ('a'<=x<='j' or 'A'<=x<='J'):
                return ch_coord[x], y
        if x.isdigit() and y.isalpha():
            x = int(x)
            if 0<x<11 and ('a'<=y<='j' or 'A'<=y<='J'):
                return ch_coord[y], x
        else:
            print('Wrong coordinates')
            return False
    

class Player:
    def __init__(self):
        self.battleships = 1
        self.battlecruisers = 2
        self.cruisers = 3
        self.frigates = 4
        self.ships = self.battleships + self.battlecruisers + self.cruisers + self.frigates
        self.field = Battlefield.empty_field
        self.enemy_field = Battlefield.empty_field
    #def attack(self):

class Enemy(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = 'Enemy'

class Human(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = 'You'
        self.state = 'Waiting'
    #def help:
    def show(self):
        print("Yours field")
        Battlefield.show(self.field)
        print("Enemies field")
        Battlefield.show(self.enemy_field)
    def fill(self):
        if self.state != 'Waiting':
            print("Can't do it right now")
        print('Place your ships\n', 'Enter the coordinates of your ships one by one, like d4,G7 etc.')
        while self.ships > 0:
            coordinates = input('> ')
            while Battlefield.check(coordinates) != False:
                x, y = Battlefield.check(coordinates)
                self.field[x][y]='1'
                self.ships -= 1
                Battlefield.show(self.field)

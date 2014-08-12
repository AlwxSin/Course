'''Battleship game'''
from random import randint
        
class Battlefield:
    def __init__self(self):
        self.name = 'Battlefield'
    def empty_field(self):
        field=[]                                            # Empty array will fills for battlefield
        for x in range(0,5):                                # First just zeros
            field.append(['0' for i in range(5)])
        field.insert(0,[i for i in range(6)])               # Number coordinates
        for char in range(ord('A'),ord('F')):               # Character coordinates
            field[char-ord('A')+1].insert(0, chr(char))
        field[0][0]=' '
        return(field)
    def show(field):
        for i in range(len(field)):                         # Prints nice looking battlefield
            print('')
            for j in field[i]:
                print(j,end=' ')
    def check(coordinates):                                 # Are coordinates valid?
        x, y = coordinates[0], coordinates[1:]
        if x.isalpha() and y.isdigit():
            y = int(y)
            if 1<=y<=10 and ('a'<=x<='f' or 'A'<=x<='F'):
                if x.isupper():
                    return (ord(x)-ord('A')+1), y
                else: return (ord(x)-ord('a')+1), y
            else:
                print('Wrong coordinates')
                return False
        else:
            print('Wrong coordinates')
            return False
    

class Player:
    def __init__(self):
        #self.battleships = 1
        #self.battlecruisers = 2                    #For future
        #self.cruisers = 3
        #self.frigates = 4
        self.ships = 10                             # Number of overall tables with ships
        self.field = Battlefield.empty_field(Battlefield)
        self.enemy_field = Battlefield.empty_field(Battlefield)
    def attack(self):

class Enemy(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = 'Enemy'
    def fill(self):
        while self.ships > 0:
            x, y = randint(1,5), randint(1,5)
            if self.field[x][y] != '1':
                self.field[x][y] = '1'
                self.ships -= 1
            else: continue
        Battlefield.show(self.field)

class Human(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = 'You'
        self.state = 'Waiting'
    #def help:
    def show(self):
        print("Yours field")
        Battlefield.show(self.field)
        print("\n\nEnemies field")
        Battlefield.show(self.enemy_field)
    def fill(self):
        if self.state != 'Waiting':
            print("Can't do it right now")
        print('Place your ships','\nEnter the coordinates of your ships one by one, like d4,G7 etc.')
        print('You have %s ships remain' %self.ships)
        while self.ships > 0:
            coordinates = input('\n> ')
            if Battlefield.check(coordinates):
                x, y = Battlefield.check(coordinates)
                if self.field[x][y] == '1':
                    print('There is already ship in that location')
                else:
                    self.field[x][y]='1'
                    self.ships -= 1
                    Battlefield.show(self.field)
                    print('\n\nYou have %s ships remain' %self.ships)

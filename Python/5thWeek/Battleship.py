'''Battleship game'''
from random import randint

all_coord = set()                       # All coordinates, for future checks
for i in range(1,6):
    for j in range(ord('a'),ord('f')):
        x = chr(j)+str(i)
        all_coord.add(x)

class Battlefield:
    def empty_field(self):
        field=[]                                                    # Empty array will fills for battlefield
        for x in range(0,5):                                        # At first just zeros
            field.append(['0' for i in range(5)])
        field.insert(0,[i for i in range(6)])                       # Number coordinates
        for char in range(ord('a'),ord('a')):                       # Character coordinates
            field[char-ord('a')+1].insert(0, chr(char))
        field[0][0]=' '
        return(field)
    def show(field):
        for i in range(len(field)):                                 # Prints nice looking battlefield
            print('')
            for j in field[i]:
                print(j,end=' ')
    def check(coordinates):                                         # Are coordinates valid?
        x, y = coordinates[0], coordinates[1:]
        if x.isalpha() and y.isdigit():
            y = int(y)
            if 1<=y<=5 and ('a'<=x<='f' or 'A'<=x<='F'):
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
        self.name = ''
        self.ships = 2                                              # Number of overall tables with ships
        self.field = Battlefield.empty_field(Battlefield)
        self.enemy_field = Battlefield.empty_field(Battlefield)
        self.my_coord = all_coord
        self.killed = 0
    def fill(self):                                                 # Fill the battlefield in random way
        count = self.ships
        while count > 0:
            x, y = randint(1,5), randint(1,5)
            if self.field[x][y] != '1':
                self.field[x][y] = '1'
                count -= 1
            else: continue
        Battlefield.show(self.field)
    def attack(self):                                               # Function returns False if player missed and True in all other situations
        coord = self.my_coord.pop()                                 # Takes random coordinate from set of all coordinates
        x, y = Battlefield.check(coord)
        if self.enemy_field[x][y] == '0' and p.field[x][y] == '0':  # Miss
            print('%s misses ' %self.name + coord + '\n------------\n')
            self.enemy_field[x][y] = 'm'
            p.field[x][y] = 'm'
            return False
        if self.enemy_field[x][y] == 'm':                           # Already hit here
            return True
        if p.field[x][y] == '1':                                    # Hit confirmed
            print('%s HITS ' %self.name + coord + '\n------------\n')
            self.enemy_field[x][y] = '1'
            p.field[x][y] = 'X'
            self.killed += 1
            return True
        else: return True
    def show(self):
        print("Yours field")
        Battlefield.show(self.field)
        print("\n\nEnemies field")
        Battlefield.show(self.enemy_field)

class Enemy(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = 'Enemy'

class Human(Player):
    def __init__(self):
        Player.__init__(self)
        self.name = 'You'
    def fill_byhands(self):                                         # Fill battlefield manualy
        print('Place your ships','\nEnter the coordinates of your ships one by one, like d4,G7 etc.')
        print('You have %s ships remain' %self.ships)
        count = self.ships
        while count > 0:
            coordinates = input('\n> ')
            if Battlefield.check(coordinates):
                x, y = Battlefield.check(coordinates)
                if self.field[x][y] == '1':
                    print('There is already ship in that location')
                else:
                    self.field[x][y]='1'
                    count -= 1
                    Battlefield.show(self.field)
                    print('\n\nYou have %s ships remain' %self.ships)
    def attack(self, x, y):
        if self.enemy_field[x][y] == '0' and e.field[x][y] == '0':  # Miss
            print('\n------------\n'+'You miss'+'\n------------')
            self.enemy_field[x][y] = 'm'
            return False
        if self.enemy_field[x][y] == 'm':                           # Already hit here
            print('You already hit that place')
            return True
        if self.enemy_field[x][y] == '0' and e.field[x][y] == '1':  # Hit cinfirmed
            print('\n------------\n'+'You HIT'+'\n------------')
            self.enemy_field[x][y] = 'X'
            self.killed += 1
            return True
        else:
            print('Check again')
            return True

p = Human()
e = Enemy()
e.fill()
print("Let's start\n")
print('If you want to random fill your battlefield, type "random". If you want to fill manually, type "myself"')
while True:
    line = input('> ')
    if line == 'random': # If player don't want to fill manually
        p.fill()
        break
    if line == 'myself': # If player wants to fill manually
        p.fill_byhands()
        break
    else:
        print('Check your input')

while True:
    pendulum = 1                                                    # Just counter
    if pendulum == 1:
        coord = input('\nYour move. Print coordinates to fire\n')
        x, y = Battlefield.check(coord)
        result = p.attack(x,y)
        p.show()
        print('\n------------')
        if p.killed == p.ships:
            print('Congratulations. You won')
            break
        if not result: pendulum = 0                                 # Move goes to enemy
    if pendulum == 0:
        print("\nEnemy's move")
        result = e.attack()
        print('\n------------')
        if e.killed == e.ships:
            print('You lost')
            break
        if not result: pendulum = 1                                 # Move goes to enemy
        p.show()

# Enemy strike only once if he hits
# Бот, если попал, должен стрелять еще раз. До тех пор, пока не промахнется. Этого не происходит. Разобраться.
